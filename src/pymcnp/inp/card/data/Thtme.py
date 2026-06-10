import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Thtme(Data):
    """
    Represents thtme data cards.

    Attributes:
        keyword: thtme data card `THTME` symbol.
        t: thtme data card `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'THTME'] | str = abc.Terminal[r'THTME']('THTME')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates thtme data cards.
        """

        if not isinstance(self.t, abc.Terminal) and not len(self.t) <= 99:
            raise abc.Error('Invalid value.', f'{self.t=}')
