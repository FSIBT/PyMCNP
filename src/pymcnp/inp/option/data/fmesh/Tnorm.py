import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh


class Tnorm(Fmesh):
    """
    Represents tnorm fmesh data options.

    Attributes:
        keyword: tnorm fmesh data option `TNORM` symbol.
        equals: tnorm fmesh data option `=` symbol.
        value: tnorm fmesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TNORM'] | str = abc.Terminal[r'TNORM']('TNORM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
