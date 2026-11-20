import typing

from .... import abc
from ... import literal
from ..Data import Data


class Files(Data):
    """
    Represents files data cards.

    Attributes:
        keyword: files data card ``r'FILES'`` symbol.
        unit_no: files data card ``unit_no`` parameter.
        filename: files data card ``filename`` parameter.
        access: files data card ``access`` parameter.
        form: files data card ``form`` parameter.
        record_length: files data card ``record_length`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FILES'] = abc.Terminal[r'FILES']('FILES')
    unit_no: literal.Integer
    filename: typing.Annotated[abc.Terminal, r'\S+']
    access: typing.Annotated[abc.Terminal, r'SEQUENTIAL|DIRECT|S|D']
    form: typing.Annotated[abc.Terminal, r'FORMATTED|UNFORMATTED|F|U']
    record_length: literal.Integer
