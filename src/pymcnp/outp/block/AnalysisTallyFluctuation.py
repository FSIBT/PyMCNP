import typing
import dataclasses

from ... import abc
from ..Block import Block


class AnalysisTallyFluctuation(Block):
    """
    Represents analysistally fluctuation blocks.

    Attributes:
        name: analysis tally fluctuation block `1analysis of the results in the tally fluctuation chart bin (tfc)` symbol.
        tally_preamble: analysis tally fluctuation block `for tally ` symbol.
        tally: analysis tally fluctuation block tally.
        nps_preamble: analysis tally fluctuation block ` with nps = ` symbol.
        nps: analysis tally fluctuation block nps.
        print_preamble: analysis tally fluctuation block ` print table ` symbol.
        print: analysis tally fluctuation block `160` symbol.
        normed_average_tally_per_history_preamble: analysis tally fluctuation block `\\n\\n\\n normed average tally per history  = ` symbol.
        normed_average_tally_per_history: analysis tally fluctuation block normed average tally per history.
        unnormed_average_tally_per_history_preamble: analysis tally fluctuation block `          unnormed average tally per history  = ` symbol.
        unnormed_average_tally_per_history: analysis tally fluctuation block unnormed average tally per history.
        estimated_tally_relative_error_preamble: analysis tally fluctuation block `\\n estimated tally relative error    = ` symbol.
        estimated_tally_relative_error: analysis tally fluctuation block estimated tally relative error.
        estimated_variance_variance_preamble: analysis tally fluctuation block `          estimated variance of the variance  = ` symbol.
        estimated_variance_variance: analysis tally fluctuation block estimated variance variance.
        relative_error_zero_tallies_preamble: analysis tally fluctuation block `\\n relative error from zero tallies  = ` symbol.
        relative_error_zero_tallies: analysis tally fluctuation block relative error zero tallies.
        relative_error_nonzero_scores_preamble: analysis tally fluctuation block `          relative error from nonzero scores  = ` symbol.
        relative_error_nonzero_scores: analysis tally fluctuation block relative error nonzero scores.
        number_nonzero_history_tallies_preamble: analysis tally fluctuation block `\\n\\n number of nonzero history tallies = ` symbol.
        number_nonzero_history_tallies: analysis tally fluctuation block number nonzero history tallies.
        efficiency_nonzero_tallies_preamble: analysis tally fluctuation block `          efficiency for the nonzero tallies  = ` symbol.
        efficiency_nonzero_tallies: analysis tally fluctuation block efficiency nonzero tallies.
        history_number_largest_tally_preamble: analysis tally fluctuation block history number largest tally preamble.
        history_number_largest_tally: analysis tally fluctuation block history number largest tally.
        largest_unnormalized_history_tally_preamble: analysis tally fluctuation block `          largest  unnormalized history tally = ` symbol.
        largest_unnormalized_history_tally: analysis tally fluctuation block largest unnormalized history tally.
        largest_tally_per_average_tally_preamble: analysis tally fluctuation block `\\n (largest  tally[` symbol.
        largest_tally_per_average_tally: analysis tally fluctuation block largest tally per average tally.
        largest_tally_per_average_nonzero_tally_preamble: analysis tally fluctuation block `          (largest  tally)` symbol.
        largest_tally_per_average_nonzero_tally: analysis tally fluctuation block largest tally per average nonzero tally.
        confidence_interval_shift_per_mean_preamble: analysis tally fluctuation block `\n\n (confidence interval shift)` symbol.
        confidence_interval_shift_per_mean: analysis tally fluctuation block confidence interval shift per mean.
        shifted_confidence_interval_center_preamble: analysis tally fluctuation block `          shifted confidence interval center  = ` symbol.
        shifted_confidence_interval_center: analysis tally fluctuation block shifted confidence interval center.
        table_preamble: analysis tally fluctuation block `\\n\\n\\n if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:` symbol.
        table_heading: analysis tally fluctuation block `\\n\\n      estimated quantities           value at nps           value at nps+1           value(nps+1)` symbol.
        table_mean_preamble: analysis tally fluctuation block `\\n\\n      mean` symbol.
        table_mean_nps: analysis tally fluctuation block table mean nps.
        table_mean_nps_plus: analysis tally fluctuation block table mean nps plus.
        table_mean_nps_times: analysis tally fluctuation block table mean nps times.
        table_relative_error_preamble: analysis tally fluctuation block `\\n      relative error` symbol.
        table_relative_error: analysis tally fluctuation block table relative error.
        table_relative_error_plus: analysis tally fluctuation block table relative error plus.
        table_relative_error_times: analysis tally fluctuation block table relative error times.
        table_variance_variance_preamble: analysis tally fluctuation block `\\n      variance of the variance` symbol.
        table_variance_variance: analysis tally fluctuation block table variance variance.
        table_variance_variance_plus: analysis tally fluctuation block table variance variance plus.
        table_variance_variance_times: analysis tally fluctuation block table variance variance times.
        table_shifted_center_preamble: analysis tally fluctuation block `\\n      shifted center` symbol.
        table_shifted_center: analysis tally fluctuation block table shifted center.
        table_shifted_center_plus: analysis tally fluctuation block table shifted center plus.
        table_shifted_center_times: analysis tally fluctuation block table shifted center times.
        table_figure_merit_preamble: analysis tally fluctuation block `\\n      figure of merit` symbol.
        table_figure_merit: analysis tally fluctuation block table figure of merit.
        table_figure_merit_plus: analysis tally fluctuation block table figure of merit plus.
        table_figure_merit_times: analysis tally fluctuation block table figure of merit times.
        message_preamble: analysis tally fluctuation block `\\n\\n` symbol.
        message: analysis tally fluctuation block message.
        figure_merit_preamble: analysis tally fluctuation block `\\n fom = (histories/minute)` symbol.
        figure_merit: analysis tally fluctuation block figure of merit.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[
        abc.Terminal,
        r'\n1analysis of the results in the tally fluctuation chart bin \(tfc\) ',
    ] = abc.Terminal[r'1analysis of the results in the tally fluctuation chart bin \(tfc\) ']('1analysis of the results in the tally fluctuation chart bin (tfc) ')
    tally_preamble: typing.Annotated[abc.Terminal, r'for tally '] = abc.Terminal[r'for tally ']('for tally ')
    tally: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r' with nps = '] = abc.Terminal[r' with nps = '](' with nps = ')
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    print_preamble: typing.Annotated[abc.Terminal, r'  print table '] = abc.Terminal[r'  print table ']('  print table ')
    print: typing.Annotated[abc.Terminal, r'160'] = abc.Terminal[r'160']('160')
    normed_average_tally_per_history_preamble: typing.Annotated[abc.Terminal, r'\n\n\n normed average tally per history  = '] = abc.Terminal[r'\n\n\n normed average tally per history  = '](
        '\n\n\n normed average tally per history  = '
    )
    normed_average_tally_per_history: typing.Annotated[abc.Terminal, r'.{11}']
    unnormed_average_tally_per_history_preamble: typing.Annotated[abc.Terminal, r'          unnormed average tally per history  = '] = abc.Terminal[
        r'          unnormed average tally per history  = '
    ]('          unnormed average tally per history  = ')
    unnormed_average_tally_per_history: typing.Annotated[abc.Terminal, r'.{11}']
    estimated_tally_relative_error_preamble: typing.Annotated[abc.Terminal, r'\n estimated tally relative error    = '] = abc.Terminal[r'\n estimated tally relative error    = '](
        '\n estimated tally relative error    = '
    )
    estimated_tally_relative_error: typing.Annotated[abc.Terminal, r'.{11}']
    estimated_variance_variance_preamble: typing.Annotated[abc.Terminal, r'          estimated variance of the variance  = '] = abc.Terminal[r'          estimated variance of the variance  = '](
        '          estimated variance of the variance  = '
    )
    estimated_variance_variance: typing.Annotated[abc.Terminal, r'.{6}']
    relative_error_zero_tallies_preamble: typing.Annotated[abc.Terminal, r'\n relative error from zero tallies  = '] = abc.Terminal[r'\n relative error from zero tallies  = '](
        '\n relative error from zero tallies  = '
    )
    relative_error_zero_tallies: typing.Annotated[abc.Terminal, r'.{11}']
    relative_error_nonzero_scores_preamble: typing.Annotated[abc.Terminal, r'          relative error from nonzero scores  = '] = abc.Terminal[r'          relative error from nonzero scores  = '](
        '          relative error from nonzero scores  = '
    )
    relative_error_nonzero_scores: typing.Annotated[abc.Terminal, r'.{6}']
    number_nonzero_history_tallies_preamble: typing.Annotated[abc.Terminal, r'\n\n number of nonzero history tallies = '] = abc.Terminal[r'\n\n number of nonzero history tallies = '](
        '\n\n number of nonzero history tallies = '
    )
    number_nonzero_history_tallies: typing.Annotated[abc.Terminal, r'.{11}']
    efficiency_nonzero_tallies_preamble: typing.Annotated[abc.Terminal, r'          efficiency for the nonzero tallies  = '] = abc.Terminal[r'          efficiency for the nonzero tallies  = '](
        '          efficiency for the nonzero tallies  = '
    )
    efficiency_nonzero_tallies: typing.Annotated[abc.Terminal, r'.{6}']
    history_number_largest_tally_preamble: typing.Annotated[abc.Terminal, r'\n history number of largest  tally  = '] = abc.Terminal[r'\n history number of largest  tally  = '](
        '\n history number of largest  tally  = '
    )
    history_number_largest_tally: typing.Annotated[abc.Terminal, r'.{11}']
    largest_unnormalized_history_tally_preamble: typing.Annotated[abc.Terminal, r'          largest  unnormalized history tally = '] = abc.Terminal[
        r'          largest  unnormalized history tally = '
    ]('          largest  unnormalized history tally = ')
    largest_unnormalized_history_tally: typing.Annotated[abc.Terminal, r'.{11}']
    largest_tally_per_average_tally_preamble: typing.Annotated[
        abc.Terminal,
        r'\n \(largest  tally\)/\(average tally\)  = ',
    ] = abc.Terminal[r'\n \(largest  tally\)/\(average tally\)  = ']('\n (largest  tally)/(average tally)  = ')
    largest_tally_per_average_tally: typing.Annotated[abc.Terminal, r'.{11}']
    largest_tally_per_average_nonzero_tally_preamble: typing.Annotated[
        abc.Terminal,
        r'          \(largest  tally\)/\(avg nonzero tally\)= ',
    ] = abc.Terminal[r'          \(largest  tally\)/\(avg nonzero tally\)= ']('          (largest  tally)/(avg nonzero tally)= ')
    largest_tally_per_average_nonzero_tally: typing.Annotated[abc.Terminal, r'.{11}']
    confidence_interval_shift_per_mean_preamble: typing.Annotated[abc.Terminal, r'\n\n \(confidence interval shift\)/mean  = '] = abc.Terminal[r'\n\n \(confidence interval shift\)/mean  = '](
        '\n\n (confidence interval shift)/mean  = '
    )
    confidence_interval_shift_per_mean: typing.Annotated[abc.Terminal, r'.{11}']
    shifted_confidence_interval_center_preamble: typing.Annotated[abc.Terminal, r'          shifted confidence interval center  = '] = abc.Terminal[
        r'          shifted confidence interval center  = '
    ]('          shifted confidence interval center  = ')
    shifted_confidence_interval_center: typing.Annotated[abc.Terminal, r'.{11}']
    table_preamble: typing.Annotated[
        abc.Terminal,
        r'\n\n\n if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:',
    ] = abc.Terminal[r'\n\n\n if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:'](
        '\n\n\n if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:'
    )
    table_heading: typing.Annotated[
        abc.Terminal,
        r'\n\n      estimated quantities           value at nps           value at nps\+1           value\(nps\+1\)/value\(nps\)-1\.',
    ] = abc.Terminal[r'\n\n      estimated quantities           value at nps           value at nps\+1           value\(nps\+1\)/value\(nps\)-1\.'](
        '\n\n      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.'
    )
    table_mean_preamble: typing.Annotated[abc.Terminal, r'\n\n      mean'] = abc.Terminal[r'\n\n      mean']('\n\n      mean')
    table_mean_nps: typing.Annotated[abc.Terminal, r'                            .{11}']
    table_mean_nps_plus: typing.Annotated[abc.Terminal, r'             .{11}']
    table_mean_nps_times: typing.Annotated[abc.Terminal, r'                    .{9}']
    table_relative_error_preamble: typing.Annotated[abc.Terminal, r'\n      relative error'] = abc.Terminal[r'\n      relative error']('\n      relative error')
    table_relative_error: typing.Annotated[abc.Terminal, r'                  .{11}']
    table_relative_error_plus: typing.Annotated[abc.Terminal, r'             .{11}']
    table_relative_error_times: typing.Annotated[abc.Terminal, r'                    .{9}']
    table_variance_variance_preamble: typing.Annotated[abc.Terminal, r'\n      variance of the variance'] = abc.Terminal[r'\n      variance of the variance']('\n      variance of the variance')
    table_variance_variance: typing.Annotated[abc.Terminal, r'        .{11}']
    table_variance_variance_plus: typing.Annotated[abc.Terminal, r'             .{11}']
    table_variance_variance_times: typing.Annotated[abc.Terminal, r'                    .{9}']
    table_shifted_center_preamble: typing.Annotated[abc.Terminal, r'\n      shifted center'] = abc.Terminal[r'\n      shifted center']('\n      shifted center')
    table_shifted_center: typing.Annotated[abc.Terminal, r'                  .{11}']
    table_shifted_center_plus: typing.Annotated[abc.Terminal, r'             .{11}']
    table_shifted_center_times: typing.Annotated[abc.Terminal, r'                    .{9}']
    table_figure_merit_preamble: typing.Annotated[abc.Terminal, r'\n      figure of merit'] = abc.Terminal[r'\n      figure of merit']('\n      figure of merit')
    table_figure_merit: typing.Annotated[abc.Terminal, r'                 .{11}']
    table_figure_merit_plus: typing.Annotated[abc.Terminal, r'             .{11}']
    table_figure_merit_times: typing.Annotated[abc.Terminal, r'                    .{9}']
    message_preamble: typing.Annotated[abc.Terminal, r'\n\n'] = abc.Terminal[r'\n\n']('\n\n')
    message: typing.Annotated[abc.Terminal, r'[\s\S]+?\n\n']
    figure_merit_preamble: typing.Annotated[
        abc.Terminal,
        r' fom = \(histories/minute\)\*\(f\(x\) signal-to-noise ratio\)\*\*2 = \(.{9}\)\*\(.{10}\)\*\*2 = \(.{9}\)\*\(.{9}\) = ',
    ]
    figure_merit: typing.Annotated[abc.Terminal, r'.{9}']
