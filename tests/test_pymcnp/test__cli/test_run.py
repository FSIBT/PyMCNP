import sys
import pathlib

import pytest

from pymcnp._cli import run


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


def test_main_valid(monkeypatch, fake_mcnp: str) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp}'])
    run.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp}'])
    run.main()


def test_main_run_failed(monkeypatch, fake_mcnp_fail: str) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), f'--command={fake_mcnp_fail}'])
    with pytest.raises(SystemExit) as error:
        run.main()
    assert error.value.code == 1


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'valid_00.inp'), '--command=""'])
    with pytest.raises(SystemExit) as error:
        run.main()
    assert error.value.code == 1
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit) as error:
        run.main()
    assert error.value.code == 1
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'invalid_01.inp')])
    with pytest.raises(SystemExit) as error:
        run.main()
    assert error.value.code == 3
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'invalid_02.inp')])
    with pytest.raises(SystemExit) as error:
        run.main()
    assert error.value.code == 3
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', 'hello'])
    with pytest.raises(SystemExit) as error:
        run.main()
    assert error.value.code == 2


def test_main_partly_parsed(monkeypatch, capsys, tmp_path: pathlib.Path, fake_mcnp: str) -> None:
    # A card PyMCNP cannot parse drops it and every card after it, so nothing is run (as `pymcnp check --fix` does not rewrite).
    partial = tmp_path / 'partial.inp'
    partial.write_text((FILES / 'inp' / 'valid_00.inp').read_text().replace('NPS 100000', 'QQQ J J [1]\nNPS 100000'))
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'run', str(FILES / 'inp' / 'valid_00.inp'), str(partial), f'--command={fake_mcnp}', f'--path={tmp_path}'])

    with pytest.raises(SystemExit) as error:
        run.main()

    assert error.value.code == 3
    assert not list(tmp_path.glob('pymcnp-*'))
    out = ' '.join(capsys.readouterr().out.replace('│', '').split())
    assert 'line 28: PyMCNP cannot parse the card "QQQ J J [1]"' in out and 'Not running' in out and 'Done!' not in out
