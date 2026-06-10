import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Ara(Sdef):
    """
    Represents ara sdef data options.

    Attributes:
        keyword: ara sdef data option `ARA` symbol.
        equals: ara sdef data option `=` symbol.
        x: ara sdef data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ARA'] | str = abc.Terminal[r'ARA']('ARA')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
