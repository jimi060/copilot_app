from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class MagicInitiateFeatPlugin(FeatPluginBase):
    """Plugin for the Magic Initiate feat."""
    name = "Magic Initiate"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Magic Initiate: Learn 2 cantrips, 1 spell (not applied in this demo)")
