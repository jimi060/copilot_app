from typing import Any, Dict, List

class FeatObserver:
    def __init__(self):
        self.plugins: Dict[str, Any] = {}  # Dict[str, FeatPluginBase subclass]

    def register(self, plugin_cls: Any) -> None:
        # Register plugin class by its name attribute
        self.plugins[plugin_cls.name] = plugin_cls

    def notify(self, feat_names: List[str], context: dict, result: dict) -> None:
        for name in feat_names:
            plugin_cls = self.plugins.get(name)
            if plugin_cls:
                plugin_cls.apply(context, result)
