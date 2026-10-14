import re

from . import _field
from . import sdef
from . import _card


class Sdef(_field.Fields, _card.Card):
    """
    Represents INP `sdef` cards.
    """

    _KEYWORD = 'sdef'

    options = _field.Field.tuple(sdef.SdefOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Asdef((?: (?:{sdef.SdefOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
