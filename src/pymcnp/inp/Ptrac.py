import re

from . import _field
from . import ptrac
from . import _card


class Ptrac(_field.Fields, _card.Card):
    """
    Represents INP `ptrac` cards.
    """

    _KEYWORD = 'ptrac'

    options = _field.Field.tuple(ptrac.PtracOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Aptrac((?: (?:{ptrac.PtracOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
