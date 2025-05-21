from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class CrossbowExpertFeatPlugin(FeatPluginBase):
    """Plugin for the Crossbow Expert feat."""
    name = "Crossbow Expert"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Crossbow Expert: Ignore loading on crossbows, no disadvantage in melee (not applied in this demo)")
