import typing


from .... import abc
from ..Data import Data


class Mplot(Data):
    """
    Represents mplot data cards.

    The plot commands, e.g., ``tal 4 freq 1000``, are MCPLOT commands, kept as
    words.

    Attributes:
        keyword: mplot data card ``r'MPLOT'`` symbol.
        x: mplot data card ``x`` parameter, the plot commands.
    """

    keyword: typing.Annotated[abc.Terminal, r'MPLOT'] = abc.Terminal[r'MPLOT']('MPLOT')
    x: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'[^\s$&]+'], None]
