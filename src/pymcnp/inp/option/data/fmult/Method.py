import typing
import dataclasses

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Method(Fmult):
    """
    Represents method fmult data options.

    Attributes:
        keyword: method fmult data option `METHOD` symbol.
        equals: method fmult data option `=` symbol.
        m: method fmult data option `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'METHOD'] | str = abc.Terminal[r'METHOD']('METHOD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates method fmult data options.

        Raises:
            Error: Invalid value.
        """

        if self.m not in {0, 1, 3, 5, 6, 7}:
            raise abc.Error('Invalid value.', f'{self.m=}')
