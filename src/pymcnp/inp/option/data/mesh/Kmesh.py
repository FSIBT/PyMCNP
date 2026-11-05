import typing
import decimal
import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Kmesh(Mesh):
    """
    Represents kmesh mesh data options.

    Attributes:
        keyword: kmesh mesh data option ``r'KMESH'`` symbol.
        equals: kmesh mesh data option ``r'='`` symbol.
        z: kmesh mesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KMESH'] | str = abc.Terminal[r'KMESH']('KMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
