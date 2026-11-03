import typing


from .... import abc
from ..Data import Data


class Totnu(Data):
    """
    Represents totnu data cards.

    Attributes:
        keyword: totnu data card `TOTNU` symbol.
        value: totnu data card `NO` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'TOTNU'] | str = abc.Terminal[r'TOTNU']('TOTNU')
    value: typing.Annotated[abc.Terminal, r'NO'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
