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

    def test_to_pdf_valid(self, outp: pymcnp.Outp) -> None:
        plotter = pymcnp.Plot()

        plotter.to_pdf(outp, '1', pathlib.Path('hello.pdf'))
