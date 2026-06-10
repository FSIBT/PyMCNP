import typing
import dataclasses

from ..... import abc
from ..Mesh import Mesh


class Geom(Mesh):
    """
    Represents geom mesh data options.

    Attributes:
        keyword: geom mesh data option `GEOM` symbol.
        equals: geom mesh data option `=` symbol.
        value: geom mesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GEOM'] | str = abc.Terminal[r'GEOM']('GEOM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:XYZ|REC|RZT|CYL|RPT|SPH)'] | str
