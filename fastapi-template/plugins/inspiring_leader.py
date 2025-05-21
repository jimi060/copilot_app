from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class InspiringLeaderFeatPlugin(FeatPluginBase):
    """Plugin for the Inspiring Leader feat."""
    name = "Inspiring Leader"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Inspiring Leader: Grant temp HP after speech (not applied in this demo)")
