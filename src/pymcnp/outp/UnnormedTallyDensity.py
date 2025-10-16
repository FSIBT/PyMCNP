import re
import typing

from . import _block
from .. import types
from .. import errors


class UnnormedTallyDensity(_block.Block):
    """
    Represents `1unnormed tally density` blocks.

    Attributes:
        tally: Tally number.
        mean: Nonzero tally mean.
        nps: Tally nps.
        chart: Tally chart.
    """

    _REGEX = re.compile(
        r'\A1unnormed tally density for tally (.{10}) nonzero tally mean[(]m[)] = (.{9})   nps = (.{21}) print table 161\n\n'
        r' abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin[(]d=decade,slope= .{3}[)]\n'
        r'((?:.+\n)+  (?:total.+))\Z'
    )

    def __init__(
        self,
        tally: types.String,
        mean: types.String,
        nps: types.String,
        chart: types.String,
    ):
        """
        Initializes `UnnormedTallyDensity`.

        Parameters:
            tally: Tally number.
            mean: Nonzero tally mean.
            nps: Tally nps.
            chart: Tally chart.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if tally is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tally)
        if mean is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, mean)
        if nps is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps)
        if chart is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, chart)

        self.tally: typing.Final[types.String] = tally
        self.mean: typing.Final[types.String] = mean
        self.nps: typing.Final[types.String] = nps
        self.chart: typing.Final[types.String] = chart

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `UnnormedTallyDensity` from OUTP.

        Parameters:
            source: OUTP for `UnnormedTallyDensity`.

        Returns:
            `UnnormedTallyDensity`.
        """

        tokens = UnnormedTallyDensity._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        tally = types.String.from_mcnp(tokens[1])
        mean = types.String.from_mcnp(tokens[2])
        nps = types.String.from_mcnp(tokens[3])
        chart = types.String.from_mcnp(tokens[4])

        return UnnormedTallyDensity(
            tally,
            mean,
            nps,
            chart,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `UnnormedTallyDensity`.

        Returns:
            OUTP for `UnnormedTallyDensity`.
        """

        return f"""
1unnormed tally density for tally {self.tally:8} nonzero tally mean(m) = {self.mean:9}   nps = {self.nps:11} print table 161

 abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 0.0)
{self.chart}
"""[1:-1]
