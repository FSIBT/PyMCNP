import typing
import dataclasses

from ..... import abc
from ..Read import Read


class Decode(Read):
    """
    Represents decode read data options.

    Attributes:
        keyword: decode read data option `DECODE` symbol.
        equals: decode read data option `=` symbol.
        password: decode read data option `password` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DECODE'] | str = abc.Terminal[r'DECODE']('DECODE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    password: typing.Annotated[abc.Terminal, r'\S+'] | str
