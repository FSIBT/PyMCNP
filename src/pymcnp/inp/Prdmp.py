import re

from . import _field
from . import _card
from .. import types


class Prdmp(_field.Fields, _card.Card):
    """
    Represents INP `prdmp` cards.
    """

    _KEYWORD = 'prdmp'

    ndp = _field.Field(types.Integer, 'Increment for printing tallies', numeric=int)
    ndm = _field.Field(types.Integer, 'Increment for dumping to RUNTPE file', numeric=int)
    mct = _field.Field(types.Integer, 'Controls printing of MCTAL file', numeric=int)
    ndmp = _field.Field(types.Integer, 'Maximum number of dumps on RUNTPE file', numeric=int)
    dmmp = _field.Field(types.Integer, 'Controls frequently of tally fluctuation chart', numeric=int)

    _REGEX = re.compile(
        rf'\Aprdmp( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
