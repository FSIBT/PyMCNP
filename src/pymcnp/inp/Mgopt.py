import re

from . import _field
from . import _card
from .. import types


class Mgopt(_field.Fields, _card.Card):
    """
    Represents INP `mgopt` cards.
    """

    _KEYWORD = 'mgopt'

    mcal = _field.Field(types.String, 'Problem type setting', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'f', 'a'})
    igm = _field.Field(types.Integer, 'Total number of energy groups for all kinds of particle', required=True, numeric=int, invalid=lambda self, value: not value >= 0)
    iplt = _field.Field(types.Integer, 'Weight windows usage indicator', numeric=int, invalid=lambda self, value: value is not None and value not in {0, 1, 2})
    iab = _field.Field(types.Integer, 'Adjoint biasing for adjoint problems contorls', numeric=int, invalid=lambda self, value: value is not None and value not in {0, 1, 2})
    icw = _field.Field(types.Integer, 'Name of the reference cell for generated weight windows', numeric=int)
    fnw = _field.Field(types.Real, 'Normalization value for generated weight windows')
    rim = _field.Field(types.Real, 'Generated weight windows compression limit')

    _REGEX = re.compile(
        rf'\Amgopt( {types.String._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
