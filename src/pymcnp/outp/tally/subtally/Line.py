import re
import typing

import pandas

from . import _subblock
from .... import types
from .... import errors


class Line(_subblock.LineSubblock):
    """
    Represents OUTP `1tally 1 nps` subtally.

    Attributes:
        bucket: Tally bucket.
        count: Tally count.
        error: Tally count error.
    """

    _REGEX = re.compile(r'\A    (\S+)   (\S+) (\S+)\n\Z', re.IGNORECASE)

    def __init__(
        self,
        bucket: types.String,
        count: types.String,
        error: types.String,
    ):
        """
        Initializes `Line`.

        Parameters:
            bucket: Tally bucket.
            count: Tally count.
            error: Tally count error.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if bucket is None:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, bucket)
        if count is None:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, count)
        if error is None:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, error)

        self.bucket: typing.Final[types.String] = bucket
        self.count: typing.Final[types.String] = count
        self.error: typing.Final[types.String] = error

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
