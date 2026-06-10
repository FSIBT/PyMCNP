import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh


class Geom(Fmesh):
    """
    Represents geom fmesh data options.

    Attributes:
        keyword: geom fmesh data option `GEOM` symbol.
        equals: geom fmesh data option `=` symbol.
        value: geom fmesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GEOM'] | str = abc.Terminal[r'GEOM']('GEOM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:XYZ|REC|RZT|CYL)'] | str
