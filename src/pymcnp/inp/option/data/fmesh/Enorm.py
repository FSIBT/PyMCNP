import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh


class Enorm(Fmesh):
    """
    Represents enorm fmesh data options.

    Attributes:
        keyword: enorm fmesh data option `ENORM` symbol.
        equals: enorm fmesh data option `=` symbol.
        value: enorm fmesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ENORM'] | str = abc.Terminal[r'ENORM']('ENORM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
