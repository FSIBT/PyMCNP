import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Calcvols(_field.Fields, _option.EmbedOption):
    """
    Represents INP `calcvols` elements.
    """

    _KEYWORD = 'calc_vols'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Yes/no calculate the inferred geometry cell information', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Acalc_vols( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
