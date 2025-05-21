# Plugin for the Resilient feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ResilientFeatPlugin(FeatPluginBase):
    """Plugin for the Resilient feat."""
    name = "Resilient"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Resilient: +1 to ability, proficiency in saves (not applied in this demo)")
