from typing import Callable, Dict, Any

#: FeatHook is the type for a function that implements a feat's logic.
#: It takes a context dictionary (with combat or action info) and a result dictionary (to be mutated with feat effects).
FeatHook = Callable[[Dict[str, Any], Dict[str, Any]], None]

#: RegisterFeatFn is the type for the function used to register a feat hook with the observer system.
#: It takes the feat's name (str) and a FeatHook function, and registers the hook for use in the system.
RegisterFeatFn = Callable[[str, FeatHook], None]
