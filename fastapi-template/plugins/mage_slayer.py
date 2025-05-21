from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class MageSlayerFeatPlugin(FeatPluginBase):
    """Plugin for the Mage Slayer feat."""
    name = "Mage Slayer"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("enemy_casting", False):
            result["extra_attack"] = True
            result.setdefault("applied_feats", []).append("Mage Slayer (attack as reaction)")
        result.setdefault("notes", []).append("Mage Slayer: Attack as reaction if enemy_casting=True")
