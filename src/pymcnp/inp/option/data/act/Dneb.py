import typing
import dataclasses

import collections

from ..... import abc
from ..Act import Act
from .... import group


class Dneb(Act):
    """
    Represents dneb act data options.

    Attributes:
        keyword: dneb act data option `DNEB` symbol.
        equals: dneb act data option `=` symbol.
        value: dneb act data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DNEB'] | str = abc.Terminal[r'DNEB']('DNEB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, group.Bias, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Bias | str] | str = abc.Terminal[r'']('')
