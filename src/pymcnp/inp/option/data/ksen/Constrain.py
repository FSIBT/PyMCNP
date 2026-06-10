import typing
import dataclasses

from ..... import abc
from ..Ksen import Ksen


class Constrain(Ksen):
    """
    Represents constrain ksen data options.

    Attributes:
        keyword: constrain ksen data option `CONSTRAIN` symbol.
        equals: constrain ksen data option `=` symbol.
        value: constrain ksen data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CONSTRAIN'] | str = abc.Terminal[r'CONSTRAIN']('CONSTRAIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:NO|YES)'] | str
