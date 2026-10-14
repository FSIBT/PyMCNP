import re

import pandas

from . import _block
from . import tally
from .. import types
from .. import errors
from .. import _fields


class Tally_2(_fields.Fields, _block.Block):
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

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SEMANTICS_TABLE

    number = _fields.Field(types.String, 'Tally number')
    nps = _fields.Field(types.String, 'Tally nps')
    tally_type = _fields.Field(types.String, 'Tally type')
    particles = _fields.Field(types.String, 'Tally particles')
    surface = _fields.Field(types.String, 'Surface number')
    surface_value = _fields.Field(types.String, 'Surface value')
    subtallies = _fields.Field(types.Tuple(tally.Subtally_1), 'Subtallies')
    stats_desired = _fields.Field(types.String, 'Statistical checks desired')
    stats_observed = _fields.Field(types.String, 'Statistical checks observed')
    stats_passed = _fields.Field(types.String, 'Statistical checks passed')
    asymmetric_interval = _fields.Field(types.String, 'Estimated asymmetric confidence interval')
    symmetric_interval = _fields.Field(types.String, 'Estimated symmetric condifence interval')

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
