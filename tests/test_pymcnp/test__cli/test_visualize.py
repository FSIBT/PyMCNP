import sys
import shutil
import pathlib

import pytest
import pyvista

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


@pytest.mark.render
@pytest.mark.parametrize('pdf', [False, True])
def test_main_skips(monkeypatch, tmp_path: pathlib.Path, pdf: bool) -> None:
    # Records how many actors each rendered plot has, instead of opening windows or writing PDFs.
    inp = tmp_path / 'spheres.inp'
    inp.write_text('title\n1 0 -1\n2 0 -2 #1\n3 0 2\n\n1 so 1\n2 so 2\n\nnps 1\n')
    actors = []
    name = 'save_graphic' if pdf else 'show'
    monkeypatch.setattr(pyvista.Plotter, name, lambda self, *args, **kwargs: actors.append(len(self.renderer.actors)))
    extra = ['--pdf'] if pdf else []

    for option in ['--cells', '--cells-skip=1', '--cells-skip=1,2', '--surfaces', '--surfaces-skip=2']:
        monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), option, *extra])
        visualize.main()

    cells, cells_skip_1, cells_skip_12, surfaces, surfaces_skip_2 = actors
    assert cells_skip_1 == cells - 2
    assert cells_skip_12 == cells - 4
    assert surfaces_skip_2 == surfaces - 1


@pytest.mark.render
@pytest.mark.parametrize(
    ('options', 'names'),
    [
        (['--cells'], ['cells']),
        (['--surfaces'], ['surfaces']),
        (['--cells-skip=1'], ['cells-skip']),
        (['-c', '1,2'], ['cell_1_2']),
        (['-s', '1'], ['surface_1']),
        (['-s', '1,2'], ['surface_1_2']),
        (['--surfaces-skip=1'], ['surfaces-skip']),
    ],
)
def test_main_pdf_names(monkeypatch, capsys, tmp_path: pathlib.Path, options, names) -> None:
    inp = tmp_path / 'spheres.inp'
    inp.write_text('title\n1 0 -1\n2 0 -2 #1\n3 0 2\n\n1 so 1\n2 so 2\n\nnps 1\n')
    monkeypatch.setattr(pyvista.Plotter, 'save_graphic', lambda self, *args, **kwargs: None)
    monkeypatch.setattr(sys, 'argv', ['pymcnp', 'visualize', str(inp), *options, '--pdf'])

    visualize.main()

    out = ''.join(capsys.readouterr().out.replace('│', '').split())

    for name in names:
        path = tmp_path / f'spheres-{name}.pdf'
        assert f'Wrote{path}' in out
        assert f'Wrote{path}.' not in out
