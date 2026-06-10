import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Emesh(Fmesh):
    """
    Represents emesh fmesh data options.

    Attributes:
        keyword: emesh fmesh data option `EMESH` symbol.
        equals: emesh fmesh data option `=` symbol.
        e: emesh fmesh data option `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EMESH'] | str = abc.Terminal[r'EMESH']('EMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
