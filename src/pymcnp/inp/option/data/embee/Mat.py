import typing
import dataclasses

from ..... import abc
from ..Embee import Embee
from .... import literal


class Mat(Embee):
    """
    Represents mat embee data options.

    Attributes:
        keyword: mat embee data option `MAT` symbol.
        equals: mat embee data option `=` symbol.
        value: mat embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MAT'] | str = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates mat embee data options.
        """

        assert isinstance(self.value, literal.Integer)

        if not (0 <= self.value <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.value=}')
