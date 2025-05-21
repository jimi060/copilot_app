from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class AlertFeatPlugin(FeatPluginBase):
    """Plugin for the Alert feat."""
    name = "Alert"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Alert: +5 to initiative, can't be surprised (not applied in this demo)")
