import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Par_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `par` elements variation #0.
    """

    _KEYWORD = 'par'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    kind = _field.Field(types.String, 'Source particle type', required=True, numeric=())

    _REGEX = re.compile(rf'\Apar( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
