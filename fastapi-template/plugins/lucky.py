from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class LuckyFeatPlugin(FeatPluginBase):
    """Plugin for the Lucky feat."""
    name = "Lucky"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Lucky: Can reroll d20 (not applied in this demo)")
