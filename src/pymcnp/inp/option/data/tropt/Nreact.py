import typing
import dataclasses

from ..... import abc
from ..Tropt import Tropt


class Nreact(Tropt):
    """
    Represents nreact tropt data options.

    Attributes:
        keyword: nreact tropt data option `NREACT` symbol.
        equals: nreact tropt data option `=` symbol.
        value: nreact tropt data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'NREACT'] | str = abc.Terminal[r'NREACT']('NREACT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:OFF|ON|ATTEN|REMOVE)'] | str = dataclasses.field(kw_only=True)
