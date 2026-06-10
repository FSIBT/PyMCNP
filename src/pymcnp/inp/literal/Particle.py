import re

from ..Literal import Literal


class Particle(Literal):
    """
    Represents particle literals.
    """

    _pattern = re.compile(
        r'([-NPE|QUV[HL+XYO!<>G/ZKB_~CW@DTSA*?#](?:,[-NPE|QUV[HL+XYO!<>G/ZKB_~CW@DTSA*?#])*)([\s\S]*)',
        re.IGNORECASE,
    )
