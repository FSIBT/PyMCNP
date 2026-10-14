import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ajed(_field.Fields, _option.BlockOption):
    """
    Represents INP `ajed` elements.
    """

    _KEYWORD = 'ajed'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Regular/adjoint edits control', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aajed( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
