import re


from . import _block
from . import _dataframe
from . import tally
from .. import types
from .. import errors
from .. import _fields


class Tally_1A(_fields.Fields, _dataframe.Dataframe, _block.Block):
    """
    Represents OUTP `1tally 1 nps` blocks.

    Attributes:
        number: Tally number.
        nps: Tally nps.
        tally_type: Tally type.
        particles: Tally particles.
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
        r'           particle[(]s[)]: (.+)\n'
        r' \n'
        rf'((?:{tally.Subtally_1._REGEX.pattern[2:-2]})+)\n'
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
    subtallies = _fields.Field(types.Tuple(tally.Subtally_1), 'Subtallies')
    stats_desired = _fields.Field(types.String, 'Statistical checks desired')
    stats_observed = _fields.Field(types.String, 'Statistical checks observed')
    stats_passed = _fields.Field(types.String, 'Statistical checks passed')
    asymmetric_interval = _fields.Field(types.String, 'Estimated asymmetric confidence interval')
    symmetric_interval = _fields.Field(types.String, 'Estimated symmetric condifence interval')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Tally_1A` from OUTP.

        Parameters:
            source: OUTP for `Tally_1A`.

        Returns:
            `Tally_1A`.
        """

        tokens = Tally_1A._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        number = types.String.from_mcnp(tokens[1])
        nps = types.String.from_mcnp(tokens[2])
        tally_type = types.String.from_mcnp(tokens[3])
        particles = types.String.from_mcnp(tokens[4])
        subtallies = types.Tuple(tally.Subtally_1).from_mcnp(tokens[5])
        offset = tally.Subtally_1._REGEX.groups
        stats_desired = types.String.from_mcnp(tokens[6 + offset])
        stats_observed = types.String.from_mcnp(tokens[7 + offset])
        stats_passed = types.String.from_mcnp(tokens[8 + offset])
        asymmetric_interval = types.String.from_mcnp(tokens[9 + offset])
        symmetric_interval = types.String.from_mcnp(tokens[10 + offset])

        return Tally_1A(
            number,
            nps,
            tally_type,
            particles,
            subtallies,
            stats_desired,
            stats_observed,
            stats_passed,
            asymmetric_interval,
            symmetric_interval,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Tally_1A`.

        Returns:
            OUTP for `Tally_1A`.
        """

        return f"""
1tally {self.number}        nps = {self.nps}
           tally type {self.tally_type}
           particle(s): {self.particles}
 
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

"""[1:-1]
