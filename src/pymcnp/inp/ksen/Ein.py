import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Ein(_field.Fields, _option.KsenOption):
    """
    Represents INP `ein` elements.
    """

    _KEYWORD = 'ein'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    energies = _field.Field.tuple(types.Real, 'List of ranges for incident energies', required=True)

    _REGEX = re.compile(rf'\Aein((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
