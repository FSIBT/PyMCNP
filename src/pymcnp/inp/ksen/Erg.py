import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Erg(_field.Fields, _option.KsenOption):
    """
    Represents INP `erg` elements.
    """

    _KEYWORD = 'erg'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    energies = _field.Field.tuple(types.Real, 'List of energies', required=True)

    _REGEX = re.compile(rf'\Aerg((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
