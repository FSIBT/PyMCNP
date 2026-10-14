import re

from . import _field
from . import _card
from .. import types


class Lca(_field.Fields, _card.Card):
    """
    Represents INP `lca` cards.
    """

    _KEYWORD = 'lca'

    ielas = _field.Field(
        types.Integer,
        'Elastic scattering controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1 or (value == 2))),
    )
    ipreg = _field.Field(
        types.Integer,
        'Pre-equilibrium model',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1 or (value == 2) or (value == 3))),
    )
    iexisa = _field.Field(
        types.Integer, 'Model choice controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1 or (value == 2)))
    )
    ichoic = _field.Field(types.Integer, 'ISABEL intranuclear cascade model control', numeric=int)
    jcoul = _field.Field(
        types.Integer,
        'Coulomb barrier for incident charged particle controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1)),
    )
    nexite = _field.Field(
        types.Integer,
        'Subtract nuclear recoil energy to get excitation energy',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1)),
    )
    npidk = _field.Field(
        types.Integer, 'Cutoff interact/terminate control', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1))
    )
    noact = _field.Field(
        types.Integer,
        'Particle transport settings',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == -2 or value == -1 or (value == 0) or (value == 1) or (value == 2))),
    )
    icem = _field.Field(
        types.Integer,
        'Choose alternative physics model',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1 or (value == 2))),
    )
    ilaq = _field.Field(
        types.Integer,
        'Choose light ion and nucleon physics modules',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value == 0 or value == 1)),
    )
    nevtype = _field.Field(types.Integer, 'Choose number of evaporation particles for GEM2', numeric=int)

    _REGEX = re.compile(
        rf'\Alca( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
