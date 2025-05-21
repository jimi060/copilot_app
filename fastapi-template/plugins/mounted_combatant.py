# Plugin for the Mounted Combatant feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class MountedCombatantFeatPlugin(FeatPluginBase):
    """Plugin for the Mounted Combatant feat."""
    name = "Mounted Combatant"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("is_mounted", False):
            result.setdefault("notes", []).append("Mounted Combatant: Advantage on melee vs unmounted targets")
