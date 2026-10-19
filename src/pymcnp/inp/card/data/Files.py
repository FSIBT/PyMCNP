import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Files(Data):
    """
    Represents files data cards.

    Attributes:
        keyword: files data card `FILES` symbol.
        unit_no: files data card `unit_no` parameter.
        filename: files data card `filename` parameter.
        access: files data card `access` parameter.
        form: files data card `form` parameter.
        record_length: files data card `record_length` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'FILES'] | str = abc.Terminal[r'FILES']('FILES')
    unit_no: literal.Integer | int | str = dataclasses.field(kw_only=True)
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str = dataclasses.field(kw_only=True)
    access: typing.Annotated[abc.Terminal, r'SEQUENTIAL|DIRECT|S|D'] | str = dataclasses.field(kw_only=True)
    form: typing.Annotated[abc.Terminal, r'FORMATTED|UNFORMATTED|F|U'] | str = dataclasses.field(kw_only=True)
    record_length: literal.Integer | int | str = dataclasses.field(kw_only=True)
