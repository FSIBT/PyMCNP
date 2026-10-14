import re

from . import _field
from . import var
from . import _card


class Var(_field.Fields, _card.Card):
    """
    Represents INP `var` cards.
    """

    _KEYWORD = 'var'

    options = _field.Field.tuple(var.VarOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Avar((?: (?:{var.VarOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
