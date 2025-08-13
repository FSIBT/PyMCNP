import re
import typing

from . import _block
from .. import types
from .. import errors


class AnalysisTallyFluctuation(_block.Block):
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

    def __init__(
        self,
        tally: types.String,
        nps: types.String,
        normed_average_per_history: types.String,
        unnormed_average_per_history: types.String,
        tally_relative_error: types.String,
        tally_variance_variance: types.String,
        relative_error_zero: types.String,
        relative_error_nonzero: types.String,
        number_nonzero: types.String,
        efficiency_nonzero: types.String,
        largest_history: types.String,
        largest_unormalized: types.String,
        largest_per_average: types.String,
        largest_per_verage_nonzero: types.String,
        confidence_per_mean: types.String,
        shifted_confidence: types.String,
        nps_mean: types.String,
        nps_plus_mean: types.String,
        nps_times_mean: types.String,
        nps_relative_error: types.String,
        nps_plus_relative_error: types.String,
        nps_times_relative_error: types.String,
        nps_variance_variance: types.String,
        nps_plus_variance_variance: types.String,
        nps_times_variance_variance: types.String,
        nps_shifted_center: types.String,
        nps_plus_shifted_center: types.String,
        nps_times_shifted_center: types.String,
        nps_merit: types.String,
        nps_plus_merit: types.String,
        nps_times_merit: types.String,
        message: types.String,
        histories_per_minute: types.String,
        singal_noise: types.String,
        singal_noise_squared: types.String,
        fom: types.String,
    ):
        """
        Initializes `AnalysisTallyFluctuation`.

        Parameters:
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

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if tally is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tally)
        if nps is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps)
        if normed_average_per_history is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, normed_average_per_history)
        if unnormed_average_per_history is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, unnormed_average_per_history)
        if tally_relative_error is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tally_relative_error)
        if tally_variance_variance is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tally_variance_variance)
        if relative_error_zero is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, relative_error_zero)
        if relative_error_nonzero is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, relative_error_nonzero)
        if number_nonzero is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, number_nonzero)
        if efficiency_nonzero is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, efficiency_nonzero)
        if largest_history is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, largest_history)
        if largest_unormalized is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, largest_unormalized)
        if largest_per_average is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, largest_per_average)
        if largest_per_verage_nonzero is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, largest_per_verage_nonzero)
        if confidence_per_mean is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, confidence_per_mean)
        if shifted_confidence is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, shifted_confidence)
        if nps_mean is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_mean)
        if nps_plus_mean is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_plus_mean)
        if nps_times_mean is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_times_mean)
        if nps_relative_error is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_relative_error)
        if nps_plus_relative_error is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_plus_relative_error)
        if nps_times_relative_error is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_times_relative_error)
        if nps_variance_variance is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_variance_variance)
        if nps_plus_variance_variance is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_plus_variance_variance)
        if nps_times_variance_variance is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_times_variance_variance)
        if nps_shifted_center is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_shifted_center)
        if nps_plus_shifted_center is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_plus_shifted_center)
        if nps_times_shifted_center is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_times_shifted_center)
        if nps_merit is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_merit)
        if nps_plus_merit is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_plus_merit)
        if nps_times_merit is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, nps_times_merit)
        if message is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, message)
        if histories_per_minute is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, histories_per_minute)
        if singal_noise is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, singal_noise)
        if singal_noise_squared is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, singal_noise_squared)
        if fom is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, fom)

        self.tally: typing.Final[types.String] = tally
        self.nps: typing.Final[types.String] = nps
        self.normed_average_per_history: typing.Final[types.String] = normed_average_per_history
        self.unnormed_average_per_history: typing.Final[types.String] = unnormed_average_per_history
        self.tally_relative_error: typing.Final[types.String] = tally_relative_error
        self.tally_variance_variance: typing.Final[types.String] = tally_variance_variance
        self.relative_error_zero: typing.Final[types.String] = relative_error_zero
        self.relative_error_nonzero: typing.Final[types.String] = relative_error_nonzero
        self.number_nonzero: typing.Final[types.String] = number_nonzero
        self.efficiency_nonzero: typing.Final[types.String] = efficiency_nonzero
        self.largest_history: typing.Final[types.String] = largest_history
        self.largest_unormalized: typing.Final[types.String] = largest_unormalized
        self.largest_per_average: typing.Final[types.String] = largest_per_average
        self.largest_per_verage_nonzero: typing.Final[types.String] = largest_per_verage_nonzero
        self.confidence_per_mean: typing.Final[types.String] = confidence_per_mean
        self.shifted_confidence: typing.Final[types.String] = shifted_confidence
        self.nps_mean: typing.Final[types.String] = nps_mean
        self.nps_plus_mean: typing.Final[types.String] = nps_plus_mean
        self.nps_times_mean: typing.Final[types.String] = nps_times_mean
        self.nps_relative_error: typing.Final[types.String] = nps_relative_error
        self.nps_plus_relative_error: typing.Final[types.String] = nps_plus_relative_error
        self.nps_times_relative_error: typing.Final[types.String] = nps_times_relative_error
        self.nps_variance_variance: typing.Final[types.String] = nps_variance_variance
        self.nps_plus_variance_variance: typing.Final[types.String] = nps_plus_variance_variance
        self.nps_times_variance_variance: typing.Final[types.String] = nps_times_variance_variance
        self.nps_shifted_center: typing.Final[types.String] = nps_shifted_center
        self.nps_plus_shifted_center: typing.Final[types.String] = nps_plus_shifted_center
        self.nps_times_shifted_center: typing.Final[types.String] = nps_times_shifted_center
        self.nps_merit: typing.Final[types.String] = nps_merit
        self.nps_plus_merit: typing.Final[types.String] = nps_plus_merit
        self.nps_times_merit: typing.Final[types.String] = nps_times_merit
        self.message: typing.Final[types.String] = message
        self.histories_per_minute: typing.Final[types.String] = histories_per_minute
        self.singal_noise: typing.Final[types.String] = singal_noise
        self.singal_noise_squared: typing.Final[types.String] = singal_noise_squared
        self.fom: typing.Final[types.String] = fom

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
