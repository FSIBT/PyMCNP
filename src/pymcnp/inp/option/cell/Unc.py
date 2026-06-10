import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Unc(Cell):
    """
    Represents unc cell options.

    Attributes:
        keyword: unc cell option `UNC` symbol.
        colon: unc cell option `colon` parameter.
        particle: unc cell option `particle` parameter.
        equals: unc cell option `=` symbol.
        u: unc cell option `u` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'UNC'] | str = abc.Terminal[r'UNC']('UNC')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    u: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates unc cell options.
        """

        if self.u not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.u=}')
