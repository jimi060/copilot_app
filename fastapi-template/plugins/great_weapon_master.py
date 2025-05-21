from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class GreatWeaponMasterFeatPlugin(FeatPluginBase):
    """Plugin for the Great Weapon Master feat."""
    name = "Great Weapon Master"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("crit", False) or context.get("reduced_to_0", False):
            result["extra_attack"] = True
            result.setdefault("applied_feats", []).append("Great Weapon Master (bonus attack)")
        result.setdefault("notes", []).append("Great Weapon Master: Bonus attack on crit/kill (not applied in this demo)")
