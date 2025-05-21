# Plugin for the Spell Sniper feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class SpellSniperFeatPlugin(FeatPluginBase):
    """Plugin for the Spell Sniper feat."""
    name = "Spell Sniper"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Spell Sniper: double spell range, ignore cover for ranged spell attacks")
