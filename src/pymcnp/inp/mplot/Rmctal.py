import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Rmctal(_field.Fields, _option.MplotOption):
    """
    Represents INP `rmctal` elements.
    """

    _KEYWORD = 'rmctal'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    filename = _field.Field(types.String, 'MCTAL file to read', required=True, numeric=())

    _REGEX = re.compile(rf'\Armctal( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
