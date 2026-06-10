import typing
import dataclasses


from .... import abc
from ..Data import Data


class Mphys(Data):
    """
    Represents mphys data cards.

    Attributes:
        keyword: mphys data card `MPHYS` symbol.
        toggle: mphys data card `toggle` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MPHYS'] | str = abc.Terminal[r'MPHYS']('MPHYS')
    toggle: typing.Annotated[abc.Terminal, r'ON|OFF'] | str
