import typing

from ... import abc
from .Distribution import Distribution


class DependentDistribution(abc.Nonterminal):
    """
    Represents dependentdistribution literals.

    Attributes:
        keyword: dependentdistribution literal `keyword` parameter.
        equals: dependentdistribution literal `equals` parameter.
        distribution: dependentdistribution literal `distribution` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'F(?:CEL|SUR|ERG|TME|DIR|VEC|NRM|POS|RAD|EXT|AXS|X|Y|Z|CCC|ARA|WGT|TR|EFF|PAR|DAT|LOC|BEM|BAP)'] | str
    equals: typing.Annotated[abc.Terminal, r'=| ']
    distribution: Distribution | str
