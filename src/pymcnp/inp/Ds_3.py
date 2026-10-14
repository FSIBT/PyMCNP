import re

from . import _field
from . import _card
from .. import types


class Ds_3(_field.Fields, _card.Card):
    """
    Represents INP `ds` elements variation #3.
    """

    _KEYWORD = 'ds'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value >= 1 and value <= 999))
    distributions = _field.Field.tuple(types.Distribution, 'Distribution numbers', required=True, numeric=())

    _REGEX = re.compile(rf'\Ads(\d+) s((?: {types.Distribution._REGEX.pattern[2:-2]})+)\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `Ds_3`.

        Returns:
            INP for `Ds_3`.
        """
        return f'ds{self.suffix} s {self.distributions}'
