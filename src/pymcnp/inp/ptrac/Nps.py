import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Nps(_field.Fields, _option.PtracOption):
    """
    Represents INP `nps` elements.
    """

    _KEYWORD = 'nps'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    particles = _field.Field.tuple(types.Integer, 'Sets the range of particle histories for which events will be output', required=True, numeric=int)

    _REGEX = re.compile(rf'\Anps((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
