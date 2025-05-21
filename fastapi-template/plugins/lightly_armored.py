from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class LightlyArmoredFeatPlugin(FeatPluginBase):
    """Plugin for the Lightly Armored feat."""
    name = "Lightly Armored"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Lightly Armored: Gain light armor proficiency (not applied in this demo)")
