import re

from . import _field
from . import ksen
from . import _card
from .. import types


class Ksen(_field.Fields, _card.Card):
    """
    Represents INP `ksen` cards.
    """

    _KEYWORD = 'ksen'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value > 0 and value <= 999))
    sen = _field.Field(types.String, 'Type of sensitivity', required=True, numeric=())
    options = _field.Field.tuple(ksen.KsenOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Aksen(\d+)( {types.String._REGEX.pattern[2:-2]})((?: (?:{ksen.KsenOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
