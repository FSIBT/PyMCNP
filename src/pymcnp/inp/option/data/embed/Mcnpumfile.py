import typing
import dataclasses

from ..... import abc
from ..Embed import Embed


class Mcnpumfile(Embed):
    """
    Represents mcnpumfile embed data options.

    Attributes:
        keyword: mcnpumfile embed data option `MCNPUMFILE` symbol.
        equals: mcnpumfile embed data option `=` symbol.
        filename: mcnpumfile embed data option `filename` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MCNPUMFILE'] | str = abc.Terminal[r'MCNPUMFILE']('MCNPUMFILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str
