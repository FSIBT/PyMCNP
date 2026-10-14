import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Vec(_field.Fields, _option.MeshOption):
    """
    Represents INP `vec` elements.
    """

    _KEYWORD = 'vec'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vector = _field.Field.tuple(types.Real, 'Vector giving the direction of the polar axis', required=True)

    _REGEX = re.compile(rf'\Avec((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
