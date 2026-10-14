import re

from . import _field
from . import rand
from . import _card


class Rand(_field.Fields, _card.Card):
    """
    Represents INP `rand` cards.
    """

    _KEYWORD = 'rand'

    options = _field.Field.tuple(rand.RandOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Arand((?: (?:{rand.RandOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
