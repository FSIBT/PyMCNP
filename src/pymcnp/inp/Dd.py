import re

from . import _field
from . import dd
from . import _card
from .. import types


class Dd(_field.Fields, _card.Card):
    """
    Represents INP dd cards.
    """

    _KEYWORD = 'dd'

    _ORDER = ('diagnostics', 'suffix')

    suffix = _field.Field(types.Integer, 'Data card option suffix', numeric=int)
    diagnostics = _field.Field.tuple(dd.Diagnostic, 'Detector diagnostic entries', required=True, numeric=())

    _REGEX = re.compile(rf'\Add(\d+)?((?: {dd.Diagnostic._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
