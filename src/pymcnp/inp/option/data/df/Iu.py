import typing
import dataclasses

from ..... import abc
from ..Df import Df
from .... import literal


class Iu(Df):
    """
    Represents iu df data options.

    Attributes:
        keyword: iu df data option `IU` symbol.
        equals: iu df data option `=` symbol.
        value: iu df data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IU'] | str = abc.Terminal[r'IU']('IU')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates iu df data options.

        Raises:
            Error: Invalid value.
        """

        if self.value not in {1, 2}:
            raise abc.Error('Invalid value.', f'{self.value=}')
