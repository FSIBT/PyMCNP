import typing
import dataclasses

from ..... import abc
from ..Act import Act
from .... import literal


class Dnbias(Act):
    """
    Represents dnbias act data options.

    Attributes:
        keyword: dnbias act data option `DNBIAS` symbol.
        equals: dnbias act data option `=` symbol.
        n: dnbias act data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DNBIAS'] | str = abc.Terminal[r'DNBIAS']('DNBIAS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates dnbais act data options.
        """

        assert isinstance(self.n, literal.Integer)

        if not (1 <= self.n <= 10):
            raise abc.Error('Invalid value.', f'{self.n=}')
