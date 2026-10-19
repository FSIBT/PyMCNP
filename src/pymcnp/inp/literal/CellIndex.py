import re

from ..Literal import Literal


class CellIndex(Literal):
    """
    Represents cell index literals.
    """

    _pattern = re.compile(
        r'((?:(?:(?:\d+(?:\s+\d+)*)\s*\[\s*(?:(?:U\s*=\s*\d+)|(?:(?:(?:\d+\s*:\s*\d+)|\d+)(?:\s+(?:(?:\d+\s*:\s*\d+)|\d+))*))\s*\]\s*)|(?:\d+(?:\s+\d+)*)|(?:D\d+))(?:\s*<\s*(?:(?:(?:(?:\d+(?:\s+\d+)*)\s*\[\s*(?:(?:U\s*=\s*\d+)|(?:(?:(?:\d+\s*:\s*\d+)|\d+)(?:\s+(?:(?:\d+\s*:\s*\d+)|\d+))*))\s*\]\s*)|(?:\d+(?:\s+\d+)*)|(?:D\d+))))*)([\s\S]*)',
        re.IGNORECASE,
    )
