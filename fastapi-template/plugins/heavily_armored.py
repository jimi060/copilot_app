from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class HeavilyArmoredFeatPlugin(FeatPluginBase):
    """Plugin for the Heavily Armored feat."""
    name = "Heavily Armored"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Heavily Armored: Gain heavy armor proficiency (not applied in this demo)")
