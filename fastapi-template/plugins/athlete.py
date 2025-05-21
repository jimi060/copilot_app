from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class AthleteFeatPlugin(FeatPluginBase):
    """Plugin for the Athlete feat."""
    name = "Athlete"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result["attack_bonus"] = result.get("attack_bonus", 0) + 1
        result.setdefault("applied_feats", []).append("Athlete (+1 attack bonus)")
        result.setdefault("notes", []).append("Athlete: Climbing/jumping improved (not applied in this demo)")
