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
        r'(?!\n \*{119}\n\n dump no\. .{4} on file runtpf     nps = .{11}     coll = .{14}     ctm = .{11}   nrn =        \n .{9}\n\n .{9} warning messages so far\.\n\n\n run terminated when .{11}  particle histories were done\.\n\n computer time = .{7} minutes\n\n mcnp     version ..{13}.{38}                     probid =  .{18})[\s\S]+?(?=\n1\w+|\Z|\n \*{119})',
    ]
