import re

from . import _field
from . import embee
from . import _card
from .. import types


class Embee(_field.Fields, _card.Card):
    """
    Represents INP `embee` cards.
    """

    _KEYWORD = 'embee'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    options = _field.Field.tuple(embee.EmbeeOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Aembee(\d+):(\S+)((?: (?:{embee.EmbeeOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
