import re
import dataclasses

from .. import abc


class CardSpace(abc.Terminal):
    """
    Represents spaces for parameters.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&\n *|\n {1,5} *| +)', re.IGNORECASE)
    _default = ' '


class Card(abc.Nonterminal):
    """
    Represents cards.
    """

    _space = (CardSpace,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)
