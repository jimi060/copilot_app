from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class HealerFeatPlugin(FeatPluginBase):
    """Plugin for the Healer feat."""
    name = "Healer"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Healer: Use healer's kit to stabilize/restore HP (not applied in this demo)")
