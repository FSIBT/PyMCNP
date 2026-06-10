import typing
import dataclasses

from ..... import abc
from ..Act import Act


class Fission(Act):
    """
    Represents fission act data options.

    Attributes:
        keyword: fission act data option `FISSION` symbol.
        equals: fission act data option `=` symbol.
        value: fission act data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FISSION'] | str = abc.Terminal[r'FISSION']('FISSION')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'NONE|ALL|(?:[npefa](?:,[npefa]){0,4})'] | str
