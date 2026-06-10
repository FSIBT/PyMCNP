import typing
import dataclasses

import collections

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class New(Ssr):
    """
    Represents new ssr data options.

    Attributes:
        keyword: new ssr data option `NEW` symbol.
        equals: new ssr data option `=` symbol.
        s: new ssr data option `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NEW'] | str = abc.Terminal[r'NEW']('NEW')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
