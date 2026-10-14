import re

from . import _field
from . import _card
from .. import types


class Fc(_field.Fields, _card.Card):
    """
    Represents INP `fc` cards.
    """

    _KEYWORD = 'fc'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    info = _field.Field(types.String, 'Title for tally in output and MCTAL file', required=True, numeric=())

    _REGEX = re.compile(r'\Afc(\d+)( [\S\s]+)\Z', re.IGNORECASE)
