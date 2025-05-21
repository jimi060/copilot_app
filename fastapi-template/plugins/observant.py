# Plugin for the Observant feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ObservantFeatPlugin(FeatPluginBase):
    """Plugin for the Observant feat."""
    name = "Observant"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Observant: +1 Int/Wis, read lips (not applied in this demo)")
