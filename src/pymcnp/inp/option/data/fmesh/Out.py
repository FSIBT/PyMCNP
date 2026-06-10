import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh


class Out(Fmesh):
    """
    Represents out fmesh data options.

    Attributes:
        keyword: out fmesh data option `OUT` symbol.
        equals: out fmesh data option `=` symbol.
        value: out fmesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'OUT'] | str = abc.Terminal[r'OUT']('OUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:COL|COLSCI|CF|CFSCI|IJ|IK|JK|NONE|XDMF)'] | str
