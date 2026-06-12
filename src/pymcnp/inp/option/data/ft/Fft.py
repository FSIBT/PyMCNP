import typing
import dataclasses

from ..... import abc
from ..Ft import Ft


class Fft(Ft):
    """
    Represents fft ft data options.

    Attributes:
        id: fft group `FFT` symbol.
        lkji: fft group `lkji` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'FFT'] | str = abc.Terminal[r'FFT']('FFT')
    lkji: typing.Annotated[abc.Terminal, r'[01]{4}'] | str
