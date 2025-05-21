from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class HeavyArmorMasterFeatPlugin(FeatPluginBase):
    """Plugin for the Heavy Armor Master feat."""
    name = "Heavy Armor Master"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("wearing_heavy_armor", False):
            result["damage"] = max(0, result.get("damage", 0) - 3)
            result.setdefault("applied_feats", []).append("Heavy Armor Master (-3 damage)")
        result.setdefault("notes", []).append("Heavy Armor Master: -3 damage if wearing_heavy_armor=True")
