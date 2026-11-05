import abc as abc_
import typing


from ... import abc
from ..Subblock import Subblock


class Statistics(Subblock):
    """
    Represents tally statistical check subblocks.
    """

    @property
    @abc_.abstractmethod
    def is_passed(self) -> bool:
        """
        ``True`` if the statistical check passed.
        """

        raise NotImplementedError

    @property
    def is_failed(self) -> bool:
        """
        ``True`` if the statistical check failed.
        """

        return not self.is_passed


class StatisticsPassed(Statistics):
    """
    Represents tally passed statistical check subblocks.
    """

    table_preamble: typing.Annotated[
        abc.Terminal,
        r'\n ===================================================================================================================================',
    ]
    table_number_preamble: typing.Annotated[
        abc.Terminal,
        r'\n\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart \(tfc\) bin of tally ',
    ]
    table_number: typing.Annotated[abc.Terminal, r'.{8}']
    table_heading_1: typing.Annotated[
        abc.Terminal,
        r'\n\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-',
    ]
    table_heading_2: typing.Annotated[
        abc.Terminal,
        r'\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope',
    ]
    table_desired_preamble: typing.Annotated[abc.Terminal, r'\n\n desired     ']
    table_desired_mean_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_relative_error_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_desired_relative_error_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_desired_relative_error_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_relative_error_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_relative_error_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_relative_error_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_desired_variance_variance_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_desired_variance_variance_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_desired_variance_variance_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_variance_variance_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_variance_variance_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_variance_variance_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_desired_figure_merit_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_desired_figure_merit_value: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_figure_merit_behavior_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_figure_merit_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_pdf_preamble: typing.Annotated[abc.Terminal, r'     ']
    table_desired_pdf: typing.Annotated[abc.Terminal, r'.{5}']
    table_observed_preamble: typing.Annotated[abc.Terminal, r'\n observed    ']
    table_observed_mean_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_relative_error_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_observed_relative_error_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_observed_relative_error_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_relative_error_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_relative_error_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_relative_error_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_observed_variance_variance_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_observed_variance_variance_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_observed_variance_variance_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_variance_variance_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_variance_variance_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_variance_variance_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_observed_figure_merit_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_observed_figure_merit_value: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_figure_merit_behavior_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_figure_merit_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_pdf_preamble: typing.Annotated[abc.Terminal, r'     ']
    table_observed_pdf: typing.Annotated[abc.Terminal, r'.{5}']
    table_passed_preamble: typing.Annotated[abc.Terminal, r'\n passed[?]     ']
    table_passed_mean_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_relative_error_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_passed_relative_error_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_passed_relative_error_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_relative_error_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_relative_error_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_relative_error_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_passed_variance_variance_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_passed_variance_variance_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_passed_variance_variance_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_variance_variance_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_variance_variance_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_variance_variance_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_passed_figure_merit_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_passed_figure_merit_value: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_figure_merit_behavior_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_figure_merit_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_pdf_preamble: typing.Annotated[abc.Terminal, r'     ']
    table_passed_pdf: typing.Annotated[abc.Terminal, r'.{5}']
    table_postamble: typing.Annotated[
        abc.Terminal,
        r'\n\n ===================================================================================================================================',
    ]
    confidence_interval_preamble: typing.Annotated[
        abc.Terminal,
        r'\n\n\n this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify\.\n the results in other bins associated with this tally may not meet these statistical criteria\.\n\n ----- estimated confidence intervals:  -----',
    ]
    estimated_asymmetric_confidence_interval_preamble: typing.Annotated[
        abc.Terminal,
        r'\n\n estimated asymmetric confidence interval\(1,2,3 sigma\): ',
    ]
    estimated_asymmetric_confidence_interval: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    estimated_symmetric_confidence_interval_preamble: typing.Annotated[
        abc.Terminal,
        r'\n estimated  symmetric confidence interval\(1,2,3 sigma\): ',
    ]
    estimated_symmetric_confidence_interval: typing.Annotated[abc.Terminal, r'.+?\n']

    @property
    def is_passed(self) -> bool:
        """
        ``True`` if the statistical check passed.
        """

        return True


