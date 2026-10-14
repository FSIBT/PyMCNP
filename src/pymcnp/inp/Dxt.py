import re

from . import _field
from . import dxt
from . import _card
from .. import types


class Dxt(_field.Fields, _card.Card):
    """
    Represents INP `dxt` cards.
    """

    _KEYWORD = 'dxt'

    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    spheres_1 = _field.Field(dxt.Shell, 'DXTRAN spheres #1', required=True, numeric=())
    spheres_2 = _field.Field(dxt.Shell, 'DXTRAN spheres #2', required=True, numeric=())
    spheres_3 = _field.Field(dxt.Shell, 'DXTRAN spheres #3', required=True, numeric=())
    spheres_4 = _field.Field(dxt.Shell, 'DXTRAN spheres #4', required=True, numeric=())
    spheres_5 = _field.Field(dxt.Shell, 'DXTRAN spheres #5', required=True, numeric=())
    spheres_6 = _field.Field(dxt.Shell, 'DXTRAN spheres #6', required=True, numeric=())
    spheres_7 = _field.Field(dxt.Shell, 'DXTRAN spheres #7', required=True, numeric=())
    spheres_8 = _field.Field(dxt.Shell, 'DXTRAN spheres #8', required=True, numeric=())
    spheres_9 = _field.Field(dxt.Shell, 'DXTRAN spheres #9', required=True, numeric=())
    spheres_10 = _field.Field(dxt.Shell, 'DXTRAN spheres #10', required=True, numeric=())
    cutoff_1 = _field.Field(types.Real, 'Upper weight cutoff in the spheres', required=True)
    cutoff_2 = _field.Field(types.Real, 'Lower weight cutoff in the spheres', required=True)
    weight = _field.Field(types.Real, 'Minimum photon weight', required=True)

    _REGEX = re.compile(
        rf'\Adxt:(\S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
