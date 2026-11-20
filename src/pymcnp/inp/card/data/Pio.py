import typing


from .... import abc
from ..Data import Data


class Pio(Data):
    """
    Represents pio data cards.

    Attributes:
        keyword: pio data card ``r'PIO'`` symbol.
        value: pio data card ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PIO'] = abc.Terminal[r'PIO']('PIO')
    value: typing.Annotated[abc.Terminal, r'(?:NO|ON)'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
