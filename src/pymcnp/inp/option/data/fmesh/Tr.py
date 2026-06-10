import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Tr(Fmesh):
    """
    Represents tr fmesh data options.

    Attributes:
        keyword: tr fmesh data option `TR` symbol.
        equals: tr fmesh data option `=` symbol.
        n: tr fmesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TR'] | str = abc.Terminal[r'TR']('TR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
