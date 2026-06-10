import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Sc(Data):
    """
    Represents sc data cards.

    Attributes:
        keyword: sc data card `SC` symbol.
        suffix: sc data card `n` parameter.
        comment: sc data card `comment` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SC'] | str = abc.Terminal[r'SC']('SC')
    suffix: literal.Integer | int | str
    comment: typing.Annotated[abc.Terminal, r'[\s\S]*?(?=\n[^ ]{1,5}|\Z)'] | str

    def __post_init__(self) -> None:
        """
        Validates sc data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
