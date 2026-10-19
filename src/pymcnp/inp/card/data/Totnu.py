import typing
import dataclasses


from .... import abc
from ..Data import Data


class Totnu(Data):
    """
    Represents totnu data cards.

    Attributes:
        keyword: totnu data card `TOTNU` symbol.
        value: totnu data card `NO` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'TOTNU'] | str = abc.Terminal[r'TOTNU']('TOTNU')
    value: typing.Annotated[abc.Terminal, r'NO'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
