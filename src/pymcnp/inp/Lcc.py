import re

from . import _field
from . import _card
from .. import types


class Lcc(_field.Fields, _card.Card):
    """
    Represents INP `lcc` cards.
    """

    _KEYWORD = 'lcc'

    stincl = _field.Field(types.Real, 'Rescaling factor of the cascade duration')
    v0incl = _field.Field(types.Real, 'Potential depth')
    xfoisaincl = _field.Field(types.Real, 'Maximum impact parameter for Pauli blocking')
    npaulincl = _field.Field(types.Integer, 'Pauli blocking parameter setting', numeric=int, invalid=lambda self, value: value is not None and (not (value == 0 or value == -1 or value == 1)))
    nosurfincl = _field.Field(types.Integer, 'Difuse nuclear surface based on Wood-Saxon density setting', numeric=int, invalid=lambda self, value: value is not None and value not in {-2, -1, 0, 1})
    ecutincl = _field.Field(types.Real, 'Bertini model energy below this energy')
    ebankincl = _field.Field(types.Real, 'INCL bank particles below this energy')
    ebankabia = _field.Field(types.Real, 'ABLA bank particles below this energy')

    _REGEX = re.compile(
        rf'\Alcc( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
