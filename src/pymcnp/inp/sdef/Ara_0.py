import re

from .. import _field
from . import _option
from ... import types


class Ara_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `ara` elements variation #0.
    """

    _KEYWORD = 'ara'

    area = _field.Field(types.Real, 'Area of surface', required=True)

    _REGEX = re.compile(rf'\Aara( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
