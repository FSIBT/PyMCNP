import re

from . import _number
from .Horizontal import Horizontal


class Integer(_number.Number):
    """
    Represents MCNP integers or horizontal syntax.

    Attributes:
        value: Integer value or horizontal syntax.
    """

    _REGEX = re.compile(r'\A(?:j|log|ilog|\d*m|i|r|(?:[-+0-9.eE][-+0-9.eEdD]*))\Z', re.IGNORECASE)

    def __init__(self, value: int | Horizontal):
        super().__init__(value)

    @staticmethod
    def _convert(value):
        return int(value)

    @staticmethod
    def _operand(other):
        if isinstance(other, Integer):
            return other.value
        if isinstance(other, int):
            return other

        return _number.UNSUPPORTED
