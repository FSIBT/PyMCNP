import re

from ..Literal import Literal


class Distribution(Literal):
    """
    Represents distribution literals.
    """

    _pattern = re.compile(r'(D\d+|[-+]?(?:\d*\.\d+|\d+\.?|\d+)(?:[eE][-+]?\d+)?)([\s\S]*)', re.IGNORECASE)
