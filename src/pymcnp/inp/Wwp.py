import re

from . import _field
from . import _card
from .. import types


class Wwp(_field.Fields, _card.Card):
    """
    Represents INP `wwp` cards.
    """

    _KEYWORD = 'wwp'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    wupn = _field.Field(types.Real, 'Multiplier to define the weight window upper limit', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 2)))
    wsurvn = _field.Field(
        types.Real,
        'Multiplier to define the maximum Russian roulette survival weight within the window',
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or 1 < value)),
    )
    mxspln = _field.Field(types.Real, 'Maximum number of integer splits', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or 1 < value)))
    mwhere = _field.Field(
        types.Integer, 'Controls where to check a particle’s weight', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0, 1}))
    )
    switchn = _field.Field(types.Real, 'Controls where to get the lower weight-window bounds')
    mtime = _field.Field(types.Integer, 'Energy/time-dependent window setting', numeric=int)
    wnrom = _field.Field(types.Real, 'Weight-window normalization factor')
    etsplt = _field.Field(
        types.Integer, 'ESLPT & TSPLT split/roulette on/off', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    wu = _field.Field(types.Real, 'Limits the maximum lower weight-window bound for any particle, energy, or time')
    nmfp = _field.Field(types.Real, 'Limits the maximum lower weight-window bound for any particle, energy, or time')

    _REGEX = re.compile(
        rf'\Awwp:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
