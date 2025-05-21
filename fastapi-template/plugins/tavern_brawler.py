# Plugin for the Tavern Brawler feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class TavernBrawlerFeatPlugin(FeatPluginBase):
    """Plugin for the Tavern Brawler feat."""
    name = "Tavern Brawler"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Tavern Brawler: proficiency with improvised weapons, unarmed strike uses d4")
