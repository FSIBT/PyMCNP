import typing

from ... import abc
from ..Block import Block


class Else(Block):
    """
    Represents non-parsed blocks.

    Attributes:
        text: Non-parsed block text.
    """


    text: typing.Annotated[abc.Terminal, r'[\s\S]+?(?=\n1\w+|\Z)']
