import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Bap(Sdef):
    """
    Represents bap sdef data options.

    Attributes:
        keyword: bap sdef data option ``r'BAP'`` symbol.
        equals: bap sdef data option ``equals`` parameter.
        ba1: bap sdef data option ``ba1`` parameter.
        ba2: bap sdef data option ``ba2`` parameter.
        u: bap sdef data option ``u`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BAP'] = abc.Terminal[r'BAP']('BAP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    ba1: literal.Real
    ba2: literal.Real
    u: literal.Real | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
