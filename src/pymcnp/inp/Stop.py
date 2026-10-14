import re

from . import _field
from . import stop
from . import _card


class Stop(_field.Fields, _card.Card):
    """
    Represents INP `stop` cards.
    """

    _KEYWORD = 'stop'

    options = _field.Field.tuple(stop.StopOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Astop((?: (?:{stop.StopOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
