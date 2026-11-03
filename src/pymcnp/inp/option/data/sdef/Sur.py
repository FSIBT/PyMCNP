import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Sur(Sdef):
    """
    Represents sur sdef data options.

    Attributes:
        keyword: sur sdef data option `SUR` symbol.
        equals: sur sdef data option `equals` parameter.
        s: sur sdef data option `s` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SUR'] | str = abc.Terminal[r'SUR']('SUR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: literal.Integer | literal.Distribution | literal.DependentDistribution | int | str
