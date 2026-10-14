import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ptconv(_field.Fields, _option.BlockOption):
    """
    Represents INP `ptconv` elements.
    """

    _KEYWORD = 'ptconv'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Special criticality convergence scheme on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Aptconv( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
