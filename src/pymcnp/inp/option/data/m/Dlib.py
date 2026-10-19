import typing
import dataclasses

from ..... import abc
from ..M import M


class Dlib(M):
    """
    Represents dlib m data options.

    Attributes:
        keyword: dlib m data option `DLIB` symbol.
        equals: dlib m data option `=` symbol.
        x: dlib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'DLIB'] | str = abc.Terminal[r'DLIB']('DLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str = dataclasses.field(kw_only=True)
