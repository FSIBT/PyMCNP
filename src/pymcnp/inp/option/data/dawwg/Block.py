import typing
import dataclasses

import collections
from ..... import abc
from ...Block import Block as Block_
from ..Dawwg import Dawwg
from .... import literal


class Block(Dawwg):
    """
    Represents block dawwg data options.

    Attributes:
        keyword: block dawwg data option `BLOCK` symbol.
        equals: block dawwg data option `=` symbol.
        k: block dawwg data option `k` parameter.
        options: block dawwg data option `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BLOCK'] | str = abc.Terminal[r'BLOCK']('BLOCK')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    k: literal.Integer | int | str
    options: typing.Annotated[abc.Array, Block_, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[Block_ | str] | str = abc.Terminal[r'']('')
