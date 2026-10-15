import re

from . import _field
from . import _card
from .. import types


class Fip(_field.Fields, _card.Card):
    """
    Represents INP `fip` cards.
    """

    _KEYWORD = 'fip'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value <= 99999999 and value % 10 == 5))
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    x1 = _field.Field(types.Real, 'Pinhole center x-coordinate', required=True)
    y1 = _field.Field(types.Real, 'Pinhole center y-coordinate', required=True)
    z1 = _field.Field(types.Real, 'Pinhole center z-coordinate', required=True)
    ro = _field.Field(types.Real, 'Pinhole exclusion radius', required=True, invalid=lambda self, value: value != 0)
    x2 = _field.Field(types.Real, 'Reference direction x-coordinate', required=True)
    y2 = _field.Field(types.Real, 'Reference direction y-coordinate', required=True)
    z2 = _field.Field(types.Real, 'Reference direction z-coordinate', required=True)
    f1 = _field.Field(types.Real, 'Cylindrical collimator radius', required=True, invalid=lambda self, value: not value >= 0)
    f2 = _field.Field(types.Real, 'Pinhole radius in the direction perpendiuclar to the reference direction', required=True, invalid=lambda self, value: not value >= 0)
    f3 = _field.Field(types.Real, 'Distance between pinhole and and detector grid', required=True, invalid=lambda self, value: not value >= 0)

    _REGEX = re.compile(
        rf'\Afip(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
