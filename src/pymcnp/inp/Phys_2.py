import re

from . import _field
from . import _card
from .. import types


class Phys_2(_field.Fields, _card.Card):
    """
    Represents INP `phys` elements variation #2.
    """

    _KEYWORD = 'phys:e'

    emax = _field.Field(types.Real, 'Upper limit for electron energy')
    ides = _field.Field(
        types.Integer, 'Photon electron production controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    iphot = _field.Field(
        types.Integer, 'Electron photon production controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    ibad = _field.Field(
        types.Integer,
        'Bremsstrahlung angular distribution method controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1})),
    )
    istrg = _field.Field(
        types.Integer, 'Electron continuous-energy straggling controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    bnum = _field.Field(types.Real, 'Bremsstrahlung photon production controls')
    xnum = _field.Field(types.Real, 'Sampling of electron-induced x-rays controls', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 0)))
    rnok = _field.Field(types.Integer, 'Knock-on electron creation controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 0)))
    enum = _field.Field(
        types.Integer, 'Photon-induced secondary electron creation controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 0))
    )
    numb = _field.Field(
        types.Integer, 'Bremsstrahlung electron creation controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value >= 0))
    )
    i_mcs_model = _field.Field(
        types.Integer, 'Choice of Coulomb scattering model controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0}))
    )
    j = _field.Field(types.String, 'Not used', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'j j'})
    efac = _field.Field(
        types.Real, 'Stopping power energy spacing controls', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or (value >= 0.8 and value <= 0.99)))
    )
    electron_method_boundary = _field.Field(types.Real, 'Single-event transport start sontrols')
    ckvnum = _field.Field(types.Real, 'Crenkov photon emission scalar', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or (value >= 0 and value < 1))))

    _REGEX = re.compile(
        r'\Aphys:e(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (\S+))?(?: (j j))?(?: (\S+))?(?: (\S+))?(?: (\S+))?\Z',
        re.IGNORECASE,
    )
