import re

from . import _field
from . import pert
from . import _card
from .. import types


class Pert(_field.Fields, _card.Card):
    """
    Represents INP `pert` cards.
    """

    _KEYWORD = 'pert'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    options = _field.Field.tuple(pert.PertOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Apert(\d+):(\S+)((?: (?:{pert.PertOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
