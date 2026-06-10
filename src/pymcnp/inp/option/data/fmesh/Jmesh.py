import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Jmesh(Fmesh):
    """
    Represents jmesh fmesh data options.

    Attributes:
        keyword: jmesh fmesh data option `JMESH` symbol.
        equals: jmesh fmesh data option `=` symbol.
        y: jmesh fmesh data option `y` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'JMESH'] | str = abc.Terminal[r'JMESH']('JMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    y: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
