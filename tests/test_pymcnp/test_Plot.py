import pathlib

import pandas
import matplotlib.pyplot
import pytest

import pymcnp

# The OUTP fixtures hold tallies PyMCNP cannot parse.
pytestmark = pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')


class Test_Plot:
    def test_to_show_invalid(self, outp: pymcnp.Outp) -> None:
        plotter = pymcnp.Plot()

        with pytest.raises(pymcnp.abc.Error):
            plotter.to_show(outp, '23423432')

    def test_to_show_unparsed_tally(self) -> None:
        outp, _ = pymcnp.Outp.from_file(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_01.outp')

        with pytest.raises(pymcnp.abc.Error, match='Tally not parsed'):
            pymcnp.Plot().to_show(outp, 4)
        with pytest.raises(pymcnp.abc.Error, match='Tally not found'):
            pymcnp.Plot().to_show(outp, 5)

    def test_plot_to_pdf_writes(self, tmp_path: pathlib.Path) -> None:
        plotter = pymcnp.Plot()
        outp, _ = pymcnp.Outp.from_file(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_38.outp')

        path = tmp_path / 'f.pdf'

        plotter.to_pdf(outp, '1', path)

        assert path.stat().st_size > 0

    @pytest.mark.parametrize('number', [21, ' 21 ', pymcnp.inp.literal.Integer('21')])
    def test_to_show_normalizes_numbers(self, outp: pymcnp.Outp, number: object) -> None:
        plotter = pymcnp.Plot()

        assert len(plotter.to_show(outp, number)) == len(plotter.to_show(outp, '21')) > 0

    def test_to_show_ignores_empty_tallies(self, outp: pymcnp.Outp, monkeypatch: pytest.MonkeyPatch) -> None:
        # An empty frame must not stand in for a tally that is missing.
        frames = list(outp.to_dataframe_iter())
        monkeypatch.setattr(type(outp), 'to_dataframe_iter', lambda self: iter([pandas.DataFrame(), *frames]))
        plotter = pymcnp.Plot()

        with pytest.raises(pymcnp.abc.Error, match='Tally not found'):
            plotter.to_show(outp, '23423432')
        assert len(plotter.to_show(outp, 21)) > 0


def test_energy_bins_are_upper_edges(tmp_path: pathlib.Path) -> None:
    # OUTP energy bins are upper bin edges, so each value is drawn from the previous edge up to its own edge, the first
    # from 0, and its error bar sits at the centre of its bin.
    outp, _ = pymcnp.Outp.from_file(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp' / 'valid_38.outp')
    figures = pymcnp.Plot().to_show(outp, 1)
    tally = outp.tally(1)
    for figure in figures:
        (stairs,) = [patch for patch in figure.axes[0].patches if patch.get_label() == 'Tally']
        values, edges, _ = stairs.get_data()
        bins = edges[1:]
        assert edges[0] == 0 and all(edges[1:] > edges[:-1]) and set(bins) <= set(tally['bins'])
        assert len(values) == len(bins) > 1
        (errors,) = figure.axes[0].containers
        segments = errors.lines[2][0].get_segments()
        assert [segment[0][0] for segment in segments] == pytest.approx((edges[:-1] + edges[1:]) / 2)
    matplotlib.pyplot.close('all')


@pytest.mark.parametrize(
    'bins, lower',
    [([1.0, 2.0, 4.0], 0.0), ([-0.5, 0.0, 1.0], -1.0), ([0.0, 0.5], 0.0), ([0.0, 1.0, 2.0], 0.0), ([-1.0, -0.5], -1.5), ([-2.0], -3.0)],
)
def test_lower_edge(bins: list[float], lower: float) -> None:
    # The first bin starts at 0 unless the bins are negative (cosines), then one bin width below.
    assert pymcnp.Plot._edges(pandas.Series(bins)).tolist() == [lower, *bins]
