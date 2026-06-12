import typing
import dataclasses

import collections

from .... import abc
from ... import literal
from ..Data import Data


class Fq(Data):
    """
    Represents fq data cards.

    Attributes:
        keyword: fq data card `FQ` symbol.
        suffix: fq data card `n` parameter.
        a: fq data card `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FQ'] | str = abc.Terminal[r'FQ']('FQ')
    suffix: literal.Integer | int | str
    a: (
        typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'F|D|U|S|M|C|E|T'], None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[typing.Annotated[abc.Terminal, r'F|D|U|S|M|C|E|T'] | str]
        | str
    ) = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fq data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.a, abc.Terminal) and not 1 <= len(self.a) <= 8:
            raise abc.Error('Invalid value.', f'{self.a=}')
