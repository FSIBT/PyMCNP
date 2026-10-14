import re

from .. import _field
from . import _entry
from ... import types
from ... import errors


class Variables(_field.Fields, _entry.DsEntry_2):
    """
    Represents INP `variables` elements.
    """

    _KEYWORD = ''

    _CODE = errors.InpCode.SEMANTICS_OPTION

    independent = _field.Field(types.Distribution, 'Independent source dependent variable', required=True, numeric=())
    dependent = _field.Field(types.Real, 'Dependent source dependent variable', required=True)

    _REGEX = re.compile(rf'\A({types.Distribution._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
