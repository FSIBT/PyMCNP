import typing

from ..... import abc
from ..Act import Act
from .... import literal


class Dnbias(Act):
    """
    Represents dnbias act data options.

    Attributes:
        keyword: dnbias act data option ``r'DNBIAS'`` symbol.
        equals: dnbias act data option ``r'='`` symbol.
        n: dnbias act data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DNBIAS'] = abc.Terminal[r'DNBIAS']('DNBIAS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    n: literal.Integer

    def __post_init__(self) -> None:
        """
        Validates dnbais act data options.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.n <= 10):
            raise abc.Error('Invalid value.', f'{self.n=}')
