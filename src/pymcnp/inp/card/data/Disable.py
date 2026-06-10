import typing
import dataclasses


from .... import abc
from ..Data import Data
from ... import option


class Disable(Data):
    """
    Represents disable data cards.

    Attributes:
        keyword: disable data card `DISABLE` symbol.
        options: disable data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DISABLE'] | str = abc.Terminal[r'DISABLE']('DISABLE')
    options: option.data.Disable | str
