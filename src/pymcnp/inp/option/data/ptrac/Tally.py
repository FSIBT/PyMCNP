import typing


from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Tally(Ptrac):
    """
    Represents tally ptrac data options.

    Attributes:
        keyword: tally ptrac data option ``r'TALLY'`` symbol.
        equals: tally ptrac data option ``r'='`` symbol.
        value: tally ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TALLY'] = abc.Terminal[r'TALLY']('TALLY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
