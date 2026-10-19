import re

from ..Literal import Literal


class EmbeddedDistribution(Literal):
    """
    Represents embeddeddistribution literals.
    """

    _pattern = re.compile(r'(D\d+(?:\s*<\s*D\d+)*)([\s\S]*)', re.IGNORECASE)
