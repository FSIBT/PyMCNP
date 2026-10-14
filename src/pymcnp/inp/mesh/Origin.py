import re

from .. import _field
from . import _option
from ... import types


class Origin(_field.Fields, _option.MeshOption):
    """
    Represents INP `origin` elements.
    """

    _KEYWORD = 'origin'

    point = _field.Field.tuple(types.Real, 'Mesh origin point', required=True)

    _REGEX = re.compile(rf'\Aorigin((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
