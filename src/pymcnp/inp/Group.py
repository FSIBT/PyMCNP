import re

from .. import abc


class Space(abc.Terminal):
    """
    Represents spaces for parameters.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&\n +|\n {1,5} *| +)([\s\S]*)', re.IGNORECASE)
    _default = ' '


class Group(abc.Nonterminal):
    """
    Represents groups.
    """

    _space = (Space,)
