import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Erg_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `erg` elements variation #1.
    """

    _KEYWORD = 'erg'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    energy = _field.Field(types.Distribution, 'Kinetic energy', required=True, numeric=())

    _REGEX = re.compile(rf'\Aerg( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
