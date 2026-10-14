import re

from . import _field
from . import ds_1
from . import _card
from .. import types


class Ds_1(_field.Fields, _card.Card):
    """
    Represents INP `ds` elements variation #1.
    """

    _KEYWORD = 'ds'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    ijs = _field.Field.tuple(ds_1.Variables, 'Dependent source independent & dependent variables', required=True, numeric=())

    _REGEX = re.compile(rf'\Ads(\d+) t((?: {ds_1.Variables._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `Ds_1`.

        Returns:
            INP for `Ds_1`.
        """
        return f'ds{self.suffix} t {self.ijs}'
