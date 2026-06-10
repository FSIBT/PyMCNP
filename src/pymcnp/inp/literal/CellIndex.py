import re

from ..Literal import Literal


class CellIndex(Literal):
    """
    Represents cellindex literals.

    Attributes:
        left: cellindex literal `left` parameter.
        operator: cellindex literal `<` symbol.
        right: cellindex literal `right` parameter.
    """

    _pattern = re.compile(
        r'((?:(?:(?:\d+(?:\s+\d+)*)\s*\[\s*(?:(?:U\s*=\s*\d+)|(?:(?:(?:\d+\s*:\s*\d+)|\d+)(?:\s+(?:(?:\d+\s*:\s*\d+)|\d+))*))\s*\]\s*)|(?:\d+(?:\s+\d+)*)|(?:D\d+))(?:\s*<\s*(?:(?:(?:(?:\d+(?:\s+\d+)*)\s*\[\s*(?:(?:U\s*=\s*\d+)|(?:(?:(?:\d+\s*:\s*\d+)|\d+)(?:\s+(?:(?:\d+\s*:\s*\d+)|\d+))*))\s*\]\s*)|(?:\d+(?:\s+\d+)*)|(?:D\d+))))*)([\s\S]*)',
        re.IGNORECASE,
    )
