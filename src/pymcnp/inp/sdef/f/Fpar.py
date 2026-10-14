import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Fpar(_field.Fields, _option.FOption):
    """
    Represents INP `fpar` elements.
    """

    _KEYWORD = 'fpar'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afpar( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
