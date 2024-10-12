import sys
from typing import Any, List, Optional

endl = object()


class Cout:
    """
    ```python
    from pycout import *

    cout << "Hello" << " World!" << endl
    ```
    """

    def __init__(self, line: str = "") -> None:
        self.line = line

    def __lshift__(self, other: Any) -> Optional["Cout"]:
        if other is endl:
            sys.stdout.write(self.line)
            sys.stdout.write("\n")
            sys.stdout.flush()
            return None
        return Cout(self.line + str(other))

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Cout) and self.line == other.line

    def __str__(self) -> str:
        return self.line


cout = Cout()
