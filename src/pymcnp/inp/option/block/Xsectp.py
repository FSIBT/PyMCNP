import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Xsectp(Block):
    """
    Represents xsectp block dawwg data options.

    Attributes:
        keyword: xsectp block suboption `XSECTP` symbol.
        equals: xsectp block suboption `=` symbol.
        value: xsectp block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'XSECTP'] | str = abc.Terminal[r'XSECTP']('XSECTP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
