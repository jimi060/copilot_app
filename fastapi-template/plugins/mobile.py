# Plugin for the Mobile feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class MobileFeatPlugin(FeatPluginBase):
    """Plugin for the Mobile feat."""
    name = "Mobile"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Mobile: +10 speed, ignore difficult terrain on Dash (not applied in this demo)")
