import re

from . import _field
from . import _card
from .. import types


class Cut(_field.Fields, _card.Card):
    """
    Represents INP cut cards.
    """

    _KEYWORD = 'cut'

    designator = _field.Field(types.Designator, 'Data option particle designator', required=True)
    time_cutoff = _field.Field(types.Real, 'Time cutoff in shakes')
    energy_cutoff = _field.Field(types.Real, 'Lower energy cutoff')
    weight_cutoff1 = _field.Field(types.Real, 'Weight cutoff #1')
    weight_cutoff2 = _field.Field(types.Real, 'Weight cutoff #2')
    source_weight = _field.Field(types.Real, 'Minimum source weight')

    _REGEX = re.compile(
        rf'\Acut:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
