import typing
import decimal
import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Jmesh(Mesh):
    """
    Represents jmesh mesh data options.

    Attributes:
        keyword: jmesh mesh data option ``r'JMESH'`` symbol.
        equals: jmesh mesh data option ``r'='`` symbol.
        y: jmesh mesh data option ``y`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'JMESH'] | str = abc.Terminal[r'JMESH']('JMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    y: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
