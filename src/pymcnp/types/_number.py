import re
import decimal
import operator
import typing

from . import _type
from .Horizontal import Repeat
from .Horizontal import Insert
from .Horizontal import Multiply
from .Horizontal import Jump
from .Horizontal import Log
from .. import errors

UNSUPPORTED = object()

_UNARY = ('hash', 'neg', 'pos', 'abs', 'bool', 'int', 'float', 'trunc', 'floor', 'ceil', 'round')
_COMPARE = ('lt', 'le', 'eq', 'ne', 'gt', 'ge')
_ARITHMETIC = ('add', 'sub', 'mul', 'mod', 'divmod', 'pow', 'floordiv', 'truediv')


def _unary(name):
    def method(self):
        return getattr(self.value, name)()

    method.__name__ = name
    return method


def _compare(name):
    function = getattr(operator, name)

    def method(a, b):
        if (operand := a._operand(b)) is not UNSUPPORTED:
            return function(a.value, operand)

    method.__name__ = f'__{name}__'
    return method


def _binary(name):
    def method(a, b):
        if (operand := a._operand(b)) is not UNSUPPORTED:
            return getattr(a.value, name)(operand)

    method.__name__ = name
    return method


class Number(_type.Type):
    """
    Represents generic MCNP numbers or horizontal syntax (e.g., jumps).

    Subclasses define `_REGEX`, `_convert` (decimal to the Python number) and `_operand`
    (operand to a Python number, or `UNSUPPORTED`).

    Attributes:
        value: Number value or horizontal syntax.
    """

    _REGEX = re.compile(r'\A(?:j|log|ilog|\d*m|i|r|(?:[-+0-9.eE][-+0-9.eEdD]*))\Z', re.IGNORECASE)

    @staticmethod
    def _convert(value: decimal.Decimal):  # pragma: no cover
        raise NotImplementedError

    @staticmethod
    def _operand(other):  # pragma: no cover
        raise NotImplementedError

    def __init__(self, value):
        """
        Initializes `Number`.

        Parameters:
            value: Number or horizontal syntax value.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

        self.value: typing.Final = value

    @classmethod
    def from_mcnp(cls, source: str):
        """
        Generates `Number` from MCNP.

        Parameters:
            source: MCNP number or horizontal syntax.

        Returns:
            `Number`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        for horizontal in (Repeat, Insert, Multiply, Jump, Log):
            try:
                return cls(horizontal.from_mcnp(source))
            except errors.TypesError:
                pass

        source = re.sub(r'([-+0-9.]+)([-+])([0-9]+)', r'\1e\2\3', source)
        source = re.sub(r'[dD]', 'e', source)
        if source[0] == 'e':
            source = '1' + source

        try:
            return cls(cls._convert(decimal.Decimal(source)))
        except decimal.InvalidOperation as err:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source) from err

    def to_mcnp(self):
        """
        Generates MCNP from `Number`.

        Returns:
            MCNP number.
        """

        return str(self.value)

    def __format__(self, spec):
        return self.value.__format__(spec)


for _name in _UNARY:
    setattr(Number, f'__{_name}__', _unary(f'__{_name}__'))
for _name in _COMPARE:
    setattr(Number, f'__{_name}__', _compare(_name))
for _name in _ARITHMETIC:
    setattr(Number, f'__{_name}__', _binary(f'__{_name}__'))
for _name in _ARITHMETIC:
    setattr(Number, f'__r{_name}__', _binary(f'__r{_name}__'))
