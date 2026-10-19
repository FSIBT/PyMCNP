import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac


class Write(Ptrac):
    """
    Represents write ptrac data options.

    Attributes:
        keyword: write ptrac data option `WRITE` symbol.
        equals: write ptrac data option `=` symbol.
        value: write ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'WRITE'] | str = abc.Terminal[r'WRITE']('WRITE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:POS|ALL)'] | str = dataclasses.field(kw_only=True)
