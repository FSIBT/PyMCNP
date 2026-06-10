import typing
import dataclasses

from ..... import abc
from ..Embee import Embee


class Comment(Embee):
    """
    Represents comment embee data options.

    Attributes:
        keyword: comment embee data option `COMMENT` symbol.
        equals: comment embee data option `=` symbol.
        value: comment embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'COMMENT'] | str = abc.Terminal[r'COMMENT']('COMMENT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'[a-z0-9]{0,128}'] | str
