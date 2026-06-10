import typing
import dataclasses

from ..... import abc
from ..Embee import Embee


class Errors(Embee):
    """
    Represents errors embee data options.

    Attributes:
        keyword: errors embee data option `ERRORS` symbol.
        equals: errors embee data option `=` symbol.
        value: errors embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ERRORS'] | str = abc.Terminal[r'ERRORS']('ERRORS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
