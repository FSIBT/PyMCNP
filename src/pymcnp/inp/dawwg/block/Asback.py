import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Asback(_field.Fields, _option.BlockOption):
    """
    Represents INP `asback` elements.
    """

    _KEYWORD = 'asback'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Front-going flux at plane k', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aasback( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
