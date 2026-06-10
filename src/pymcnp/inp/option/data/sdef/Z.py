import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Z(Sdef):
    """
    Represents z sdef data options.

    Attributes:
        keyword: z sdef data option `Z` symbol.
        equals: z sdef data option `equals` parameter.
        z: z sdef data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'Z'] | str = abc.Terminal[r'Z']('Z')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    z: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution | int | float | decimal.Decimal | str
