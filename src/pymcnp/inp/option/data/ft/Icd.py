import typing

from ..... import abc
from ..Ft import Ft


class Icd(Ft):
    """
    Represents icd ft data options.

    Attributes:
        id: icd group `ICD` symbol.
    """

    id: typing.Annotated[abc.Terminal, r'ICD'] | str = abc.Terminal[r'ICD']('ICD')
