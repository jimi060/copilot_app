from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ElementalAdeptFeatPlugin(FeatPluginBase):
    """Plugin for the Elemental Adept feat."""
    name = "Elemental Adept"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Elemental Adept: Ignore resistance to chosen element (not applied in this demo)")
