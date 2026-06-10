import typing
import dataclasses

from ..... import abc
from ..Read import Read


class Encode(Read):
    """
    Represents encode read data options.

    Attributes:
        keyword: encode read data option `ENCODE` symbol.
        equals: encode read data option `=` symbol.
        password: encode read data option `password` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ENCODE'] | str = abc.Terminal[r'ENCODE']('ENCODE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    password: typing.Annotated[abc.Terminal, r'\S+'] | str
