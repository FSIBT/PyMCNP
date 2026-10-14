import re

from . import _field
from . import _card
from .. import types


class Ds_0(_field.Fields, _card.Card):
    """
    Represents INP `ds` elements variation #0.
    """

    _KEYWORD = 'ds'

    _ORDER = ('suffix', 'js', 'option')

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    option = _field.Field(types.String, 'Dependent variable setting', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'h', 'l', 's'})
    js = _field.Field.tuple(types.Real, 'Depdented source dependent variables', required=True)

    _REGEX = re.compile(rf'\Ads(\d+)( [hls])?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
