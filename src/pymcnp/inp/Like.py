import re

from . import _field
from . import like
from . import _card
from .. import types


class Like(_field.Fields, _card.Card):
    """
    Represents INP cell cards.
    """

    number = _field.Field(types.Integer, 'Cell number', required=True, numeric=int, invalid=lambda self, value: not 1 <= value <= 99999999)
    cell = _field.Field(types.Integer, 'Base cell number', required=True, numeric=int, invalid=lambda self, value: not 1 <= value <= 99999999)
    options = _field.Field.tuple(like.LikeOption, 'Cell options', numeric=())

    _REGEX = re.compile(rf'\A(\S+) like (\S+) but((?: (?:{like.LikeOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `Like`.

        Returns:
            INP cell card.
        """

        source = f'{self.number} like {self.cell} but {self.options if self.options is not None else ""}'
        source = _card.Card._postprocess(source)

        return source
