"""
Reads the panels that ``pymcnp`` prints, whichever box ``rich`` draws.
"""

import re

# A border line: rich's box-drawing characters (round corners, or square ones on legacy Windows
# consoles) or, for an output encoding without them, ASCII.
_BORDER = re.compile(r'[+\-─-╿]+')


def plain(output: str) -> str:
    """
    Text of the panels in ``output``, without borders and line breaks, words separated by single spaces.
    """

    lines = (line.strip() for line in output.splitlines())
    return ' '.join(' '.join(line.strip('|│') for line in lines if not _BORDER.fullmatch(line)).split())
