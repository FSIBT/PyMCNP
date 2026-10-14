import re

from .. import _field
from . import _entry
from ... import types


class Photonbias(_field.Fields, _entry.PikmtEntry):
    """
    Represents INP `photonbias` elements.
    """

    _KEYWORD = ''

    zaid = _field.Field(types.Zaid, 'Bias nuclide identifier', required=True, numeric=())
    ipiki = _field.Field(types.Integer, 'Bias controls', required=True, numeric=int)

    _REGEX = re.compile(rf'\A({types.Zaid._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
