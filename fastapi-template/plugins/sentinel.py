from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class SentinelFeatPlugin(FeatPluginBase):
    """Plugin for the Sentinel feat."""
    name = "Sentinel"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("opportunity_attack", False):
            result.setdefault("notes", []).append("Sentinel: Target speed 0 on hit")
