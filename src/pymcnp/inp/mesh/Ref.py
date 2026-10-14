import re

from .. import _field
from . import _option
from ... import types


class Ref(_field.Fields, _option.MeshOption):
    """
    Represents INP `ref` elements.
    """

    _KEYWORD = 'ref'

    point = _field.Field.tuple(types.Real, 'Mesh reference point', required=True)

    _REGEX = re.compile(rf'\Aref((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
