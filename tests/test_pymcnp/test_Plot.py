import pathlib

import pytest

import pymcnp


class Test_Plot:
    def test_to_show_valid(self, plot: pymcnp.Plot) -> None:
        plot.to_show('21')

    def test_to_show_invalid(self, plot: pymcnp.Plot) -> None:
        with pytest.raises(pymcnp.abc.Error):
            plot.to_show('23423432')

    def test_to_pdf_valid(self, plot: pymcnp.Plot) -> None:
        plot.to_pdf('1', pathlib.Path('hello.pdf'))
