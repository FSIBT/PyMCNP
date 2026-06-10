import typing
import dataclasses

from ..... import abc
from ..Embed import Embed


class Elementchk(Embed):
    """
    Represents elementchk embed data options.

    Attributes:
        keyword: elementchk embed data option `ELEMENTCHK` symbol.
        equals: elementchk embed data option `=` symbol.
        value: elementchk embed data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ELEMENTCHK'] | str = abc.Terminal[r'ELEMENTCHK']('ELEMENTCHK')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
