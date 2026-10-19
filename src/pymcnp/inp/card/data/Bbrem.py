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

    keyword: typing.Annotated[abc.Terminal, r'BBREM'] | str = abc.Terminal[r'BBREM']('BBREM')
    b1: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b2: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b3: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b4: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b5: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b6: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b7: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b8: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b9: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b10: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b11: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b12: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b13: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b14: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b15: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b16: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b17: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b18: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b19: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b20: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b21: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b22: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b23: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b24: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b25: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b26: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b27: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b28: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b29: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b30: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b31: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b32: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b33: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b34: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b35: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b36: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b37: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b38: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b39: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b40: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b41: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b42: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b43: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b44: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b45: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b46: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b47: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b48: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b49: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)
