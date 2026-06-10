import typing
import decimal
import collections
import dataclasses

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Jmesh(Mesh):
    """
    Represents jmesh mesh data options.

    Attributes:
        keyword: jmesh mesh data option `JMESH` symbol.
        equals: jmesh mesh data option `=` symbol.
        y: jmesh mesh data option `y` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'JMESH'] | str = abc.Terminal[r'JMESH']('JMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    y: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
