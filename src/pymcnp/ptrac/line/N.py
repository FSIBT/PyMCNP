import typing
import dataclasses

from ... import abc
from ..Line import Line


class N(Line):
    """
    Represents n lines.

    Attributes:
        n1: n line `n1` parameter.
        n2: n line `n2` parameter.
        n3: n line `n3` parameter.
        n4: n line `n4` parameter.
        n5: n line `n5` parameter.
        n6: n line `n6` parameter.
        n7: n line `n7` parameter.
        n8: n line `n8` parameter.
        n9: n line `n9` parameter.
        n10: n line `n10` parameter.
        n11: n line `n11` parameter.
        n12: n line `n12` parameter.
        n13: n line `n13` parameter.
        n14: n line `n14` parameter.
        n15: n line `n15` parameter.
        n16: n line `n16` parameter.
        n17: n line `n17` parameter.
        n18: n line `n18` parameter.
        n19: n line `n19` parameter.
        n20: n line `n20` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    blank: typing.Annotated[abc.Terminal, r' ']
    n1: typing.Annotated[abc.Terminal, r'.{5}']
    n2: typing.Annotated[abc.Terminal, r'.{5}']
    n3: typing.Annotated[abc.Terminal, r'.{5}']
    n4: typing.Annotated[abc.Terminal, r'.{5}']
    n5: typing.Annotated[abc.Terminal, r'.{5}']
    n6: typing.Annotated[abc.Terminal, r'.{5}']
    n7: typing.Annotated[abc.Terminal, r'.{5}']
    n8: typing.Annotated[abc.Terminal, r'.{5}']
    n9: typing.Annotated[abc.Terminal, r'.{5}']
    n10: typing.Annotated[abc.Terminal, r'.{5}']
    n11: typing.Annotated[abc.Terminal, r'.{5}']
    n12: typing.Annotated[abc.Terminal, r'.{5}']
    n13: typing.Annotated[abc.Terminal, r'.{5}']
    n14: typing.Annotated[abc.Terminal, r'.{5}']
    n15: typing.Annotated[abc.Terminal, r'.{5}']
    n16: typing.Annotated[abc.Terminal, r'.{5}']
    n17: typing.Annotated[abc.Terminal, r'.{5}']
    n18: typing.Annotated[abc.Terminal, r'.{5}']
    n19: typing.Annotated[abc.Terminal, r'.{5}']
    n20: typing.Annotated[abc.Terminal, r'.{5}']
