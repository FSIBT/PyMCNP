import re

from . import _field
from . import embed
from . import _card
from .. import types


class Embed(_field.Fields, _card.Card):
    """
    Represents INP `embed` cards.
    """

    _KEYWORD = 'embed'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    options = _field.Field.tuple(embed.EmbedOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Aembed(\d+)?((?: (?:{embed.EmbedOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
