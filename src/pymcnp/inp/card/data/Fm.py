import typing
import dataclasses

from .... import abc
from ..Data import Data
from ... import literal


class Fm(Data):
    """
    Represents fm data cards.

    Attributes:
        prefix: fm data card `prefix` parameter.
        keyword: fm data card `FM` symbol.
        suffix: fm data card `n` parameter.
        bins: fm data card `bins` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    prefix: typing.Annotated[abc.Terminal, r'[*+]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'FM'] | str = abc.Terminal[r'FM']('FM')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    bins: typing.Annotated[abc.Terminal, r'[^\s$](?:[^$\n]*[^\s$])?(?:\n {1,5}[^\s$](?:[^$\n]*[^\s$])?)*'] | str = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates fm data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999) or self.suffix % 10 == 8:
            raise abc.Error('Invalid value.', f'{self.suffix=}')
