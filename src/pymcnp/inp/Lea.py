import re

from . import _field
from . import _card
from .. import types


class Lea(_field.Fields, _card.Card):
    """
    Represents INP `lea` cards.
    """

    _KEYWORD = 'lea'

    ipht = _field.Field(
        types.Integer, 'Generation of de-excitation photons setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    icc = _field.Field(
        types.Integer,
        'Level of physics for PHT physics setting',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1, 2, 3, 4})),
    )
    nobalc = _field.Field(
        types.Integer, 'Mass-energy balancing in cascade setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    nobale = _field.Field(
        types.Integer, 'Mass-energy balancing in evaporation setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    ifbrk = _field.Field(
        types.Integer, 'Mass-energy balancing in Fermi-breakup setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1}))
    )
    ilvden = _field.Field(
        types.Integer, 'Level-density model setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1, -1}))
    )
    ievap = _field.Field(
        types.Integer, 'Evaporation and fission model setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1, -1, 2}))
    )
    nofis = _field.Field(types.Integer, 'Fission setting', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1})))

    _REGEX = re.compile(
        rf'\Alea( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
