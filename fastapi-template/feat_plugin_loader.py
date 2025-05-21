# This file will dynamically load all feat plugin hooks from the plugins/ directory
from os import listdir, path
from importlib.util import spec_from_file_location, module_from_spec
from plugins.types.feat_observer import FeatObserver

PLUGIN_DIR = path.join(path.dirname(__file__), "plugins")

def load_feat_plugins(observer: FeatObserver):
    for filename in listdir(PLUGIN_DIR):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            file_path = path.join(PLUGIN_DIR, filename)
            spec = spec_from_file_location(module_name, file_path)
            if spec and spec.loader:
                module = module_from_spec(spec)
                spec.loader.exec_module(module)
                class_name = module_name.capitalize() + "FeatPlugin"
                if hasattr(module, class_name):
                    plugin_class = getattr(module, class_name)
                    observer.register(plugin_class)
