import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Avatar(Block):
    """
    Represents avatar block dawwg data options.

    Attributes:
        keyword: avatar block suboption `AVATAR` symbol.
        equals: avatar block suboption `=` symbol.
        value: avatar block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'AVATAR'] | str = abc.Terminal[r'AVATAR']('AVATAR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str = dataclasses.field(kw_only=True)
