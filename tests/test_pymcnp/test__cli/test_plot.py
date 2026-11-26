import sys
import shutil
import pathlib

import pytest
import matplotlib.pyplot

from pymcnp._cli import plot


# The OUTP fixtures hold tallies PyMCNP cannot parse.
pytestmark = pytest.mark.filterwarnings('ignore:Tally not parsed:pymcnp.abc.Warning')

FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


def test_main_valid(monkeypatch, tmp_path: pathlib.Path) -> None:
    path = tmp_path / 'valid_39.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', path)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(path), '21'])
    plot.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(path), '21', '--pdf'])
    plot.main()

    assert path.with_suffix('.pdf').stat().st_size > 0

    matplotlib.pyplot.close()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(FILES / 'outp' / 'invalid_02.outp'), '21'])
    with pytest.raises(SystemExit):
        plot.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(FILES / 'outp' / 'valid_39.outp'), '123'])
    with pytest.raises(SystemExit):
        plot.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', 'hello', '1'])
    with pytest.raises(SystemExit):
        plot.main()

    matplotlib.pyplot.close()
