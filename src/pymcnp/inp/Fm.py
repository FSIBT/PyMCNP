import re

from . import _field
from . import _card
from .. import types


class Fm(_field.Fields, _card.Card):
    """
    Represents INP `fm` cards.
    """

    _KEYWORD = 'fm'

    _ORDER = ('suffix', 'bins', 'prefix')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    bins = _field.Field(types.String, 'Tally multiplier bins', required=True, numeric=())

    _REGEX = re.compile(r'\A([+*])?fm(\d+)( [\S\s]+)\Z', re.IGNORECASE)