class StatisticsFailed(Statistics):
    """
    Represents tally failed statistical check subblocks.
    """

    table_preamble: typing.Annotated[
        abc.Terminal,
        r'\n ===================================================================================================================================',
    ]
    table_number_preamble: typing.Annotated[
        abc.Terminal,
        r'\n\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart \(tfc\) bin of tally ',
    ]
    table_number: typing.Annotated[abc.Terminal, r'.{8}']
    table_heading_1: typing.Annotated[
        abc.Terminal,
        r'\n\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-',
    ]
    table_heading_2: typing.Annotated[
        abc.Terminal,
        r'\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope',
    ]
    table_desired_preamble: typing.Annotated[abc.Terminal, r'\n\n desired     ']
    table_desired_mean_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_relative_error_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_desired_relative_error_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_desired_relative_error_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_relative_error_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_relative_error_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_relative_error_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_desired_variance_variance_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_desired_variance_variance_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_desired_variance_variance_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_variance_variance_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_variance_variance_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_variance_variance_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_desired_figure_merit_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_desired_figure_merit_value: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_figure_merit_behavior_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_desired_figure_merit_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_desired_pdf_preamble: typing.Annotated[abc.Terminal, r'     ']
    table_desired_pdf: typing.Annotated[abc.Terminal, r'.{5}']
    table_observed_preamble: typing.Annotated[abc.Terminal, r'\n observed    ']
    table_observed_mean_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_relative_error_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_observed_relative_error_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_observed_relative_error_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_relative_error_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_relative_error_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_relative_error_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_observed_variance_variance_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_observed_variance_variance_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_observed_variance_variance_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_variance_variance_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_variance_variance_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_variance_variance_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_observed_figure_merit_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_observed_figure_merit_value: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_figure_merit_behavior_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_observed_figure_merit_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_observed_pdf_preamble: typing.Annotated[abc.Terminal, r'     ']
    table_observed_pdf: typing.Annotated[abc.Terminal, r'.{5}']
    table_passed_preamble: typing.Annotated[abc.Terminal, r'\n passed[?]     ']
    table_passed_mean_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_relative_error_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_passed_relative_error_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_passed_relative_error_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_relative_error_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_relative_error_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_relative_error_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_passed_variance_variance_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_passed_variance_variance_value: typing.Annotated[abc.Terminal, r'.{5}']
    table_passed_variance_variance_decrease_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_variance_variance_decrease: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_variance_variance_rate_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_variance_variance_rate: typing.Annotated[abc.Terminal, r'.{13}']
    table_passed_figure_merit_value_preamble: typing.Annotated[abc.Terminal, r'      ']
    table_passed_figure_merit_value: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_figure_merit_behavior_preamble: typing.Annotated[abc.Terminal, r'   ']
    table_passed_figure_merit_behavior: typing.Annotated[abc.Terminal, r'.{8}']
    table_passed_pdf_preamble: typing.Annotated[abc.Terminal, r'     ']
    table_passed_pdf: typing.Annotated[abc.Terminal, r'.{5}']
    table_postamble: typing.Annotated[
        abc.Terminal,
        r'\n\n ===================================================================================================================================',
    ]
    fails_preamble: typing.Annotated[
        abc.Terminal,
        r'\n\n\n warning\.  the tally in the tally fluctuation chart bin did not pass ',
    ]
    fails: typing.Annotated[abc.Terminal, r'.{2}']
    fails_postamble: typing.Annotated[abc.Terminal, r' of the 10 statistical checks\.\n']

    @property
    def is_passed(self) -> bool:
        """
        ``True`` if the statistical check passed.
        """

        return False
