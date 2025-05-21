# Plugin for the Skilled feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class SkilledFeatPlugin(FeatPluginBase):
    """Plugin for the Skilled feat."""
    name = "Skilled"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Skilled: Gain 3 skills/tools (not applied in this demo)")
