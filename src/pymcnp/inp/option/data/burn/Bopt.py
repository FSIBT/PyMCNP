import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Burn import Burn


class Bopt(Burn):
    """
    Represents bopt burn data options.

    Attributes:
        keyword: bopt burn data option `BOPT` symbol.
        equals: bopt burn data option `=` symbol.
        b1: bopt burn data option `b1` parameter.
        b2: bopt burn data option `b2` parameter.
        b3: bopt burn data option `b3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BOPT'] | str = abc.Terminal[r'BOPT']('BOPT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    b1: literal.Real | int | float | decimal.Decimal | str
    b2: literal.Real | int | float | decimal.Decimal | str
    b3: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates bopt burn data options.
        """

        if self.b3 not in {0, -1, 1}:
            raise abc.Error('Invalid value.', f'{self.b3=}')
