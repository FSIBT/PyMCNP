import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Kcode(Data):
    """
    Represents kcode data cards.

    Attributes:
        keyword: kcode data card `KCODE` symbol.
        nsrck: kcode data card `nsrck` parameter.
        rkk: kcode data card `rkk` parameter.
        ikz: kcode data card `ikz` parameter.
        kct: kcode data card `kct` parameter.
        msrk: kcode data card `msrk` parameter.
        knrm: kcode data card `knrm` parameter.
        mrkp: kcode data card `mrkp` parameter.
        kc8: kcode data card `kc8` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KCODE'] | str = abc.Terminal[r'KCODE']('KCODE')
    nsrck: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    rkk: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ikz: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    kct: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    msrk: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    knrm: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    mrkp: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    kc8: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates kcode data cards.

        Raises:
            Error: Invalid value.
        """

        if isinstance(self.knrm, literal.Integer) and self.knrm not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.knrm=}')

        if isinstance(self.kc8, literal.Integer) and self.kc8 not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.kc8=}')
