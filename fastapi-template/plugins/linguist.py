from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class LinguistFeatPlugin(FeatPluginBase):
    """Plugin for the Linguist feat."""
    name = "Linguist"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append(
            "Linguist: Learn 3 languages, create ciphers (not applied in this demo)"
        )
