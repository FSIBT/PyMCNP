import typing
import dataclasses

from ..... import abc
from ..Ft import Ft


class Scd(Ft):
    """
    Represents scd ft data options.

    Attributes:
        id: scd group `SCD` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'SCD'] | str = abc.Terminal[r'SCD']('SCD')
