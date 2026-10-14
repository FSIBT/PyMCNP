import re

from . import _field
from . import ds_2
from . import _card
from .. import types


class Ds_2(_field.Fields, _card.Card):
    """
    Represents INP `ds` elements variation #2.
    """

    _KEYWORD = 'ds'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    vss = _field.Field.tuple(ds_2.Variables, 'Dependent source independent & dependent variables', required=True, numeric=())

    _REGEX = re.compile(rf'\Ads(\d+) q((?: {ds_2.Variables._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `Ds_2`.

        Returns:
            INP for `Ds_2`.
        """
        return f'ds{self.suffix} q {self.vss}'
