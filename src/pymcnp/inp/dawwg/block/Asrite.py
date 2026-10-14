import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Asrite(_field.Fields, _option.BlockOption):
    """
    Represents INP `asrite` elements.
    """

    _KEYWORD = 'asrite'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Left-going flux at plane i', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aasrite( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
