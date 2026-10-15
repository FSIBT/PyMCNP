import re

from . import _field
from . import _card
from .. import types


class Kcode(_field.Fields, _card.Card):
    """
    Represents INP `kcode` cards.
    """

    _KEYWORD = 'kcode'

    nsrck = _field.Field(
        types.Integer, 'Number of source histories per cycle', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 0))
    )
    rkk = _field.Field(types.Real, 'Initial guess of keff')
    ikz = _field.Field(types.Integer, 'Number of cycles to be skipped before beginning tally accumulation', numeric=int)
    kct = _field.Field(types.Integer, 'Total number of cycles to be done', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value > 0)))
    msrk = _field.Field(
        types.Integer,
        'Number of source points to allocate for',
        numeric=int,
        invalid=lambda self, value: (
            value is not None and (not (isinstance(value.value, types.Jump) or value < 40 * (1000 if not self.nsrck or isinstance(self.nsrck.value, types.Jump) else self.nsrck)))
        ),
    )
    knrm = _field.Field(
        types.Integer, 'Normalization of tallies setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    mrkp = _field.Field(
        types.Integer,
        'Maximum number of cycle values on MCTAL or RUNTPE files',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value > 0)),
    )
    kc8 = _field.Field(
        types.Integer, 'Number of cylces for average setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )

    _REGEX = re.compile(
        rf'\Akcode( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
