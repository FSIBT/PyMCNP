import pathlib

import pytest

import pymcnp


class Test_Plot:
    def test_to_show_valid(self, outp: pymcnp.Outp) -> None:
        plotter = pymcnp.Plot()

        plotter.to_show(outp, '21')

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
