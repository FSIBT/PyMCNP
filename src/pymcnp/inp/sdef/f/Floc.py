import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Floc(_field.Fields, _option.FOption):
    """
    Represents INP `floc` elements.
    """

    _KEYWORD = 'floc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afloc( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
