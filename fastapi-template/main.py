from fastapi import FastAPI, HTTPException, Body
from models import MsgPayload
from pydantic import BaseModel
from typing import Optional, List, Any, Dict
from pymongo import MongoClient
from os import path, environ
from random import randint, choice, sample
from json import load
from feat_plugin_loader import load_feat_plugins
from plugins.types.feat_observer import FeatObserver

app = FastAPI()
messages_list: dict[int, MsgPayload] = {}

# MongoDB connection setup
MONGO_URL = environ.get("MONGO_URL", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URL)
db = client["fastapi_app"]
users_collection = db["users"]

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

class DnDCharacter(BaseModel):
    name: str
    race: str
    character_class: str
    base_abilities: dict[str, int]
    final_abilities: dict[str, int]
    racial_bonus: dict[str, int]
    racial_features: list[str]

class Feat(BaseModel):
    name: str
    description: str
    bonuses: Optional[dict[str, int]] = None  # e.g., {"strength": 1}
    prerequisites: Optional[str] = None

class CombatResult(BaseModel):
    attacker: str
    defender: str
    attack_roll: int
    hit: bool
    damage: int
    applied_feats: list[str]
    notes: Optional[str] = None

# Load all D&D 5e feats from dnd_feats.json into the FEATS list at startup
with open(path.join(path.dirname(__file__), "dnd_feats.json"), "r") as f:
    FEATS = [Feat(**feat) for feat in load(f)]

RACES_FILE = path.join(path.dirname(__file__), "dnd_races.json")
with open(RACES_FILE, "r") as f:
    RACE_DATA = load(f)
RACES = list(RACE_DATA.keys())
CLASSES = [
    "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
]

def roll_ability_score() -> int:
    rolls = sorted([randint(1, 6) for _ in range(4)], reverse=True)
    return sum(rolls[:3])

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello"}


# About page route
@app.get("/about")
def about() -> dict[str, str]:
    return {"message": "This is the about page."}


# Route to add a message
@app.post("/messages/{msg_name}/")
def add_msg(msg_name: str) -> dict[str, MsgPayload]:
    # Generate an ID for the item based on the highest ID in the messages_list
    msg_id = max(messages_list.keys()) + 1 if messages_list else 0
    messages_list[msg_id] = MsgPayload(msg_id=msg_id, msg_name=msg_name)

    return {"message": messages_list[msg_id]}


# Route to list all messages
@app.get("/messages")
def message_items() -> dict[str, dict[int, MsgPayload]]:
    return {"messages:": messages_list}


# --- User Administration Routes ---
@app.post("/admin/users/", response_model=User)
def create_user(user: User):
    if users_collection.find_one({"id": user.id}):
        raise HTTPException(status_code=400, detail="User already exists")
    users_collection.insert_one(user.dict())
    return user


@app.get("/admin/users/", response_model=list[User])
def list_users():
    return [User(**u) for u in users_collection.find({}, {"_id": 0})]


@app.get("/admin/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = users_collection.find_one({"id": user_id}, {"_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)


@app.put("/admin/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    result = users_collection.update_one({"id": user_id}, {"$set": user.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/admin/users/{user_id}")
def delete_user(user_id: int):
    result = users_collection.delete_one({"id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}


@app.get("/admin/users/by-username/{username}", response_model=User)
def get_user_by_username(username: str):
    user = users_collection.find_one({"username": username}, {"_id": 0})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(**user)

def apply_racial_bonuses(race: str, stats: dict, other_stats: Optional[list[str]] = None) -> tuple[dict, dict]:
    bonuses = {k: 0 for k in stats}
    final_stats = stats.copy()
    race_bonuses = RACE_DATA[race]["bonuses"]
    # Generic handling for 'other' keys in bonuses
    if "other" in race_bonuses:
        n = race_bonuses["other"]
        exclude = [k for k in race_bonuses if k != "other"]
        available = [k for k in stats if k not in exclude]
        chosen = other_stats if other_stats is not None else sample(available, k=n)
        for k in chosen:
            final_stats[k] += 1
            bonuses[k] += 1
    for k, v in race_bonuses.items():
        if k != "other" and k in final_stats:
            final_stats[k] += v
            bonuses[k] += v
    return final_stats, bonuses

@app.post("/dnd5e/character", response_model=DnDCharacter)
def generate_dnd_character(name: str = "Adventurer", other_stats: Optional[list[str]] = None):
    race = choice(RACES)
    base_stats = {
        "strength": roll_ability_score(),
        "dexterity": roll_ability_score(),
        "constitution": roll_ability_score(),
        "intelligence": roll_ability_score(),
        "wisdom": roll_ability_score(),
        "charisma": roll_ability_score()
    }
    final_stats, bonuses = apply_racial_bonuses(race, base_stats, other_stats)
    character = DnDCharacter(
        name=name,
        race=race,
        character_class=choice(CLASSES),
        base_abilities=base_stats,
        final_abilities=final_stats,
        racial_bonus=bonuses,
        racial_features=RACE_DATA[race]["features"]
    )
    return character

# Global observer instance
feat_observer = FeatObserver()

# Dynamically load all feat plugin classes from plugins/
load_feat_plugins(feat_observer)

def apply_feats_to_attack(attacker_feats: list[Feat], base_attack_bonus: int, base_damage: int, context: Optional[dict] = None) -> tuple[int, int, list[str], str]:
    result = {"attack_bonus": 0, "damage": base_damage, "applied_feats": [], "notes": []}
    print(f"DEBUG: feats={attacker_feats}, context={context}")
    if context is None:
        context = {"base_attack_bonus": base_attack_bonus, "base_damage": base_damage}
    feat_names = [f.name for f in attacker_feats]
    feat_observer.notify(feat_names, context, result)
    attack_bonus = base_attack_bonus + result["attack_bonus"]
    damage = result["damage"]
    applied = result["applied_feats"]
    notes = "; ".join(result["notes"])
    return attack_bonus, damage, applied, notes

@app.post("/dnd5e/combat", response_model=CombatResult)
def combat(
    attacker: str,
    defender: str,
    attacker_feats: Optional[List[str]] = None,
    context: Optional[Dict[str, Any]] = Body(default=None)
):
    feats = [f for f in FEATS if attacker_feats and f.name in attacker_feats]
    base_attack_bonus = randint(1, 20)
    base_damage = randint(1, 8)
    # Use provided context or default
    feat_context = {"base_attack_bonus": base_attack_bonus, "base_damage": base_damage}
    if context:
        feat_context.update(context)
    attack_bonus, damage, applied, notes = apply_feats_to_attack(feats, base_attack_bonus, base_damage, feat_context)
    attack_roll = base_attack_bonus + attack_bonus
    hit = attack_roll >= 12  # Arbitrary AC for demo
    return CombatResult(
        attacker=attacker,
        defender=defender,
        attack_roll=attack_roll,
        hit=hit,
        damage=damage if hit else 0,
        applied_feats=applied,
        notes=notes
    )
