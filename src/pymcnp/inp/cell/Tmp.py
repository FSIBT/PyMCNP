import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tmp(_field.Fields, _option.CellOption):
    """
    Represents INP `tmp` elements.
    """

    _KEYWORD = 'tmp'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('temperature', 'suffix')

    suffix = _field.Field(types.Integer, 'Thermal time index', numeric=int)
    temperature = _field.Field.tuple(types.Real, 'Temperature at time index', required=True, invalid=lambda self, value: not min(map(lambda temp: temp, value)) > 0)

    _REGEX = re.compile(rf'\Atmp(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
