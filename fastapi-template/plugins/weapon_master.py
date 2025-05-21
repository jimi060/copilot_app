# Plugin for the Weapon Master feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class WeaponMasterFeatPlugin(FeatPluginBase):
    """Plugin for the Weapon Master feat."""
    name = "Weapon Master"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Weapon Master: proficiency with four weapons of your choice")
