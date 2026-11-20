import typing

from .... import abc
from ... import literal
from ..Data import Data


class Thtme(Data):
    """
    Represents thtme data cards.

    Attributes:
        keyword: thtme data card ``r'THTME'`` symbol.
        t: thtme data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'THTME'] = abc.Terminal[r'THTME']('THTME')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates thtme data cards.

        Raises:
            Error: Invalid value.
        """

        if not isinstance(self.t, abc.Terminal) and not len(self.t) <= 99:
            raise abc.Error('Invalid value.', f'{self.t=}')
