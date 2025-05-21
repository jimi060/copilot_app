# Plugin for the Medium Armor Master feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class MediumArmorMasterFeatPlugin(FeatPluginBase):
    """Plugin for the Medium Armor Master feat."""
    name = "Medium Armor Master"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Medium Armor Master: No Stealth disadvantage, +3 max Dex bonus (not applied in this demo)")
