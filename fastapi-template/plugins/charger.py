from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ChargerFeatPlugin(FeatPluginBase):
    """Plugin for the Charger feat."""
    name = "Charger"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("used_dash", False):
            result["damage"] = result.get("damage", 0) + 5
            result.setdefault("applied_feats", []).append("Charger (+5 damage after Dash)")
        result.setdefault("notes", []).append("Charger: Bonus damage after Dash if used_dash=True")
