from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class DualWielderFeatPlugin(FeatPluginBase):
    """Plugin for the Dual Wielder feat."""
    name = "Dual Wielder"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Dual Wielder: +1 AC when dual wielding")
