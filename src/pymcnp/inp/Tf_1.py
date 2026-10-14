import re

from . import _field
from . import _card
from .. import types


class Tf_1(_field.Fields, _card.Card):
    """
    Represents INP `tf` elements variation #1.
    """

    _KEYWORD = 'tf'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    if1 = _field.Field(types.Integer, 'Cell, surface, or detector bin number', numeric=int)
    id1 = _field.Field(types.Integer, 'Total, flagged, or un-collided bin number', numeric=int)
    iu1 = _field.Field(types.Integer, 'User bin number', numeric=int)
    is1 = _field.Field(types.Integer, 'Segment bin number', numeric=int)
    im1 = _field.Field(types.Integer, 'Multiplier bin number', numeric=int)
    ic1 = _field.Field(types.Integer, 'Cosine bin number', numeric=int)
    ie1 = _field.Field(types.Integer, 'Energy bin number', numeric=int)
    it1 = _field.Field(types.Integer, 'Time bin number', numeric=int)
    if2 = _field.Field(types.Integer, 'Cell, surface, or detector bin number', numeric=int)
    id2 = _field.Field(types.Integer, 'Total, flagged, or un-collided bin number', numeric=int)
    iu2 = _field.Field(types.Integer, 'User bin number', numeric=int)
    is2 = _field.Field(types.Integer, 'Segment bin number', numeric=int)
    im2 = _field.Field(types.Integer, 'Multiplier bin number', numeric=int)
    ic2 = _field.Field(types.Integer, 'Cosine bin number', numeric=int)
    ie2 = _field.Field(types.Integer, 'Energy bin number', numeric=int)
    it2 = _field.Field(types.Integer, 'Time bin number', numeric=int)

    _REGEX = re.compile(
        rf'\Atf(\d+)( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
