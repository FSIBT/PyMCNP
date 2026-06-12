import typing
import dataclasses

import pandas

from ... import abc
from ..Block import Block
from .. import subblock


class Tally(Block):
    """
    Represents tally blocks.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for tally blocks.

        Returns:
            Pandas dataframe for tally block.
        """

        assert hasattr(self, 'number')
        assert isinstance(self.number, str)
        assert hasattr(self, 'tally_type')
        assert isinstance(self.tally_type, str)
        assert hasattr(self, 'particles')
        assert isinstance(self.particles, str)
        assert hasattr(self, 'nps')
        assert isinstance(self.nps, str)
        assert hasattr(self, 'subtallies')
        assert isinstance(self.subtallies, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.subtallies, abc.Array) or all(isinstance(subtally, subblock.Tally) for subtally in self.subtallies)

        if isinstance(self.subtallies, abc.Array) and self.subtallies:
            df = pandas.concat((subtally.to_dataframe() for subtally in self.subtallies), ignore_index=True)
            df['number'] = self.number.strip()
            df['type'] = self.tally_type.strip()
            df['particles'] = self.particles.strip()
            df['nps'] = self.nps.strip()
            return df

        return pandas.DataFrame()


class Tally_0(Tally):
    """
    Represents tally blocks, form #0.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        confidence_interval_preamble: tally block `\\n\\n\\n this tally meets the statistical criteria used to form confidence intervals.
        estimated_asymmetric_confidence_interval_preamble: tally block `\\n\\n estimated asymmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_asymmetric_confidence_interval: tally block estimated asymmetric confidence interval.
        estimated_symmetric_confidence_interval_preamble: tally block `\\n estimated  symmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_symmetric_confidence_interval: tally block estimated symmetric confidence interval.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    surface_preamble: typing.Annotated[abc.Terminal, r'\n\n           areas   \n                surface: ']
    surface_number: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    surface_area_preamble: typing.Annotated[abc.Terminal, r'\n                         ']
    surface_area: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Surface, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_1(Tally):
    """
    Represents tally blocks, form #1.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        fails_preamble: tally block `\\n\\n\\n warning.  the tally in the tally fluctuation chart bin did not pass ` symbol.
        fails: tally block fails.
        fails_postamble: tally block fails postamble.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    surface_preamble: typing.Annotated[abc.Terminal, r'\n\n           areas   \n                surface: ']
    surface_number: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    surface_area_preamble: typing.Annotated[abc.Terminal, r'\n                         ']
    surface_area: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Surface, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_2(Tally):
    """
    Represents tally blocks, form #2.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        surface_preamble: tally block `           areas   \n                surface.
        surface_number: tally block surface number.
        surface_area_preamble: tally block `\\n                         ` symbol.
        surface_area: tally block surface area.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        confidence_interval_preamble: tally block `\\n\\n\\n this tally meets the statistical criteria used to form confidence intervals.
        estimated_asymmetric_confidence_interval_preamble: tally block `\\n\\n estimated asymmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_asymmetric_confidence_interval: tally block estimated asymmetric confidence interval.
        estimated_symmetric_confidence_interval_preamble: tally block `\\n estimated  symmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_symmetric_confidence_interval: tally block estimated symmetric confidence interval.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.SurfaceAngle, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_3(Tally):
    """
    Represents tally blocks, form #3.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        surface_preamble: tally block `           areas   \n                surface.
        surface_number: tally block surface number.
        surface_area_preamble: tally block `\\n                         ` symbol.
        surface_area: tally block surface area.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        fails_preamble: tally block `\\n\\n\\n warning.  the tally in the tally fluctuation chart bin did not pass ` symbol.
        fails: tally block fails.
        fails_postamble: tally block fails postamble.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.SurfaceAngle, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_4(Tally):
    """
    Represents tally blocks, form #4.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        cell_preamble: tally block `           volumes \\n                   cell.
        cell_number: tally block cell number.
        cell_volume_preamble: tally block `\\n                         ` symbol.
        cell_volume: tally block cell volume.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        confidence_interval_preamble: tally block `\\n\\n\\n this tally meets the statistical criteria used to form confidence intervals.
        estimated_asymmetric_confidence_interval_preamble: tally block `\\n\\n estimated asymmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_asymmetric_confidence_interval: tally block estimated asymmetric confidence interval.
        estimated_symmetric_confidence_interval_preamble: tally block `\\n estimated  symmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_symmetric_confidence_interval: tally block estimated symmetric confidence interval.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    cell_preamble: typing.Annotated[abc.Terminal, r'\n\n           volumes \n                   cell: ']
    cell_number: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    cell_volume_preamble: typing.Annotated[abc.Terminal, r'\n                         ']
    cell_volume: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Cell, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_5(Tally):
    """
    Represents tally blocks, form #5.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        cell_preamble: tally block `\\n\\n           volumes \\n                   cell: `
        cell_number: tally block cell number.
        cell_volume_preamble: tally block `\\n                         ` symbol.
        cell_volume: tally block cell volume.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        fails_preamble: tally block `\\n\\n\\n warning.  the tally in the tally fluctuation chart bin did not pass ` symbol.
        fails: tally block fails.
        fails_postamble: tally block fails postamble.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    cell_preamble: typing.Annotated[abc.Terminal, r'\n\n           volumes \n                   cell: ']
    cell_number: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    cell_volume_preamble: typing.Annotated[abc.Terminal, r'\n                         ']
    cell_volume: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Cell, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_6(Tally):
    """
    Represents tally blocks, form #6.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        confidence_interval_preamble: tally block `\\n\\n\\n this tally meets the statistical criteria used to form confidence intervals.
        estimated_asymmetric_confidence_interval_preamble: tally block `\\n\\n estimated asymmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_asymmetric_confidence_interval: tally block estimated asymmetric confidence interval.
        estimated_symmetric_confidence_interval_preamble: tally block `\\n estimated  symmetric confidence interval(1,2,3 sigma)` symbol.
        estimated_symmetric_confidence_interval: tally block estimated symmetric confidence interval.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Cell, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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


class Tally_7(Tally):
    """
    Represents tally blocks, form #7.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block `        nps = ` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block `\\n           tally type ` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block `\\n           particle(s)` symbol.
        particles: tally block particles.
        subtallies_preamble: tally block `\\n \\n` symbol.
        subtallies: tally block subtallies.
        table_preamble: tally block `\\n ===================================================================================================================================` symbol.
        table_number_preamble: tally block `\\n\\n           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc)` symbol.
        table_number: tally block table number.
        table_heading_1: tally block `\\n\\n tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-` symbol.
        table_heading_2: tally block `\\n behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope` symbol.
        table_desired_preamble: tally block `\\n\\n desired     ` symbol.
        table_desired_mean_behavior: tally block table desired mean behavior.
        table_desired_relative_error_value_preamble: tally block `      ` symbol.
        table_desired_relative_error_value: tally block table desired relative error value.
        table_desired_relative_error_decrease_preamble: tally block `   ` symbol.
        table_desired_relative_error_decrease: tally block table desired relative error decrease.
        table_desired_relative_error_rate_preamble: tally block `   ` symbol.
        table_desired_relative_error_rate: tally block table desired relative error rate.
        table_desired_variance_variance_value_preamble: tally block `      ` symbol.
        table_desired_variance_variance_value: tally block table desired variance variance value.
        table_desired_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_desired_variance_variance_decrease: tally block table desired variance variance decrease.
        table_desired_variance_variance_rate_preamble: tally block `   ` symbol.
        table_desired_variance_variance_rate: tally block table desired variance variance rate.
        table_desired_figure_merit_value_preamble: tally block `      ` symbol.
        table_desired_figure_merit_value: tally block table desired figure merit value.
        table_desired_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_desired_figure_merit_behavior: tally block table desired figure merit behavior.
        table_desired_pdf_preamble: tally block `     ` symbol.
        table_desired_pdf: tally block table desired pdf.
        table_observed_preamble: tally block `\\n observed    ` symbol.
        table_observed_mean_behavior: tally block table observed mean behavior.
        table_observed_relative_error_value_preamble: tally block `      ` symbol.
        table_observed_relative_error_value: tally block table observed relative error value.
        table_observed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_observed_relative_error_decrease: tally block table observed relative error decrease.
        table_observed_relative_error_rate_preamble: tally block `   ` symbol.
        table_observed_relative_error_rate: tally block table observed relative error rate.
        table_observed_variance_variance_value_preamble: tally block `      ` symbol.
        table_observed_variance_variance_value: tally block table observed variance variance value.
        table_observed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_observed_variance_variance_decrease: tally block table observed variance variance decrease.
        table_observed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_observed_variance_variance_rate: tally block table observed variance variance rate.
        table_observed_figure_merit_value_preamble: tally block `      ` symbol.
        table_observed_figure_merit_value: tally block table observed figure merit value.
        table_observed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_observed_figure_merit_behavior: tally block table observed figure merit behavior.
        table_observed_pdf_preamble: tally block `     ` symbol.
        table_observed_pdf: tally block table observed pdf.
        table_passed_preamble: tally block `\\n passed?     ` symbol.
        table_passed_mean_behavior: tally block table passed mean behavior.
        table_passed_relative_error_value_preamble: tally block `      ` symbol.
        table_passed_relative_error_value: tally block table passed relative error value.
        table_passed_relative_error_decrease_preamble: tally block `   ` symbol.
        table_passed_relative_error_decrease: tally block table passed relative error decrease.
        table_passed_relative_error_rate_preamble: tally block `   ` symbol.
        table_passed_relative_error_rate: tally block table passed relative error rate.
        table_passed_variance_variance_value_preamble: tally block `      ` symbol.
        table_passed_variance_variance_value: tally block table passed variance variance value.
        table_passed_variance_variance_decrease_preamble: tally block `   ` symbol.
        table_passed_variance_variance_decrease: tally block table passed variance variance decrease.
        table_passed_variance_variance_rate_preamble: tally block `   ` symbol.
        table_passed_variance_variance_rate: tally block table passed variance variance rate.
        table_passed_figure_merit_value_preamble: tally block `      ` symbol.
        table_passed_figure_merit_value: tally block table passed figure merit value.
        table_passed_figure_merit_behavior_preamble: tally block `   ` symbol.
        table_passed_figure_merit_behavior: tally block table passed figure merit behavior.
        table_passed_pdf_preamble: tally block `     ` symbol.
        table_passed_pdf: tally block table passed pdf.
        table_postamble: tally block table postamble.
        fails_preamble: tally block `\\n\\n\\n warning.  the tally in the tally fluctuation chart bin did not pass ` symbol.
        fails: tally block fails.
        fails_postamble: tally block fails postamble.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Cell, typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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
