import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Fc(Data):
    """
    Represents fc data cards.

    Attributes:
        keyword: fc data card `FC` symbol.
        suffix: fc data card `n` parameter.
        info: fc data card `info` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FC'] | str = abc.Terminal[r'FC']('FC')
    suffix: literal.Integer | int | str
    info: typing.Annotated[abc.Terminal, r'[\s\S]*?(?=\n[^ ]{1,5}|\Z)'] | str

    def __post_init__(self) -> None:
        """
        Validates fc data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
