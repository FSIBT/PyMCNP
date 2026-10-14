import re

from . import _field
from . import _card
from .. import types


class Comment(_field.Fields, _card.Card):
    """
    Represents INP comment cards.
    """

    text = _field.Field(types.String, 'Comment text', numeric=())

    _REGEX = re.compile(r'\Ac(?: (.*))?\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `Comment`.

        Returns:
            INP comment card.
        """

        source = f'c{f" {self.text}" if self.text else ""}'
        source = _card.Card._postprocess(source)

        return source
