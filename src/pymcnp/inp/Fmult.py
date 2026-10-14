import re

from . import _field
from . import fmult
from . import _card
from .. import types


class Fmult(_field.Fields, _card.Card):
    """
    Represents INP `fmult` cards.
    """

    _KEYWORD = 'fmult'

    zaid = _field.Field(types.Zaid, 'Nuclide for which data are entered', required=True, numeric=())
    options = _field.Field.tuple(fmult.FmultOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Afmult( {types.Zaid._REGEX.pattern[2:-2]})((?: (?:{fmult.FmultOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
