import re

from .. import _field
from . import _option
from ... import types


class Dir_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `dir` elements variation #0.
    """

    _KEYWORD = 'dir'

    cosine = _field.Field(types.Real, 'Cosine of the angle between VEC and particle')

    _REGEX = re.compile(rf'\Adir( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
