import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh


class Type(Fmesh):
    """
    Represents type fmesh data options.

    Attributes:
        keyword: type fmesh data option `TYPE` symbol.
        equals: type fmesh data option `=` symbol.
        type: type fmesh data option `type` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TYPE'] | str = abc.Terminal[r'TYPE']('TYPE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    type: typing.Annotated[abc.Terminal, r'(?:FLUX|SOURCE)'] | str
