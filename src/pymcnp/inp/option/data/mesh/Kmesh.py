import typing
import decimal
import collections
import dataclasses

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Kmesh(Mesh):
    """
    Represents kmesh mesh data options.

    Attributes:
        keyword: kmesh mesh data option `KMESH` symbol.
        equals: kmesh mesh data option `=` symbol.
        z: kmesh mesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KMESH'] | str = abc.Terminal[r'KMESH']('KMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
