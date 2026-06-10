import typing
import dataclasses


from .... import abc
from ..Data import Data


class Pio(Data):
    """
    Represents pio data cards.

    Attributes:
        keyword: pio data card `PIO` symbol.
        value: pio data card `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PIO'] | str = abc.Terminal[r'PIO']('PIO')
    value: typing.Annotated[abc.Terminal, r'(?:NO|ON)'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
