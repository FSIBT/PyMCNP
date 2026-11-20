import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Wgt(Sdef):
    """
    Represents wgt sdef data options.

    Attributes:
        keyword: wgt sdef data option ``r'WGT'`` symbol.
        equals: wgt sdef data option ``equals`` parameter.
        x: wgt sdef data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WGT'] = abc.Terminal[r'WGT']('WGT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
