from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ActorFeatPlugin(FeatPluginBase):
    """Plugin for the Actor feat."""
    name = "Actor"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("impersonating", False):
            result.setdefault("advantage_checks", []).extend(["Deception", "Performance"])
            result.setdefault("notes", []).append("Actor: Advantage on Deception and Performance checks (impersonating)")
        else:
            result.setdefault("notes", []).append("Actor: Advantage on Deception/Performance (not applied in this demo)")
