import typing
import decimal
import dataclasses

from ..... import abc
from ..Df import Df
from .... import literal


class Fac(Df):
    """
    Represents fac df data options.

    Attributes:
        keyword: fac df data option `FAC` symbol.
        equals: fac df data option `=` symbol.
        value: fac df data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FAC'] | str = abc.Terminal[r'FAC']('FAC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates fac df data options.
        """

        assert isinstance(self.value, literal.Real)

        if not (self.value > 0 or self.value in {-1, -2, -3}):
            raise abc.Error('Invalid value.', f'{self.value=}')
