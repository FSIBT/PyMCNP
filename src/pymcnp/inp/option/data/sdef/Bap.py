import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Bap(Sdef):
    """
    Represents bap sdef data options.

    Attributes:
        keyword: bap sdef data option `BAP` symbol.
        equals: bap sdef data option `equals` parameter.
        ba1: bap sdef data option `ba1` parameter.
        ba2: bap sdef data option `ba2` parameter.
        u: bap sdef data option `u` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'BAP'] | str = abc.Terminal[r'BAP']('BAP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    ba1: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ba2: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    u: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')
