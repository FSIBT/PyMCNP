import typing

from ..... import abc
from ..Ft import Ft


class Fft(Ft):
    """
    Represents fft ft data options.

    Attributes:
        id: fft group ``r'FFT'`` symbol.
        lkji: fft group ``lkji`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'FFT'] | str = abc.Terminal[r'FFT']('FFT')
    lkji: typing.Annotated[abc.Terminal, r'[01]{4}'] | str
