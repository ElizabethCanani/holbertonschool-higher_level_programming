#!/usr/bin/python3

import sys
from typing import Any, Callable, Tuple


def safe_function(fct: Callable[..., Any], *args: Tuple[Any]) -> Any:
    """Executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
