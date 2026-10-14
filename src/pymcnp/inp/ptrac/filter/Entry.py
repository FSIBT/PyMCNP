import re

from ... import _field
from . import _entry
from .... import types


class Entry(_field.Fields, _entry.FilterEntry):
    """
    Represents INP `entry` elements.
    """

    _KEYWORD = ''

    _ORDER = ('lower', 'upper', 'variable')

    lower = _field.Field(types.Real, 'Lower bound for filtering', required=True)
    variable = _field.Field(types.String, 'Variable name for PBL derived structure', numeric=())
    upper = _field.Field(types.Real, 'Upper bound for filtering', required=True)

    _REGEX = re.compile(r'\A([^\s,]+),([^\s,]+)(?:,([^\s,]+))?\Z', re.IGNORECASE)

    def to_mcnp(self):
        """
        Generates INP from `Entry`.

        Returns:
            INP for `Entry`.
        """

        return f'{self.lower},{self.variable}{f",{self.upper}" if self.upper is not None else ""}'
