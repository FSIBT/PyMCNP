import typing
import dataclasses

import collections

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Iso(Kpert):
    """
    Represents iso kpert data options.

    Attributes:
        keyword: iso kpert data option `ISO` symbol.
        equals: iso kpert data option `=` symbol.
        z: iso kpert data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ISO'] | str = abc.Terminal[r'ISO']('ISO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Zaid, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Zaid | str] | str = abc.Terminal[r'']('')
