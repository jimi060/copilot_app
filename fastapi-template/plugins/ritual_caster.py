# Plugin for the Ritual Caster feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class RitualCasterFeatPlugin(FeatPluginBase):
    """Plugin for the Ritual Caster feat."""
    name = "Ritual Caster"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Ritual Caster: Can cast rituals (not applied in this demo)")
