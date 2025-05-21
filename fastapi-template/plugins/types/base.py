from typing import Dict, Any

class FeatPluginBase:
    """Base class for all feat plugins."""
    name: str

    @classmethod
    def apply(cls, context: Dict[str, Any], result: Dict[str, Any]) -> None:
        raise NotImplementedError
