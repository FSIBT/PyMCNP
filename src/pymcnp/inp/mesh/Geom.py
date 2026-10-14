import re

from .. import _field
from . import _option
from ... import types


class Geom(_field.Fields, _option.MeshOption):
    """
    Represents INP `geom` elements.
    """

    _KEYWORD = 'geom'

    geometry = _field.Field(types.String, 'Controls mesh geometry type', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'xyz', 'rzt', 'rpt', 'cyl', 'rec', 'sph'})

    _REGEX = re.compile(rf'\Ageom( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
