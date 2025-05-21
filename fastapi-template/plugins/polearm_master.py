# Plugin for the Polearm Master feat
from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class PolearmMasterFeatPlugin(FeatPluginBase):
    """Plugin for the Polearm Master feat."""
    name = "Polearm Master"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        if context.get("using_polearm", False):
            result["extra_attack"] = True
            result.setdefault("applied_feats", []).append("Polearm Master (bonus attack)")
        result.setdefault("notes", []).append("Polearm Master: Bonus attack if using_polearm=True")
