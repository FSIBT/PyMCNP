import typing

from ... import abc
from .Distribution import Distribution


class DependentDistribution(abc.Nonterminal):
    """
    Represents dependent distribution literals.

    Attributes:
        keyword: dependent distribution literal `keyword` parameter.
        equals: dependent distribution literal `equals` parameter.
        distribution: dependent distribution literal `distribution` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'F(?:CEL|SUR|ERG|TME|DIR|VEC|NRM|POS|RAD|EXT|AXS|X|Y|Z|CCC|ARA|WGT|TR|EFF|PAR|DAT|LOC|BEM|BAP)'] | str
    equals: typing.Annotated[abc.Terminal, r'=| ']
    distribution: Distribution | str
