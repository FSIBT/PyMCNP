import typing
import dataclasses

from ..... import abc
from ..Ft import Ft


class Icd(Ft):
    """
    Represents icd ft data options.

    Attributes:
        id: icd group `ICD` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'ICD'] | str = abc.Terminal[r'ICD']('ICD')
