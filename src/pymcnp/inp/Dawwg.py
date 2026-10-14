import re

from . import _field
from . import dawwg
from . import _card


class Dawwg(_field.Fields, _card.Card):
    """
    Represents INP dawwg cards.
    """

    _KEYWORD = 'dawwg'

    options = _field.Field.tuple(dawwg.DawwgOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Adawwg((?: (?:{dawwg.DawwgOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
