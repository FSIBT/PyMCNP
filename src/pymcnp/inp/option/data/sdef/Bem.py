import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Bem(Sdef):
    """
    Represents bem sdef data options.

    Attributes:
        keyword: bap sdef data option `BEM` symbol.
        equals: bap sdef data option `equals` parameter.
        exn: bap sdef data option `exn` parameter.
        eyn: bap sdef data option `eyn` parameter.
        u: bap sdef data option `u` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BEM'] | str = abc.Terminal[r'BEM']('BEM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    exn: literal.Real | int | float | decimal.Decimal | str
    eyn: literal.Real | int | float | decimal.Decimal | str
    bml: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')
