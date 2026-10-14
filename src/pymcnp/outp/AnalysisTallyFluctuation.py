import re

from . import _block
from .. import types
from .. import errors
from .. import _fields


class AnalysisTallyFluctuation(_fields.Fields, _block.Block):
    """
    Represents OUTP 160 tables.

    Attributes:
        tally: Tally number.
        nps: Tally nps.
        normed_average_per_history: Normed average tally per history.
        unnormed_average_per_history: Unnormed average tally per history.
        tally_relative_error: Estimated tally elative error.
        tally_variance_variance: Estimated variance of the variance.
        relative_error_zero: Relative error from zero tallies.
        relative_error_nonzero: Relative error from nonzero scroes.
        number_nonzero: Number of nonzero hsitory tallies.
        efficiency_nonzero: Efficiency for the nonzero tallies.
        largest_history: History number of largest tally.
        largest_unormalized: Largest unnormalized history tally.
        largest_per_average: Largest tally by average tally.
        largest_per_verage_nonzero: Largest tally by average nonzero tally.
        confidence_per_mean: Confidence interval shift by mean.
        shifted_confidence: Shifted confidence interval center.
        nps_mean: Mean at nps.
        nps_plus_mean: Mean at nps+1.
        nps_times_mean: Mean times nps+1/nps-1.
        nps_relative_error: Relative error nps.
        nps_plus_relative_error: Relative error nps+1.
        nps_times_relative_error: Relative error nps+1/nps-1.
        nps_variance_variance: Variance of the variance nps.
        nps_plus_variance_variance: Variance of the variance nps+1.
        nps_times_variance_variance: Variance of the variance nps+1/nps-1.
        nps_shifted_center: Shifted center nps.
        nps_plus_shifted_center: Shifted center nps+1.
        nps_times_shifted_center: Shifted center nps+1/nps-1.
        nps_merit: Figure of merit nps.
        nps_plus_merit: Figure of merit nps+1.
        nps_times_merit: Figure of merit nps+1/nps-1.
        message: Diagnostic message.
        histories_per_minute: Histories per minute.
        singal_noise: Signal-to-noise ratio.
        singal_noise_squared: Signal to-noise ratio squared.
        fom: Figure of merit.
    """

    _REGEX = re.compile(
        r'\A1analysis of the results in the tally fluctuation chart bin [(]tfc[)] for tally (.{1}) with nps = (.{19}) print table 160\n\n\n'
        r' normed average tally per history  = (.{11})          unnormed average tally per history  = (.{11})\n'
        r' estimated tally relative error    = (.{11})          estimated variance of the variance  = (.{6})\n'
        r' relative error from zero tallies  = (.{11})          relative error from nonzero scores  = (.{6})\n\n'
        r' number of nonzero history tallies = (.{11})          efficiency for the nonzero tallies  = (.{6})\n'
        r' history number of largest  tally  = (.{11})          largest  unnormalized history tally = (.{11})\n'
        r' [(]largest  tally[)]/[(]average tally[)]  = (.{11})          [(]largest  tally[)]/[(]avg nonzero tally[)]= (.{11})\n\n'
        r' [(]confidence interval shift[)]/mean  = (.{11})          shifted confidence interval center  = (.{11})\n\n\n'
        r' if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:\n\n'
        r'      estimated quantities           value at nps           value at nps[+]1           value[(]nps[+]1[)]/value[(]nps[)]-1[.]\n\n'
        r'      mean                            (.{11})             (.{11})                    (.{9})\n'
        r'      relative error                  (.{11})             (.{11})                    (.{9})\n'
        r'      variance of the variance        (.{11})             (.{11})                    (.{9})\n'
        r'      shifted center                  (.{11})             (.{11})                    (.{9})\n'
        r'      figure of merit                 (.{11})             (.{11})                    (.{9})\n\n'
        r'((?:.+\n)+)\n'
        r' fom = [(]histories/minute[)][*][(]f[(]x[)] signal-to-noise ratio[)][*][*]2 = [(](.{9})[)][*][(](.{10})[)][*][*]2 = [(].{9}[)][*][(](.{9})[)] = (.{9})\n\Z'
    )

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SEMANTICS_TABLE

    tally = _fields.Field(types.String, 'Tally number')
    nps = _fields.Field(types.String, 'Tally nps')
    normed_average_per_history = _fields.Field(types.String, 'Normed average tally per history')
    unnormed_average_per_history = _fields.Field(types.String, 'Unnormed average tally per history')
    tally_relative_error = _fields.Field(types.String, 'Estimated tally elative error')
    tally_variance_variance = _fields.Field(types.String, 'Estimated variance of the variance')
    relative_error_zero = _fields.Field(types.String, 'Relative error from zero tallies')
    relative_error_nonzero = _fields.Field(types.String, 'Relative error from nonzero scroes')
    number_nonzero = _fields.Field(types.String, 'Number of nonzero hsitory tallies')
    efficiency_nonzero = _fields.Field(types.String, 'Efficiency for the nonzero tallies')
    largest_history = _fields.Field(types.String, 'History number of largest tally')
    largest_unormalized = _fields.Field(types.String, 'Largest unnormalized history tally')
    largest_per_average = _fields.Field(types.String, 'Largest tally by average tally')
    largest_per_verage_nonzero = _fields.Field(types.String, 'Largest tally by average nonzero tally')
    confidence_per_mean = _fields.Field(types.String, 'Confidence interval shift by mean')
    shifted_confidence = _fields.Field(types.String, 'Shifted confidence interval center')
    nps_mean = _fields.Field(types.String, 'Mean at nps')
    nps_plus_mean = _fields.Field(types.String, 'Mean at nps+1')
    nps_times_mean = _fields.Field(types.String, 'Mean times nps+1/nps-1')
    nps_relative_error = _fields.Field(types.String, 'Relative error nps')
    nps_plus_relative_error = _fields.Field(types.String, 'Relative error nps+1')
    nps_times_relative_error = _fields.Field(types.String, 'Relative error nps+1/nps-1')
    nps_variance_variance = _fields.Field(types.String, 'Variance of the variance nps')
    nps_plus_variance_variance = _fields.Field(types.String, 'Variance of the variance nps+1')
    nps_times_variance_variance = _fields.Field(types.String, 'Variance of the variance nps+1/nps-1')
    nps_shifted_center = _fields.Field(types.String, 'Shifted center nps')
    nps_plus_shifted_center = _fields.Field(types.String, 'Shifted center nps+1')
    nps_times_shifted_center = _fields.Field(types.String, 'Shifted center nps+1/nps-1')
    nps_merit = _fields.Field(types.String, 'Figure of merit nps')
    nps_plus_merit = _fields.Field(types.String, 'Figure of merit nps+1')
    nps_times_merit = _fields.Field(types.String, 'Figure of merit nps+1/nps-1')
    message = _fields.Field(types.String, 'Diagnostic message')
    histories_per_minute = _fields.Field(types.String, 'Histories per minute')
    singal_noise = _fields.Field(types.String, 'Signal-to-noise ratio')
    singal_noise_squared = _fields.Field(types.String, 'Signal to-noise ratio squared')
    fom = _fields.Field(types.String, 'Figure of merit')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `AnalysisTallyFluctuation` from OUTP.

        Parameters:
            source: OUTP for `AnalysisTallyFluctuation`.

        Returns:
            `AnalysisTallyFluctuation`.
        """

        tokens = AnalysisTallyFluctuation._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        tally = types.String.from_mcnp(tokens[1])
        nps = types.String.from_mcnp(tokens[2])
        normed_average_per_history = types.String.from_mcnp(tokens[3])
        unnormed_average_per_history = types.String.from_mcnp(tokens[4])
        tally_relative_error = types.String.from_mcnp(tokens[5])
        tally_variance_variance = types.String.from_mcnp(tokens[6])
        relative_error_zero = types.String.from_mcnp(tokens[7])
        relative_error_nonzero = types.String.from_mcnp(tokens[8])
        number_nonzero = types.String.from_mcnp(tokens[9])
        efficiency_nonzero = types.String.from_mcnp(tokens[10])
        largest_history = types.String.from_mcnp(tokens[11])
        largest_unormalized = types.String.from_mcnp(tokens[12])
        largest_per_average = types.String.from_mcnp(tokens[13])
        largest_per_verage_nonzero = types.String.from_mcnp(tokens[14])
        confidence_per_mean = types.String.from_mcnp(tokens[15])
        shifted_confidence = types.String.from_mcnp(tokens[16])
        nps_mean = types.String.from_mcnp(tokens[17])
        nps_plus_mean = types.String.from_mcnp(tokens[18])
        nps_times_mean = types.String.from_mcnp(tokens[19])
        nps_relative_error = types.String.from_mcnp(tokens[20])
        nps_plus_relative_error = types.String.from_mcnp(tokens[21])
        nps_times_relative_error = types.String.from_mcnp(tokens[22])
        nps_variance_variance = types.String.from_mcnp(tokens[23])
        nps_plus_variance_variance = types.String.from_mcnp(tokens[24])
        nps_times_variance_variance = types.String.from_mcnp(tokens[25])
        nps_shifted_center = types.String.from_mcnp(tokens[26])
        nps_plus_shifted_center = types.String.from_mcnp(tokens[27])
        nps_times_shifted_center = types.String.from_mcnp(tokens[28])
        nps_merit = types.String.from_mcnp(tokens[29])
        nps_plus_merit = types.String.from_mcnp(tokens[30])
        nps_times_merit = types.String.from_mcnp(tokens[31])
        message = types.String.from_mcnp(tokens[32])
        histories_per_minute = types.String.from_mcnp(tokens[33])
        singal_noise = types.String.from_mcnp(tokens[34])
        singal_noise_squared = types.String.from_mcnp(tokens[35])
        fom = types.String.from_mcnp(tokens[36])

        return AnalysisTallyFluctuation(
            tally,
            nps,
            normed_average_per_history,
            unnormed_average_per_history,
            tally_relative_error,
            tally_variance_variance,
            relative_error_zero,
            relative_error_nonzero,
            number_nonzero,
            efficiency_nonzero,
            largest_history,
            largest_unormalized,
            largest_per_average,
            largest_per_verage_nonzero,
            confidence_per_mean,
            shifted_confidence,
            nps_mean,
            nps_plus_mean,
            nps_times_mean,
            nps_relative_error,
            nps_plus_relative_error,
            nps_times_relative_error,
            nps_variance_variance,
            nps_plus_variance_variance,
            nps_times_variance_variance,
            nps_shifted_center,
            nps_plus_shifted_center,
            nps_times_shifted_center,
            nps_merit,
            nps_plus_merit,
            nps_times_merit,
            message,
            histories_per_minute,
            singal_noise,
            singal_noise_squared,
            fom,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `AnalysisTallyFluctuation`.

        Returns:
            OUTP for `AnalysisTallyFluctuation`.
        """

        return f"""
1analysis of the results in the tally fluctuation chart bin (tfc) for tally {self.tally.value:1} with nps = {self.nps.value:19} print table 160


 normed average tally per history  = {self.normed_average_per_history.value:11}          unnormed average tally per history  = {self.unnormed_average_per_history.value:11}
 estimated tally relative error    = {self.tally_relative_error.value:11}          estimated variance of the variance  = {self.tally_variance_variance.value:6}
 relative error from zero tallies  = {self.relative_error_zero.value:11}          relative error from nonzero scores  = {self.relative_error_nonzero.value:6}

 number of nonzero history tallies = {self.number_nonzero.value:11}          efficiency for the nonzero tallies  = {self.efficiency_nonzero.value:6}
 history number of largest  tally  = {self.largest_history.value:11}          largest  unnormalized history tally = {self.largest_unormalized.value:11}
 (largest  tally)/(average tally)  = {self.largest_per_average.value:11}          (largest  tally)/(avg nonzero tally)= {self.largest_per_verage_nonzero.value:11}

 (confidence interval shift)/mean  = {self.confidence_per_mean.value:11}          shifted confidence interval center  = {self.shifted_confidence.value:11}


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            {self.nps_mean.value:11}             {self.nps_plus_mean.value:11}                    {self.nps_times_mean.value:8}
      relative error                  {self.nps_relative_error.value:11}             {self.nps_plus_relative_error.value:11}                    {self.nps_times_relative_error.value:8}
      variance of the variance        {self.nps_variance_variance.value:11}             {self.nps_plus_variance_variance.value:11}                    {self.nps_times_variance_variance.value:8}
      shifted center                  {self.nps_shifted_center.value:11}             {self.nps_plus_shifted_center.value:11}                    {self.nps_times_shifted_center.value:8}
      figure of merit                 {self.nps_merit.value:11}             {self.nps_plus_merit.value:11}                    {self.nps_times_merit.value:8}

{self.message}
 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = ({self.histories_per_minute.value:9})*({self.singal_noise.value:10})**2 = ({self.histories_per_minute.value:9})*({self.singal_noise_squared.value:9}) = {self.fom.value:9}
"""[1:]
