import sys
import shutil
import pathlib

import pytest
import matplotlib.pyplot

from pymcnp._cli import plot
from pymcnp.Outp import Outp


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


@pytest.mark.parametrize('pdf', [[], ['--pdf']])
def test_main_partly_parsed(monkeypatch, capsys, tmp_path: pathlib.Path, pdf: list[str]) -> None:
    # A part of the file PyMCNP cannot parse is missing: plot what was parsed, warn, and exit 3, as `visualize` does.
    path = tmp_path / 'valid_39.outp'
    shutil.copy(FILES / 'outp' / 'valid_39.outp', path)
    from_file = Outp.from_file
    monkeypatch.setattr(Outp, 'from_file', lambda file: (from_file(file)[0], 'garbage [here]\nmore\n'))
    shown = []
    monkeypatch.setattr(matplotlib.pyplot, 'show', lambda: shown.append(True))
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'plot', str(path), '21', *pdf])

    with pytest.raises(SystemExit) as error:
        plot.main()

    assert error.value.code == 3
    assert shown == ([] if pdf else [True])
    assert path.with_suffix('.pdf').exists() == bool(pdf)
    out = ' '.join(capsys.readouterr().out.replace('│', '').split())
    # The patched remainder is not the end of the file, so no line number is given.
    assert 'Warning:' in out and ': PyMCNP cannot parse the line "garbage [here]"' in out and ', line' not in out and 'Done!' not in out

    matplotlib.pyplot.close('all')
