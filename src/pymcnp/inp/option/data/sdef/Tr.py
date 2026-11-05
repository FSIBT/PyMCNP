import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Tr(Sdef):
    """
    Represents tr sdef data options.

    Attributes:
        keyword: tr sdef data option ``r'TR'`` symbol.
        equals: tr sdef data option ``equals`` parameter.
        n: tr sdef data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TR'] | str = abc.Terminal[r'TR']('TR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | literal.Distribution | int | str
