# Plugin for the Shield Master feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class ShieldMasterFeatPlugin(FeatPluginBase):
    """Plugin for the Shield Master feat."""
    name = "Shield Master"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("using_shield", False):
            result["extra_attack"] = True
            result.setdefault("applied_feats", []).append("Shield Master (shove as bonus action)")
        result.setdefault("notes", []).append("Shield Master: Shove as bonus action if using_shield=True")
