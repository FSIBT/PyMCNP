import re

from . import _field
from . import _card
from .. import types


class Wwg(_field.Fields, _card.Card):
    """
    Represents INP `wwg` cards.
    """

    _KEYWORD = 'wwg'

    tally = _field.Field(types.Integer, 'Problem tally number', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    cell = _field.Field(types.Integer, 'Cell-based or mesh-based weight window generator', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    lower = _field.Field(types.Real, 'Value of the generated lower weight-window bound for cell', required=True)
    setting = _field.Field(types.Integer, 'Energy- or time-dependent weight window toggle', numeric=int)

    _REGEX = re.compile(
        rf'\Awwg( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE
    )
