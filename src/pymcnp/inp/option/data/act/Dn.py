import typing
import dataclasses

from ..... import abc
from ..Act import Act


class Dn(Act):
    """
    Represents dn act data options.

    Attributes:
        keyword: dn act data option `DN` symbol.
        equals: dn act data option `=` symbol.
        value: dn act data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DN'] | str = abc.Terminal[r'DN']('DN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:MODEL|LIBRARY|BOTH|PROMPT)'] | str
