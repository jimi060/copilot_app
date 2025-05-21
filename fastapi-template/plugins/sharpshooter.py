# Plugin for the Sharpshooter feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class SharpshooterFeatPlugin(FeatPluginBase):
    """Plugin for the Sharpshooter feat."""
    name = "Sharpshooter"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Sharpshooter: No disadvantage at long range, ignore cover (not applied in this demo)")
