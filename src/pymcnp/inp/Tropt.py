import re

from . import _field
from . import tropt
from . import _card


class Tropt(_field.Fields, _card.Card):
    """
    Represents INP `tropt` cards.
    """

    _KEYWORD = 'tropt'

    options = _field.Field.tuple(tropt.TroptOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Atropt((?: (?:{tropt.TroptOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
