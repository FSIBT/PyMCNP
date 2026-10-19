import typing
import dataclasses

from ..... import abc
from ..Embed import Embed


class Debug(Embed):
    """
    Represents debug embed data options.

    Attributes:
        keyword: debug embed data option `DEBUG` symbol.
        equals: debug embed data option `=` symbol.
        value: debug embed data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'DEBUG'] | str = abc.Terminal[r'DEBUG']('DEBUG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:ECHOMESH)'] | str = dataclasses.field(kw_only=True)
