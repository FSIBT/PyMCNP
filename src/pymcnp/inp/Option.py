import re
import dataclasses

from .. import abc


class OptionSpace(abc.Terminal):
    """
    Represents spaces for parameters.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&\n +|\n {1,5} *| +)', re.IGNORECASE)
    _default = ' '


class Option(abc.Nonterminal):
    """
    Represents options.
    """

    _space = (OptionSpace,)

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)
