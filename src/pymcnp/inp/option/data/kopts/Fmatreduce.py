import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Fmatreduce(Kopts):
    """
    Represents fmatreduce kopts data options.

    Attributes:
        keyword: fmatreduce kopts data option `FMATREDUCE` symbol.
        equals: fmatreduce kopts data option `=` symbol.
        value: fmatreduce kopts data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATREDUCE'] | str = abc.Terminal[r'FMATREDUCE']('FMATREDUCE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
