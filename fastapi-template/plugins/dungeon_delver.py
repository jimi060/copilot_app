from plugins.types.base import FeatPluginBase
from typing import Dict, Any

class DungeonDelverFeatPlugin(FeatPluginBase):
    """Plugin for the Dungeon Delver feat."""
    name = "Dungeon Delver"

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        result.setdefault("notes", []).append("Dungeon Delver: Advantage on Perception/Investigation for secret doors/traps (not applied in this demo)")
