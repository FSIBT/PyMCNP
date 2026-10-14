import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Geom(_field.Fields, _option.FmeshOption):
    """
    Represents INP `geom` elements.
    """

    _KEYWORD = 'geom'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    geometry = _field.Field(types.String, 'Mesh geometry', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'xyz', 'rec', 'rzt', 'cyl'})

    _REGEX = re.compile(r'\Ageom(?: (xyz|rec|rzt|cyl))\Z', re.IGNORECASE)
