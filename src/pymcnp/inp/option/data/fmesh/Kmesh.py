import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Kmesh(Fmesh):
    """
    Represents kmesh fmesh data options.

    Attributes:
        keyword: kmesh fmesh data option `KMESH` symbol.
        equals: kmesh fmesh data option `=` symbol.
        z: kmesh fmesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KMESH'] | str = abc.Terminal[r'KMESH']('KMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
