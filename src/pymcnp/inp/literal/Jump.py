import re

from ..Literal import Literal


class Jump(Literal):
    """
    Represents jump literals.
    """

    _pattern = re.compile(r'(J)([\s\S]*)', re.IGNORECASE)
