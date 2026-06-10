import typing
import decimal
import collections
import dataclasses

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Ein(Ksen):
    """
    Represents ein ksen data options.

    Attributes:
        keyword: ein ksen data option `EIN` symbol.
        equals: ein ksen data option `=` symbol.
        e: ein ksen data option `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EIN'] | str = abc.Terminal[r'EIN']('EIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
