import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmatreduce(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatreduce` elements.
    """

    _KEYWORD = 'fmatreduce'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Fmatreduce', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Afmatreduce( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
