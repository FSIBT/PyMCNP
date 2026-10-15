import re

from . import _field
from . import f_1
from . import _card
from .. import types


class F_1(_field.Fields, _card.Card):
    """
    Represents INP `f` elements variation #1.
    """

    _KEYWORD = 'f'

    _ORDER = ('suffix', 'spheres', 'prefix', 'designator', 'nd')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value <= 99999999 and value % 10 == 5))
    designator = _field.Field(types.Designator, 'Data card particle designator', numeric=())
    spheres = _field.Field.tuple(f_1.Sphere, 'Detector points', required=True, numeric=())
    nd = _field.Field(types.String, 'Total/average specified surfaces/cells option', numeric=(), invalid=lambda self, value: value is not None and value != 'nd')

    _REGEX = re.compile(r'\A([*+])?f(\d*[5])(?::(\S+))?((?: \S+ \S+ \S+ \S+)+?)( nd)?\Z', re.IGNORECASE)
