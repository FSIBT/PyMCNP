import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Fissrp(_field.Fields, _option.BlockOption):
    """
    Represents INP `fissrp` elements.
    """

    _KEYWORD = 'fissrp'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Print fission source rate on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Afissrp( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
