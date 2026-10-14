import re

from . import _field
from . import kopts
from . import _card


class Kopts(_field.Fields, _card.Card):
    """
    Represents INP `kopts` cards.
    """

    _KEYWORD = 'kopts'

    options = _field.Field.tuple(kopts.KoptsOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Akopts((?: (?:{kopts.KoptsOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
