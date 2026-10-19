import sys
import pathlib

import pytest

from pymcnp._cli import visualize


def test_main_valid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp')])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cell=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surface=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cell=1', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surface=1', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells-skip=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces-skip=1'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--cells-skip=1', '--pdf'])
    visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_00.inp'), '--surfaces-skip=1', '--pdf'])
    visualize.main()


def test_main_invalid(monkeypatch) -> None:
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_00.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_01.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'invalid_02.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(pathlib.Path(__file__).parent.parent.parent.parent / 'files' / 'inp' / 'valid_41.inp')])
    with pytest.raises(SystemExit):
        visualize.main()
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', 'hello'])
    with pytest.raises(SystemExit):
        visualize.main()
