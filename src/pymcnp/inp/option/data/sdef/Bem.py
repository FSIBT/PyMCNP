import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Bem(Sdef):
    """
    Represents bem sdef data options.

    Attributes:
        keyword: bap sdef data option ``r'BEM'`` symbol.
        equals: bap sdef data option ``equals`` parameter.
        exn: bap sdef data option ``exn`` parameter.
        eyn: bap sdef data option ``eyn`` parameter.
        u: bap sdef data option ``u`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BEM'] = abc.Terminal[r'BEM']('BEM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    exn: literal.Real
    eyn: literal.Real
    bml: literal.Real | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
