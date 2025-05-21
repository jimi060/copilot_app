from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class MartialAdeptFeatPlugin(FeatPluginBase):
    """Plugin for the Martial Adept feat."""
    name = "Martial Adept"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Martial Adept: Learn 2 maneuvers (not applied in this demo)")
