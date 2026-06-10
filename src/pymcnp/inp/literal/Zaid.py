import re

from ..Literal import Literal


class Zaid(Literal):
    """
    Represents zaid literals.
    """

    _pattern = re.compile(r'((?:(?:[a-z]+)|(?:(?:(?:\d{4,6})|(?:[a-z]{1,2}-?\d*))(?:m\d+)?))(?:\.\d{2,}[a-z]*)?)([\s\S]*)', re.IGNORECASE)
