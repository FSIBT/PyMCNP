import re

from .. import _field
from . import _option
from ... import types


class Wgt_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `wgt` elements variation #0.
    """

    _KEYWORD = 'wgt'

    weight = _field.Field(types.Real, 'Particle weight', required=True)

    _REGEX = re.compile(rf'\Awgt( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
