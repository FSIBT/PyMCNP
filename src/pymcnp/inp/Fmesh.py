import re

from . import _field
from . import fmesh
from . import _card
from .. import types


class Fmesh(_field.Fields, _card.Card):
    """
    Represents INP `fmesh` cards.
    """

    _KEYWORD = 'fmesh'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value > 0 and value <= 999))
    designator = _field.Field(types.Designator, 'Data card particle designator', required=True, numeric=())
    options = _field.Field.tuple(fmesh.FmeshOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Afmesh(\d+):(\S+)((?: (?:{fmesh.FmeshOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
