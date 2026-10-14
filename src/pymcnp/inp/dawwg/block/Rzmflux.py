import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Rzmflux(_field.Fields, _option.BlockOption):
    """
    Represents INP `rzmflux` elements.
    """

    _KEYWORD = 'rzmflux'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Write b-flux file on/off', required=True, numeric=int, invalid=lambda self, value: value not in {0, 1})

    _REGEX = re.compile(rf'\Arzmflux( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
