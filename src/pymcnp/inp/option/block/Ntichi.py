import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ntichi(Block):
    """
    Represents ntichi block dawwg data options.

    Attributes:
        keyword: ntichi block suboption `NTICHI` symbol.
        equals: ntichi block suboption `=` symbol.
        value: ntichi block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NTICHI'] | str = abc.Terminal[r'NTICHI']('NTICHI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
