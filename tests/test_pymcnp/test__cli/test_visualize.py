import sys
import shutil
import pathlib

import pytest

from pymcnp._cli import visualize


FILES: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent / 'files'


@pytest.mark.render
def test_main_valid(monkeypatch, tmp_path: pathlib.Path) -> None:
    # The CLI writes PDFs next to its input, so run on a copy inside ``tmp_path``.
    inp = tmp_path / 'valid_00.inp'
    shutil.copy(FILES / 'inp' / 'valid_00.inp', inp)

    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp)])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--cells'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--surfaces'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--cells', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--surfaces', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--cell=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--surface=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--cell=1', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--surface=1', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--cells-skip=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--surfaces-skip=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--cells-skip=1', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), '--surfaces-skip=1', '--pdf'])
    visualize.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(FILES / 'inp' / 'valid_00.inp'), '--cell=81023'])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(FILES / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(FILES / 'inp' / 'invalid_01.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(FILES / 'inp' / 'invalid_02.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(FILES / 'inp' / 'valid_41.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', 'hello'])
    with pytest.raises(SystemExit):
        visualize.main()
