from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class DurableFeatPlugin(FeatPluginBase):
    """Plugin for the Durable feat."""
    name = "Durable"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Durable: Minimum HP from Hit Die = 2x CON mod (not applied in this demo)")
