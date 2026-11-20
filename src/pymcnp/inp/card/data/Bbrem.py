import typing

from .... import abc
from ... import literal
from ..Data import Data


class Bbrem(Data):
    """
    Represents bbrem data cards.

    Attributes:
        keyword: bbrem data card ``r'BBREM'`` symbol.
        b1: bbrem data card ``b1`` parameter.
        b2: bbrem data card ``b2`` parameter.
        b3: bbrem data card ``b3`` parameter.
        b4: bbrem data card ``b4`` parameter.
        b5: bbrem data card ``b5`` parameter.
        b6: bbrem data card ``b6`` parameter.
        b7: bbrem data card ``b7`` parameter.
        b8: bbrem data card ``b8`` parameter.
        b9: bbrem data card ``b9`` parameter.
        b10: bbrem data card ``b10`` parameter.
        b11: bbrem data card ``b11`` parameter.
        b12: bbrem data card ``b12`` parameter.
        b13: bbrem data card ``b13`` parameter.
        b14: bbrem data card ``b14`` parameter.
        b15: bbrem data card ``b15`` parameter.
        b16: bbrem data card ``b16`` parameter.
        b17: bbrem data card ``b17`` parameter.
        b18: bbrem data card ``b18`` parameter.
        b19: bbrem data card ``b19`` parameter.
        b20: bbrem data card ``b20`` parameter.
        b21: bbrem data card ``b21`` parameter.
        b22: bbrem data card ``b22`` parameter.
        b23: bbrem data card ``b23`` parameter.
        b24: bbrem data card ``b24`` parameter.
        b25: bbrem data card ``b25`` parameter.
        b26: bbrem data card ``b26`` parameter.
        b27: bbrem data card ``b27`` parameter.
        b28: bbrem data card ``b28`` parameter.
        b29: bbrem data card ``b29`` parameter.
        b30: bbrem data card ``b30`` parameter.
        b31: bbrem data card ``b31`` parameter.
        b32: bbrem data card ``b32`` parameter.
        b33: bbrem data card ``b33`` parameter.
        b34: bbrem data card ``b34`` parameter.
        b35: bbrem data card ``b35`` parameter.
        b36: bbrem data card ``b36`` parameter.
        b37: bbrem data card ``b37`` parameter.
        b38: bbrem data card ``b38`` parameter.
        b39: bbrem data card ``b39`` parameter.
        b40: bbrem data card ``b40`` parameter.
        b41: bbrem data card ``b41`` parameter.
        b42: bbrem data card ``b42`` parameter.
        b43: bbrem data card ``b43`` parameter.
        b44: bbrem data card ``b44`` parameter.
        b45: bbrem data card ``b45`` parameter.
        b46: bbrem data card ``b46`` parameter.
        b47: bbrem data card ``b47`` parameter.
        b48: bbrem data card ``b48`` parameter.
        b49: bbrem data card ``b49`` parameter.
        m: bbrem data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BBREM'] = abc.Terminal[r'BBREM']('BBREM')
    b1: literal.Real
    b2: literal.Real
    b3: literal.Real
    b4: literal.Real
    b5: literal.Real
    b6: literal.Real
    b7: literal.Real
    b8: literal.Real
    b9: literal.Real
    b10: literal.Real
    b11: literal.Real
    b12: literal.Real
    b13: literal.Real
    b14: literal.Real
    b15: literal.Real
    b16: literal.Real
    b17: literal.Real
    b18: literal.Real
    b19: literal.Real
    b20: literal.Real
    b21: literal.Real
    b22: literal.Real
    b23: literal.Real
    b24: literal.Real
    b25: literal.Real
    b26: literal.Real
    b27: literal.Real
    b28: literal.Real
    b29: literal.Real
    b30: literal.Real
    b31: literal.Real
    b32: literal.Real
    b33: literal.Real
    b34: literal.Real
    b35: literal.Real
    b36: literal.Real
    b37: literal.Real
    b38: literal.Real
    b39: literal.Real
    b40: literal.Real
    b41: literal.Real
    b42: literal.Real
    b43: literal.Real
    b44: literal.Real
    b45: literal.Real
    b46: literal.Real
    b47: literal.Real
    b48: literal.Real
    b49: literal.Real
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
