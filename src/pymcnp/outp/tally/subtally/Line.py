import re

import pandas

from . import _subblock
from .... import types
from .... import errors
from .... import _fields


class Line(_fields.Fields, _subblock.LineSubblock):
    """
    Represents OUTP `1tally 1 nps` subtally.

    Attributes:
        bucket: Tally bucket.
        count: Tally count.
        error: Tally count error.
    """

    _REGEX = re.compile(r'\A    (\S+)   (\S+) (\S+)\n\Z', re.IGNORECASE)

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SYNTAX_TABLE

    bucket = _fields.Field(types.String, 'Tally bucket')
    count = _fields.Field(types.String, 'Tally count')
    error = _fields.Field(types.String, 'Tally count error')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Line` from OUTP.

        Parameters:
            source: OUTP for `Line`.

        Returns:
            `Line`.
        """

        tokens = Line._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        bucket = types.String.from_mcnp(tokens[1])
        count = types.String.from_mcnp(tokens[2])
        error = types.String.from_mcnp(tokens[3])

        return Line(
            bucket,
            count,
            error,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Line`.

        Returns:
            OUTP for `Line`.
        """

        return f'    {self.bucket}   {self.count} {self.error}\n'

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Line`.

        Returns:
            `pandas.DataFrame`.
        """

        return pandas.DataFrame(
            {
                'bins': [float(self.bucket.value)],
                'counts': [float(self.count.value)],
                'errors': [float(self.error.value)],
            }
        )
