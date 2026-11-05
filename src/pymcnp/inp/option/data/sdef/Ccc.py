import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Ccc(Sdef):
    """
    Represents ccc sdef data options.

    Attributes:
        keyword: ccc sdef data option ``r'CCC'`` symbol.
        equals: ccc sdef data option ``equals`` parameter.
        x: ccc sdef data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CCC'] | str = abc.Terminal[r'CCC']('CCC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Integer | literal.Distribution | literal.DependentDistribution | int | str
