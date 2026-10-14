import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Erg_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `erg` elements variation #0.
    """

    _KEYWORD = 'erg'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    energy = _field.Field(types.Real, 'Kinetic energy', required=True)

    _REGEX = re.compile(rf'\Aerg( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
