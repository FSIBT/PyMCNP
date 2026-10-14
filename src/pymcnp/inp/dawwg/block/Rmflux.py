import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Rmflux(_field.Fields, _option.BlockOption):
    """
    Represents INP `rmflux` elements.
    """

    _KEYWORD = 'rmflux'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Prepare flux moments file on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Armflux( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
