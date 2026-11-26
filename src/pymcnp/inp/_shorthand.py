import re

import numpy


_NUMBER = r'[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?'
# An `xM` entry whose own previous entry is still a shorthand is not a value yet, so `nR`, `nI` and `nLOG` wait for it.
_REGEX_REPEAT = re.compile(r'(\S+)(?<!\d[mM]) (\d+)R', re.IGNORECASE)
_REGEX_INSERT = re.compile(r'(\S+)(?<!\d[mM]) (\d+)I (\S+)', re.IGNORECASE)
_REGEX_JUMP = re.compile(r'(?<!\S)(\d+)(J)(?!\S)', re.IGNORECASE)
_REGEX_LOG = re.compile(r'(\S+)(?<!\d[mM]) (\d+)I?LOG (\S+)', re.IGNORECASE)
_REGEX_MULTIPLY = re.compile(rf'(?<!\S)({_NUMBER}) ({_NUMBER})M(?!\S)', re.IGNORECASE)
_REGEX_COMMENT = re.compile(r' {0,4}c(?:\s|\Z)', re.IGNORECASE)


def _expand(code: str) -> str:
    """
    Expands the horizontal data format shorthands (``nR``, ``nI``, ``nJ``, ``nLOG``, ``xM``) of one line of card text.

    ``xM`` is the previous entry times ``x``. Its previous entry may itself come from a shorthand, e.g., ``1 2R 2M``, so
    the shorthands are expanded until none is left.

    Parameters:
        code: Card text, without a ``$`` comment.

    Returns:
        ``code`` with its shorthands written out.
    """

    previous = None
    while code != previous:
        previous = code
        while (multiplied := _REGEX_MULTIPLY.sub(lambda match: f'{match[1]} {float(match[1]) * float(match[2])}', code, count=1)) != code:
            code = multiplied
        code = _REGEX_REPEAT.sub(lambda match: f'{match[1]} {" ".join([match[1]] * int(match[2]))}', code)
        code = _REGEX_INSERT.sub(lambda match: ' '.join(map(str, numpy.linspace(float(match[1]), float(match[3]), num=int(match[2]) + 2))), code)
        code = _REGEX_JUMP.sub(lambda match: ' '.join([match[2]] * int(match[1])), code)
        code = _REGEX_LOG.sub(lambda match: ' '.join(map(str, numpy.geomspace(float(match[1]), float(match[3]), num=int(match[2]) + 2))), code)

    return code


def _expand_line(line: str) -> str:
    """
    Expands the horizontal data format shorthands of one line of an input file.

    Comment cards and ``$`` comments are left verbatim.

    Parameters:
        line: Line of card text.

    Returns:
        ``line`` with the shorthands of its card text written out.
    """

    if not line or _REGEX_COMMENT.match(line):
        return line

    code, dollar, comment = line.partition('$')
    return _expand(code) + dollar + comment


def _expand_card(source: str) -> str:
    """
    Expands the horizontal data format shorthands of one card, as ``Inp`` does for each card of a file.

    Parameters:
        source: Card text, possibly over several lines.

    Returns:
        ``source`` with the shorthands of its card text written out.
    """

    return '\n'.join(_expand_line(line) for line in source.split('\n'))
