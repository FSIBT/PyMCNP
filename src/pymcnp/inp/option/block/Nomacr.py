import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Nomacr(Block):
    """
    Represents nomacr block dawwg data options.

    Attributes:
        keyword: nomacr block suboption `NOMACR` symbol.
        equals: nomacr block suboption `=` symbol.
        value: nomacr block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOMACR'] | str = abc.Terminal[r'NOMACR']('NOMACR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
