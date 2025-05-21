# Plugin for the War Caster feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class WarCasterFeatPlugin(FeatPluginBase):
    """Plugin for the War Caster feat."""
    name = "War Caster"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("War Caster: advantage on concentration saves")
