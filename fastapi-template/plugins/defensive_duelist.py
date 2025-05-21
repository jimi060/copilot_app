from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class DefensiveDuelistFeatPlugin(FeatPluginBase):
    """Plugin for the Defensive Duelist feat."""
    name = "Defensive Duelist"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Defensive Duelist: Can add proficiency to AC as reaction (not applied in this demo)")
