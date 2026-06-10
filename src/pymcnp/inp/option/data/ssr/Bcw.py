import typing
import decimal
import dataclasses

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Bcw(Ssr):
    """
    Represents bcw ssr data options.

    Attributes:
        keyword: bcw ssr data option `BCW` symbol.
        equals: bcw ssr data option `=` symbol.
        r: bcw ssr data option `r` parameter.
        zb: bcw ssr data option `zb` parameter.
        ze: bcw ssr data option `ze` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BCW'] | str = abc.Terminal[r'BCW']('BCW')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: literal.Real | int | float | decimal.Decimal | str
    zb: literal.Real | int | float | decimal.Decimal | str
    ze: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates bcw ssr data options.
        """

        assert isinstance(self.zb, literal.Real)
        assert isinstance(self.ze, literal.Real)

        if not (0 < self.zb < self.ze):
            raise abc.Error('Invalid value.', f'{self.ze=}')
