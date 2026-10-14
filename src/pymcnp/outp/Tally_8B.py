import re

import pandas

from . import _block
from . import tally
from .. import types
from .. import errors
from .. import _fields


class Tally_8B(_fields.Fields, _block.Block):
    """
    Represents OUTP `1tally 8 nps` blocks.

    Attributes:
        number: Tally number.
        nps: Tally nps.
        tally_type: Tally type.
        particles: Tally particles.
        message: Tally modification message.
        subtallies: Subtallies.
        stats_desired: Statistical checks desired.
        stats_observed: Statistical checks observed.
        stats_passed: Statistical checks passed.
        fails: Number of failed statistics checks.
    """

    _REGEX = re.compile(
        r'\A1tally (.{8})        nps = (.{11})\n'
        r'           tally type (.+)\n'
        r'           particle[(]s[)]: (.+)(\n.*)?\n \n'
        rf'((?:{tally.Subtally_4._REGEX.pattern[2:-2]})+)\n'
        r' ===================================================================================================================================\n\n'
        r'           results of 10 statistical checks for the estimated answer for the tally fluctuation chart [(]tfc[)] bin of tally .{8}\n\n'
        r' tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-\n'
        r' behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope\n\n'
        r'( .+)\n'
        r'( .+)\n'
        r'( .+)\n\n'
        r' ===================================================================================================================================\n\n\n'
        r' warning[.]  the tally in the tally fluctuation chart bin did not pass (..) of the 10 statistical checks[.]\n\Z'
    )

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SEMANTICS_TABLE

    number = _fields.Field(types.String, 'Tally number')
    nps = _fields.Field(types.String, 'Tally nps')
    tally_type = _fields.Field(types.String, 'Tally type')
    particles = _fields.Field(types.String, 'Tally particles')
    message = _fields.Field(types.String, 'Tally modification message', nullable=True)
    subtallies = _fields.Field(types.Tuple(tally.Subtally_1), 'Subtallies')
    stats_desired = _fields.Field(types.String, 'Statistical checks desired')
    stats_observed = _fields.Field(types.String, 'Statistical checks observed')
    stats_passed = _fields.Field(types.String, 'Statistical checks passed')
    fails = _fields.Field(types.String, 'Number of failed statistics checks')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Tally_8B` from OUTP.

        Parameters:
            source: OUTP for `Tally_8B`.

        Returns:
            `Tally_8B`.
        """

        tokens = Tally_8B._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        number = types.String.from_mcnp(tokens[1])
        nps = types.String.from_mcnp(tokens[2])
        tally_type = types.String.from_mcnp(tokens[3])
        particles = types.String.from_mcnp(tokens[4])
        message = types.String.from_mcnp(tokens[5]) if tokens[5] else None
        subtallies = types.Tuple(tally.Subtally_4).from_mcnp(tokens[6])
        offset = tally.Subtally_4._REGEX.groups
        stats_desired = types.String.from_mcnp(tokens[7 + offset])
        stats_observed = types.String.from_mcnp(tokens[8 + offset])
        stats_passed = types.String.from_mcnp(tokens[9 + offset])
        fails = types.String.from_mcnp(tokens[10 + offset])

        return Tally_8B(
            number,
            nps,
            tally_type,
            particles,
            message,
            subtallies,
            stats_desired,
            stats_observed,
            stats_passed,
            fails,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Tally_8B`.

        Returns:
            OUTP for `Tally_8B`.
        """

        message = '\n           ' + str(self.message) + '\n' if self.message else ''

        return f"""
1tally {self.number}        nps = {self.nps}
           tally type {self.tally_type}
           particle(s): {self.particles}{message}
 
{''.join(map(str, self.subtallies))}
 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally {self.number}

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

{self.stats_desired}
{self.stats_observed}
{self.stats_passed}

 ===================================================================================================================================


 warning.  the tally in the tally fluctuation chart bin did not pass {self.fails} of the 10 statistical checks.
"""[1:]

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Tally_8B`.

        Returns:
            `pandas.DataFrame`.
        """

        df = pandas.concat((subtally.to_dataframe() for subtally in self.subtallies), ignore_index=True)
        df['number'] = self.number.value.strip()
        df['type'] = self.tally_type.value.strip()
        df['particles'] = self.particles.value.strip()
        df['nps'] = self.nps.value.strip()
        return df
