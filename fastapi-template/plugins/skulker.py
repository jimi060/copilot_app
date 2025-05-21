# Plugin for the Skulker feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class SkulkerFeatPlugin(FeatPluginBase):
    """Plugin for the Skulker feat."""
    name = "Skulker"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Skulker: Can hide when lightly obscured (not applied in this demo)")
