import typing
import dataclasses

from ..... import abc
from ..Df import Df
from .... import literal


class Ic(Df):
    """
    Represents ic df data options.

    Attributes:
        keyword: ic df data option `IC` symbol.
        equals: ic df data option `=` symbol.
        value: ic df data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IC'] | str = abc.Terminal[r'IC']('IC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | typing.Annotated[abc.Terminal, r'(?:HE3|BF3|LIG|LII|ZNS|NAI|BGO|CSI|BC4|HPG)-1'] | int | str

    def __post_init__(self) -> None:
        """
        Validates ic df data options.

        Raises:
            Error: Invalid value.
        """

        if isinstance(self.value, literal.Integer) and self.value != 99:
            raise abc.Error('Invalid value.', f'{self.value=}')
