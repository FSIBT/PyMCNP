import typing
import decimal
import collections
import dataclasses

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Cos(Ksen):
    """
    Represents cos ksen data options.

    Attributes:
        keyword: cos ksen data option `COS` symbol.
        equals: cos ksen data option `=` symbol.
        angles: cos ksen data option `angles` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'COS'] | str = abc.Terminal[r'COS']('COS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    angles: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[
        r''
    ]('')
