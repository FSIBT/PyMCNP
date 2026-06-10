import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Dir(Sdef):
    """
    Represents dir sdef data options.

    Attributes:
        keyword: dir sdef data option `DIR` symbol.
        equals: dir sdef data option `equals` parameter.
        u: dir sdef data option `u` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DIR'] | str = abc.Terminal[r'DIR']('DIR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    u: literal.Real | literal.DependentDistribution | literal.EmbeddedDistribution | int | float | decimal.Decimal | str
