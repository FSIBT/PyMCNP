import re

from . import _field
from . import _card
from .. import types


class Phys_0(_field.Fields, _card.Card):
    """
    Represents INP `phys` elements variation #0.
    """

    _KEYWORD = 'phys:n'

    emax = _field.Field(types.Real, 'Upper limit for neutron energy')
    emcnf = _field.Field(types.Real, 'Analog energy limit')
    iunr = _field.Field(types.Integer, 'Unresolved resonanace controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1})))
    coilf = _field.Field(types.Real, 'Light-ion and heavy-ion recoil and NCIA control')
    cutn = _field.Field(types.Integer, 'Table-based physics cutoff controls', numeric=int)
    ngam = _field.Field(
        types.Integer, 'Secondary photon production controls', numeric=int, invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {0, 1, 2}))
    )
    i_int_model = _field.Field(
        types.Integer,
        'Treataement of nuclear interactions controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0, 1, 2, 3})),
    )
    i_els_model = _field.Field(
        types.Integer,
        'Treatment of nuclear elastic scattering controls',
        numeric=int,
        invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value in {-1, 0, 1})),
    )

    _REGEX = re.compile(
        rf'\Aphys:n( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
