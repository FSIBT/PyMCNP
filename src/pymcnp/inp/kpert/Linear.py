import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Linear(_field.Fields, _option.KpertOption):
    """
    Represents INP `linear` elements.
    """

    _KEYWORD = 'linear'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Pertubated fission source on/off', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Alinear( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
