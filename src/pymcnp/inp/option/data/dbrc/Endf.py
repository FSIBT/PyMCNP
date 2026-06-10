import typing
import dataclasses

from ..... import abc
from ..Dbrc import Dbrc
from .... import literal


class Endf(Dbrc):
    """
    Represents endf dbrc data options.

    Attributes:
        keyword: endf dbrc data option `ENDF` symbol.
        equals: endf dbrc data option `=` symbol.
        nn: endf dbrc data option `nn` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ENDF'] | str = abc.Terminal[r'ENDF']('ENDF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    nn: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates end dbrc data options.
        """

        if self.nn not in {71, 80}:
            raise abc.Error('Invalid value.', f'{self.nn=}')
