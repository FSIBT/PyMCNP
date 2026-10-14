import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Type(_field.Fields, _option.PtracOption):
    """
    Represents INP `type` elements.
    """

    _KEYWORD = 'type'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    particles = _field.Field.tuple(types.Designator, 'Filters events based on one or more particle types', required=True, numeric=())

    _REGEX = re.compile(rf'\Atype((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
