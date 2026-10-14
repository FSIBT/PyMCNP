import re

from . import _field
from . import _card
from .. import types


class Phys_1(_field.Fields, _card.Card):
    """
    Represents INP `phys` elements variation #1.
    """

    _KEYWORD = 'phys:p'

    emcpf = _field.Field(types.Real, 'Upper energy limit for photon treatment')
    ides = _field.Field(
        types.Integer, 'Generation of elections by photon controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    nocoh = _field.Field(
        types.Integer, 'Coherent Thomson scattering controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    ispn = _field.Field(
        types.Integer, 'Photonuclear particle production controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0, 1}))
    )
    nodop = _field.Field(
        types.Integer, 'Photon Doppler energy broadening controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    fism = _field.Field(types.Integer, 'Selection of photofission method controls', numeric=int)

    _REGEX = re.compile(
        rf'\Aphys:p( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
