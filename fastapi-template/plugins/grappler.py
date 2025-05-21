from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class GrapplerFeatPlugin(FeatPluginBase):
    """Plugin for the Grappler feat."""
    name = "Grappler"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("is_grappling", False):
            result.setdefault("notes", []).append("Grappler: Advantage on attack rolls vs grappled target")
