import re

from . import _field
from . import mplot
from . import _card


class Mplot(_field.Fields, _card.Card):
    """
    Represents INP `mplot` cards.
    """

    _KEYWORD = 'mplot'

    options = _field.Field.tuple(mplot.MplotOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Amplot((?: (?:{mplot.MplotOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
