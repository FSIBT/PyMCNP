import typing
import dataclasses

import collections

from ..... import abc
from ..Act import Act
from .... import group


class Dgeb(Act):
    """
    Represents dgeb act data options.

    Attributes:
        keyword: dgeb act data option `DGEB` symbol.
        equals: dgeb act data option `=` symbol.
        value: dgeb act data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DGEB'] | str = abc.Terminal[r'DGEB']('DGEB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, group.Bias, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Bias | str] | str = abc.Terminal[r'']('')
