import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tr_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `tr` elements variation #1.
    """

    _KEYWORD = 'tr'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    number = _field.Field(types.Distribution, 'Particle weight', required=True, numeric=())

    _REGEX = re.compile(rf'\Atr( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
