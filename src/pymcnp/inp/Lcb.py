import re

from . import _field
from . import _card
from .. import types


class Lcb(_field.Fields, _card.Card):
    """
    Represents INP `lcb` cards.
    """

    _KEYWORD = 'lcb'

    flenb1 = _field.Field(types.Real, 'Kinetic energy for nucleons CEM/Bertini/INCL')
    flenb2 = _field.Field(types.Real, 'Kinetic energy for nucleons LAQGSM03.03')
    flenb3 = _field.Field(types.Real, 'Kinetic energy for pions CEM/Bertini/INCL')
    flenb4 = _field.Field(types.Real, 'Kinetic energy for pions LAQGSM03.03')
    flenb5 = _field.Field(types.Real, 'Kinetic energy for nucleons ISABEL')
    flenb6 = _field.Field(types.Real, 'Kinetic energy for appropriate model')
    cotfe = _field.Field(types.Real, 'Cutoff kinetic energy for particle escape')
    film0 = _field.Field(types.Real, 'Maximum correction allowed for masss-energy balancing')

    _REGEX = re.compile(
        rf'\Alcb( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
