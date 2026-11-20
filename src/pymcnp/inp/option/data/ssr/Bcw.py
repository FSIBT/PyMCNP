import typing

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Bcw(Ssr):
    """
    Represents bcw ssr data options.

    Attributes:
        keyword: bcw ssr data option ``r'BCW'`` symbol.
        equals: bcw ssr data option ``r'='`` symbol.
        r: bcw ssr data option ``r`` parameter.
        zb: bcw ssr data option ``zb`` parameter.
        ze: bcw ssr data option ``ze`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BCW'] = abc.Terminal[r'BCW']('BCW')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    r: literal.Real
    zb: literal.Real
    ze: literal.Real

    def __post_init__(self) -> None:
        """
        Validates bcw ssr data options.

        Raises:
            Error: Invalid value.
        """

        if not (0 < self.zb < self.ze):
            raise abc.Error('Invalid value.', f'{self.ze=}')
