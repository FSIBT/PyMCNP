import typing
import dataclasses

from ..... import abc
from ..Act import Act


class Dg(Act):
    """
    Represents dg act data options.

    Attributes:
        keyword: dg act data option `DG` symbol.
        equals: dg act data option `=` symbol.
        value: dg act data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DG'] | str = abc.Terminal[r'DG']('DG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:LINES|MG|NONE)'] | str
