import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Iso(Ksen):
    """
    Represents iso ksen data options.

    Attributes:
        keyword: iso ksen data option `ISO` symbol.
        equals: iso ksen data option `=` symbol.
        z: iso ksen data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ISO'] | str = abc.Terminal[r'ISO']('ISO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Zaid | str] | str = abc.Terminal[r'']('')
