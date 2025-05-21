# Plugin for the Moderately Armored feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ModeratelyArmoredFeatPlugin(FeatPluginBase):
    """Plugin for the Moderately Armored feat."""
    name = "Moderately Armored"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Moderately Armored: Gain medium armor/shield proficiency (not applied in this demo)")
