import re

from . import _field
from . import act
from . import _card


class Act(_field.Fields, _card.Card):
    """
    Represents INP act cards.
    """

    _KEYWORD = 'act'

    options = _field.Field.tuple(act.ActOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Aact((?: (?:{act.ActOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
