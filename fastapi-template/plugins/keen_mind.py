from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class KeenMindFeatPlugin(FeatPluginBase):
    """Plugin for the Keen Mind feat."""
    name = "Keen Mind"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Keen Mind: Always know which way is north, etc. (not applied in this demo)")
