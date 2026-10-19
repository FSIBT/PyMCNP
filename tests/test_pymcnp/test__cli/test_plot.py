import sys
import pathlib

import pytest
import matplotlib.pyplot

from pymcnp._cli import plot


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '21'])
    plot.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '21', '--pdf'])
    plot.main()

    matplotlib.pyplot.close()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'invalid_02.outp'), '21'])
    with pytest.raises(SystemExit):
        plot.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'outp' / 'valid_39.outp'), '123'])
    with pytest.raises(SystemExit):
        plot.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', 'hello', '1'])
    with pytest.raises(SystemExit):
        plot.main()

    matplotlib.pyplot.close()
