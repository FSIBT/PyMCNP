import re

from . import _field
from . import _card
from .. import types


class Cosyp(_field.Fields, _card.Card):
    """
    Represents INP cosyp cards.
    """

    _KEYWORD = 'cosyp'

    pre = _field.Field(types.Integer, 'Prefix number of the COSY map files', required=True, numeric=int)
    axsh = _field.Field(types.Integer, 'Horiztonal axis orientation', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2, 3})
    axsv = _field.Field(types.Integer, 'Vertical axis orientation', required=True, numeric=int, invalid=lambda self, value: value not in {1, 2, 3})
    emaps = _field.Field.tuple(types.Real, 'Tuple of operating beam energies', required=True)

    _REGEX = re.compile(
        rf'\Acosyp( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE
    )
