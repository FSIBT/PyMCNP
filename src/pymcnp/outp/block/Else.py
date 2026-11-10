import typing

from ... import abc
from ..Block import Block


class Else(Block):
    """
    Represents non-parsed blocks.

    Attributes:
        text: Non-parsed block text.
    """

    text: typing.Annotated[
        abc.Terminal,
        r'(?!\n \*{119}\n\n dump no\.(?:(?!\n1\w|\n \*{119})[\s\S])*\n mcnp     version [^\n]*\n?\Z)[\s\S]+?(?=\n1\w+|\Z|\n \*{119})',
    ]
