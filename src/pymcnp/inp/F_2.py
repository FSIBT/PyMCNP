import re

from . import _field
from . import f_2
from . import _card
from .. import types


class F_2(_field.Fields, _card.Card):
    """
    Represents INP `f` elements variation #2.
    """

    _KEYWORD = 'f'

    _ORDER = ('suffix', 'a', 'rings', 'prefix', 'designator', 'nd')

    prefix = _field.Field(types.String, 'Star prefix', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not (value <= 99999999 and value % 10 == 5))
    a = _field.Field(types.String, 'Letter', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'x', 'y', 'z'})
    designator = _field.Field(types.Designator, 'Data card particle designator', numeric=())
    rings = _field.Field.tuple(f_2.Ring, 'Detector points', required=True, numeric=())
    nd = _field.Field(types.String, 'Total/average specified surfaces/cells option', numeric=(), invalid=lambda self, value: value is not None and value != 'nd')

    _REGEX = re.compile(r'\A([*+])?f(\d*[5])([xyz])(?::(\S+))?((?: \S+ \S+ \S+)+?)( nd)?\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `F_2`.

        Returns:
            INP for `F_2`.
        """

        return f'{self.prefix if self.prefix is not None else ""}f{self.suffix}{self.a}{f":{self.designator}" if self.designator is not None else ""} {self.rings} {self.nd if self.nd is not None else ""}'
