import pathlib

import pandas
import pytest

import pymcnp


class Test_Plot:
    def test_to_show_invalid(self, outp: pymcnp.Outp) -> None:
        plotter = pymcnp.Plot()

        with pytest.raises(pymcnp.abc.Error):
            plotter.to_show(outp, '23423432')

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
