import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Tmesh(Fmesh):
    """
    Represents tmesh fmesh data options.

    Attributes:
        keyword: tmesh fmesh data option `TMESH` symbol.
        equals: tmesh fmesh data option `=` symbol.
        t: tmesh fmesh data option `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TMESH'] | str = abc.Terminal[r'TMESH']('TMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
