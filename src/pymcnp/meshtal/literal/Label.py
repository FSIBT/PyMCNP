import re

from ..Literal import Literal


class Label(Literal):
    """
    Represents label literals.
    """

    _pattern = re.compile(
        r'(Energy|Time|X|Y|Z|Result|Rel Error)',
        re.IGNORECASE,
    )
