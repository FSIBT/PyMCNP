import re

from . import _field
from . import bfld
from . import _card
from .. import types


class Bfld(_field.Fields, _card.Card):
    """
    Represents INP bfld cards.
    """

    _KEYWORD = 'bfld'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    kind = _field.Field(types.String, 'Magnetic field type', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'const', 'quad', 'quadff'})
    options = _field.Field.tuple(bfld.BfldOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Abfld(\d+)( {types.String._REGEX.pattern[2:-2]})((?: (?:{bfld.BfldOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
