import re

from .. import _field
from . import _option
from ... import types


class Par_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `par` elements variation #0.
    """

    _KEYWORD = 'par'

    kind = _field.Field(types.String, 'Source particle type', required=True, numeric=())

    _REGEX = re.compile(rf'\Apar( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
