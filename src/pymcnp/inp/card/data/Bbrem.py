import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Bbrem(Data):
    """
    Represents bbrem data cards.

    Attributes:
        keyword: bbrem data card `BBREM` symbol.
        b1: bbrem data card `b1` parameter.
        b2: bbrem data card `b2` parameter.
        b3: bbrem data card `b3` parameter.
        b4: bbrem data card `b4` parameter.
        b5: bbrem data card `b5` parameter.
        b6: bbrem data card `b6` parameter.
        b7: bbrem data card `b7` parameter.
        b8: bbrem data card `b8` parameter.
        b9: bbrem data card `b9` parameter.
        b10: bbrem data card `b10` parameter.
        b11: bbrem data card `b11` parameter.
        b12: bbrem data card `b12` parameter.
        b13: bbrem data card `b13` parameter.
        b14: bbrem data card `b14` parameter.
        b15: bbrem data card `b15` parameter.
        b16: bbrem data card `b16` parameter.
        b17: bbrem data card `b17` parameter.
        b18: bbrem data card `b18` parameter.
        b19: bbrem data card `b19` parameter.
        b20: bbrem data card `b20` parameter.
        b21: bbrem data card `b21` parameter.
        b22: bbrem data card `b22` parameter.
        b23: bbrem data card `b23` parameter.
        b24: bbrem data card `b24` parameter.
        b25: bbrem data card `b25` parameter.
        b26: bbrem data card `b26` parameter.
        b27: bbrem data card `b27` parameter.
        b28: bbrem data card `b28` parameter.
        b29: bbrem data card `b29` parameter.
        b30: bbrem data card `b30` parameter.
        b31: bbrem data card `b31` parameter.
        b32: bbrem data card `b32` parameter.
        b33: bbrem data card `b33` parameter.
        b34: bbrem data card `b34` parameter.
        b35: bbrem data card `b35` parameter.
        b36: bbrem data card `b36` parameter.
        b37: bbrem data card `b37` parameter.
        b38: bbrem data card `b38` parameter.
        b39: bbrem data card `b39` parameter.
        b40: bbrem data card `b40` parameter.
        b41: bbrem data card `b41` parameter.
        b42: bbrem data card `b42` parameter.
        b43: bbrem data card `b43` parameter.
        b44: bbrem data card `b44` parameter.
        b45: bbrem data card `b45` parameter.
        b46: bbrem data card `b46` parameter.
        b47: bbrem data card `b47` parameter.
        b48: bbrem data card `b48` parameter.
        b49: bbrem data card `b49` parameter.
        m: bbrem data card `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BBREM'] | str = abc.Terminal[r'BBREM']('BBREM')
    b1: literal.Real | int | float | decimal.Decimal | str
    b2: literal.Real | int | float | decimal.Decimal | str
    b3: literal.Real | int | float | decimal.Decimal | str
    b4: literal.Real | int | float | decimal.Decimal | str
    b5: literal.Real | int | float | decimal.Decimal | str
    b6: literal.Real | int | float | decimal.Decimal | str
    b7: literal.Real | int | float | decimal.Decimal | str
    b8: literal.Real | int | float | decimal.Decimal | str
    b9: literal.Real | int | float | decimal.Decimal | str
    b10: literal.Real | int | float | decimal.Decimal | str
    b11: literal.Real | int | float | decimal.Decimal | str
    b12: literal.Real | int | float | decimal.Decimal | str
    b13: literal.Real | int | float | decimal.Decimal | str
    b14: literal.Real | int | float | decimal.Decimal | str
    b15: literal.Real | int | float | decimal.Decimal | str
    b16: literal.Real | int | float | decimal.Decimal | str
    b17: literal.Real | int | float | decimal.Decimal | str
    b18: literal.Real | int | float | decimal.Decimal | str
    b19: literal.Real | int | float | decimal.Decimal | str
    b20: literal.Real | int | float | decimal.Decimal | str
    b21: literal.Real | int | float | decimal.Decimal | str
    b22: literal.Real | int | float | decimal.Decimal | str
    b23: literal.Real | int | float | decimal.Decimal | str
    b24: literal.Real | int | float | decimal.Decimal | str
    b25: literal.Real | int | float | decimal.Decimal | str
    b26: literal.Real | int | float | decimal.Decimal | str
    b27: literal.Real | int | float | decimal.Decimal | str
    b28: literal.Real | int | float | decimal.Decimal | str
    b29: literal.Real | int | float | decimal.Decimal | str
    b30: literal.Real | int | float | decimal.Decimal | str
    b31: literal.Real | int | float | decimal.Decimal | str
    b32: literal.Real | int | float | decimal.Decimal | str
    b33: literal.Real | int | float | decimal.Decimal | str
    b34: literal.Real | int | float | decimal.Decimal | str
    b35: literal.Real | int | float | decimal.Decimal | str
    b36: literal.Real | int | float | decimal.Decimal | str
    b37: literal.Real | int | float | decimal.Decimal | str
    b38: literal.Real | int | float | decimal.Decimal | str
    b39: literal.Real | int | float | decimal.Decimal | str
    b40: literal.Real | int | float | decimal.Decimal | str
    b41: literal.Real | int | float | decimal.Decimal | str
    b42: literal.Real | int | float | decimal.Decimal | str
    b43: literal.Real | int | float | decimal.Decimal | str
    b44: literal.Real | int | float | decimal.Decimal | str
    b45: literal.Real | int | float | decimal.Decimal | str
    b46: literal.Real | int | float | decimal.Decimal | str
    b47: literal.Real | int | float | decimal.Decimal | str
    b48: literal.Real | int | float | decimal.Decimal | str
    b49: literal.Real | int | float | decimal.Decimal | str
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
