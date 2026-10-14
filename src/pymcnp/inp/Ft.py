import re

from . import _field
from . import _card
from .. import types


class Ft(_field.Fields, _card.Card):
    """
    Represents INP `ft` cards.
    """

    _KEYWORD = 'ft'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    treatments = _field.Field(types.String, 'Tally special treatments', required=True, numeric=())

    _REGEX = re.compile(r'\Aft(\d+)( [\S\s]+)\Z', re.IGNORECASE)
