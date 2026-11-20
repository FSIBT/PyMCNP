import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Eff(Sdef):
    """
    Represents eff sdef data options.

    Attributes:
        keyword: eff sdef data option ``r'EFF'`` symbol.
        equals: eff sdef data option ``equals`` parameter.
        x: eff sdef data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EFF'] = abc.Terminal[r'EFF']('EFF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
