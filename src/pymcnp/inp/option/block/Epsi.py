import typing
import decimal

from .... import abc
from ..Block import Block
from ... import literal


class Epsi(Block):
    """
    Represents epsi block dawwg data options.

    Attributes:
        keyword: epsi block suboption `EPSI` symbol.
        equals: epsi block suboption `=` symbol.
        value: epsi block suboption `value` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EPSI'] | str = abc.Terminal[r'EPSI']('EPSI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
