import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Ref(Mesh):
    """
    Represents ref mesh data options.

    Attributes:
        keyword: ref mesh data option `REF` symbol.
        equals: ref mesh data option `=` symbol.
        x: ref mesh data option `x` parameter.
        y: ref mesh data option `y` parameter.
        z: ref mesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'REF'] | str = abc.Terminal[r'REF']('REF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
