import re

from . import _field
from . import _card
from .. import types


class Phys_3(_field.Fields, _card.Card):
    """
    Represents INP `phys` elements variation #3.
    """

    _KEYWORD = 'phys:h'

    emax = _field.Field(types.Real, 'Upper proton energy limit')
    ean = _field.Field(types.Real, 'Analog energy limit')
    tabl = _field.Field(types.Real, 'Table-based physics cutoff', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == -1 or value >= 0)))
    istrg = _field.Field(
        types.Integer, 'Charged-particle straggling controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    recl = _field.Field(types.Real, 'Light ion recoil control', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or (value >= 0 and value <= 1))))
    i_mcs_model = _field.Field(
        types.Integer,
        'Choice of Coulomb scattering model controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0, 1, 2})),
    )
    i_int_model = _field.Field(
        types.Integer,
        'Treatment of nuclear interactions controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0, 1, 2})),
    )
    i_els_model = _field.Field(
        types.Integer,
        'Treatment of nuclear elastic scattering controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0})),
    )
    efac = _field.Field(types.Real, 'Stopping power energy spacing', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or (value >= 0.8 and value <= 0.99))))
    ckvnum = _field.Field(types.Real, 'Crenkov photon emission scalar', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or (value >= 0 and value < 1))))
    drp = _field.Field(types.Real, 'Lower energy delta-ray cutoff', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 0 or value == -1)))

    _REGEX = re.compile(
        rf'\Aphys:h( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
