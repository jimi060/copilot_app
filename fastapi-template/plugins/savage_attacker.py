# Plugin for the Savage Attacker feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class SavageAttackerFeatPlugin(FeatPluginBase):
    """Plugin for the Savage Attacker feat."""
    name = "Savage Attacker"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("melee_attack", False):
            result.setdefault("notes", []).append("Savage Attacker: Can reroll melee damage (not applied in this demo)")
