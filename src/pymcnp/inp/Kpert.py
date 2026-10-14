import re

from . import _field
from . import kpert
from . import _card
from .. import types


class Kpert(_field.Fields, _card.Card):
    """
    Represents INP `kpert` cards.
    """

    _KEYWORD = 'kpert'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value > 0 and value <= 10000))
    options = _field.Field.tuple(kpert.KpertOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Akpert(\d+)((?: (?:{kpert.KpertOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
