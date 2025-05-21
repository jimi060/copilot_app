# Plugin for the Tough feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ToughFeatPlugin(FeatPluginBase):
    """Plugin for the Tough feat."""
    name = "Tough"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Tough: HP max increases by 2 per level")
