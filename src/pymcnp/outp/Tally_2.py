import re
import typing

import pandas

from . import _block
from . import tally
from .. import types
from .. import errors


class Tally_2(_block.Block):
    """
    Represents OUTP `1tally 2 nps` blocks.

    Attributes:
        number: Tally number.
        nps: Tally nps.
        tally_type: Tally type.
        particles: Tally particles.
        surface: Surface number.
        surface_value: Surface value.
        subtallies: Subtallies.
        stats_desired: Statistical checks desired.
        stats_observed: Statistical checks observed.
        stats_passed: Statistical checks passed.
        asymmetric_interval: Estimated asymmetric confidence interval.
        symmetric_interval: Estimated symmetric condifence interval.
    """

    _REGEX = re.compile(
        r'\A1tally (.{8})        nps = (.{11})\n'
        r'           tally type (.+)\n'
        r'           particle[(]s[)]: (.+)\n\n'
        r'           areas   \n'
        r'                surface: (.+)\n'
        r'                         (.+)\n \n'
        rf'((?:{tally.Subtally_2._REGEX.pattern[2:-2]})+)\n'
        r' ===================================================================================================================================\n\n'
        r'           results of 10 statistical checks for the estimated answer for the tally fluctuation chart [(]tfc[)] bin of tally .{8}\n\n'
        r' tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-\n'
        r' behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope\n\n'
        r'( .+)\n'
        r'( .+)\n'
        r'( .+)\n\n'
        r' ===================================================================================================================================\n\n\n'
        r' this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify[.]\n'
        r' the results in other bins associated with this tally may not meet these statistical criteria[.]\n\n'
        r' ----- estimated confidence intervals:  -----\n\n'
        r' estimated asymmetric confidence interval[(]1,2,3 sigma[)]: (.+)\n'
        r' estimated  symmetric confidence interval[(]1,2,3 sigma[)]: (.+)\n\Z'
    )

    def __init__(
        self,
        number: types.String,
        nps: types.String,
        tally_type: types.String,
        particles: types.String,
        surface: types.String,
        surface_value: types.String,
        subtallies: types.Tuple(tally.Subtally_1),
        stats_desired: types.String,
        stats_observed: types.String,
        stats_passed: types.String,
        asymmetric_interval: types.String,
        symmetric_interval: types.String,
    ):
        """
        Initializes `Tally_2`.

        Parameters:
            number: Tally number.
            nps: Tally nps.
            tally_type: Tally type.
            particles: Tally particles.
            surface: Surface number.
            surface_value: Surface value.
            subtallies: Subtallies.
            stats_desired: Statistical checks desired.
            stats_observed: Statistical checks observed.
            stats_passed: Statistical checks passed.
            asymmetric_interval: Estimated asymmetric confidence interval.
            symmetric_interval: Estimated symmetric condifence interval.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if number is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, number)
        if nps is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps)
        if tally_type is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tally_type)
        if particles is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, particles)
        if surface is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, surface)
        if surface_value is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, surface_value)
        if subtallies is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, subtallies)
        if stats_desired is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, stats_desired)
        if stats_observed is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, stats_observed)
        if stats_passed is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, stats_passed)
        if asymmetric_interval is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, asymmetric_interval)
        if symmetric_interval is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, symmetric_interval)

        self.number: typing.Final[types.String] = number
        self.nps: typing.Final[types.String] = nps
        self.tally_type: typing.Final[types.String] = tally_type
        self.particles: typing.Final[types.String] = particles
        self.surface: typing.Final[types.String] = surface
        self.surface_value: typing.Final[types.String] = surface_value
        self.subtallies: typing.Final[types.Tuple(tally.Subtally_1)] = subtallies
        self.stats_desired: typing.Final[types.String] = stats_desired
        self.stats_observed: typing.Final[types.String] = stats_observed
        self.stats_passed: typing.Final[types.String] = stats_passed
        self.asymmetric_interval: typing.Final[types.String] = asymmetric_interval
        self.symmetric_interval: typing.Final[types.String] = symmetric_interval

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Tally_2` from OUTP.

        Parameters:
            source: OUTP for `Tally_2`.

        Returns:
            `Tally_2`.
        """

        tokens = Tally_2._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        number = types.String.from_mcnp(tokens[1])
        nps = types.String.from_mcnp(tokens[2])
        tally_type = types.String.from_mcnp(tokens[3])
        particles = types.String.from_mcnp(tokens[4])
        surface = types.String.from_mcnp(tokens[5])
        surface_value = types.String.from_mcnp(tokens[6])
        subtallies = types.Tuple(tally.Subtally_2).from_mcnp(tokens[7])
        offset = tally.Subtally_2._REGEX.groups
        stats_desired = types.String.from_mcnp(tokens[8 + offset])
        stats_observed = types.String.from_mcnp(tokens[9 + offset])
        stats_passed = types.String.from_mcnp(tokens[10 + offset])
        asymmetric_interval = types.String.from_mcnp(tokens[11 + offset])
        symmetric_interval = types.String.from_mcnp(tokens[12 + offset])

        return Tally_2(
            number,
            nps,
            tally_type,
            particles,
            surface,
            surface_value,
            subtallies,
            stats_desired,
            stats_observed,
            stats_passed,
            asymmetric_interval,
            symmetric_interval,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Tally_2`.

        Returns:
            OUTP for `Tally_2`.
        """

        return f"""
1tally {self.number}        nps = {self.nps}
           tally type {self.tally_type}
           particle(s): {self.particles}

           areas   
                surface: {self.surface}
                         {self.surface_value}
 
{''.join(map(str, self.subtallies))}
 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally {self.number}

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

{self.stats_desired}
{self.stats_observed}
{self.stats_passed}

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): {self.asymmetric_interval}
 estimated  symmetric confidence interval(1,2,3 sigma): {self.symmetric_interval}
"""[1:]

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Tally_2`.

        Returns:
            `pandas.DataFrame`.
        """

        df = pandas.concat((subtally.to_dataframe() for subtally in self.subtallies), ignore_index=True)
        df['number'] = self.number.value.strip()
        df['type'] = self.tally_type.value.strip()
        df['particles'] = self.particles.value.strip()
        df['nps'] = self.nps.value.strip()
        return df
