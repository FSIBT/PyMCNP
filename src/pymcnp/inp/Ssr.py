import re

from . import _field
from . import ssr
from . import _card


class Ssr(_field.Fields, _card.Card):
    """
    Represents INP `ssr` cards.
    """

    _KEYWORD = 'ssr'

    options = _field.Field.tuple(ssr.SsrOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Assr((?: (?:{ssr.SsrOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
