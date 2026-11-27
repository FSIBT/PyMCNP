import pathlib

import pytest
import pyvista

import pymcnp


EXAMPLE = pathlib.Path(__file__).parent.parent.parent / 'examples' / 'example_00.inp'


pytestmark = pytest.mark.render


class Test_Visualize:
    def test_to_show_surfaces_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_surfaces(inp)

    def test_to_show_cells_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_cells(inp)

    def test_to_show_surface_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_surface(inp, '1')

    def test_to_show_cell_valid(self, inp: pymcnp.Inp) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_show_cell(inp, '1')
        visualizer.to_show_cell(inp, '4')

    def test_to_pdf_surfaces_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_surfaces(inp, tmp_path / 'hello.pdf')

    def test_to_pdf_cells_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_cells(inp, tmp_path / 'hello.pdf')

    def test_to_pdf_surface_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_surface(inp, tmp_path / 'hello.pdf', '1')

    def test_to_pdf_cell_valid(self, inp: pymcnp.Inp, tmp_path: pathlib.Path) -> None:
        visualizer = pymcnp.Visualize()
        visualizer.to_pdf_cell(inp, tmp_path / 'hello.pdf', '1')

    def test_visualize_cells_runs(self) -> None:
        inp = pymcnp.Inp.from_file(EXAMPLE)[0]

        plot = pymcnp.Visualize().to_show_cells(inp)

        assert isinstance(plot, pyvista.Plotter)
        assert len(plot.renderer.actors) >= 1

    def test_visualize_pdf(self, tmp_path: pathlib.Path) -> None:
        # Renders for real, off screen (``pyvista.OFF_SCREEN`` is set in ``conftest.py``).
        inp = pymcnp.Inp.from_file(EXAMPLE)[0]
        path = tmp_path / 'c.pdf'

        pymcnp.Visualize().to_pdf_cells(inp, path)

        assert path.exists()
        assert path.stat().st_size > 0


# Cell 2 refers to cell 1 with ``#1``, so skipping cell 1 must still resolve it.
SPHERES = 'title\n1 0 -1\n2 0 -2 #1\n3 0 2\n\n1 so 1\n2 so 2\n\nnps 1\n'


def _actors(plot: pyvista.Plotter) -> int:
    return len(plot.renderer.actors)


class Test_Visualize_numbers:
    @pytest.fixture
    def spheres(self) -> pymcnp.Inp:
        return pymcnp.Inp.from_mcnp(SPHERES)[0]

    @pytest.mark.parametrize('skip', [(1,), ('1',), (' 1 ',), (pymcnp.inp.literal.Integer('1'),)])
    def test_to_show_cells_skips(self, spheres: pymcnp.Inp, skip: tuple) -> None:
        visualizer = pymcnp.Visualize()
        everything = _actors(visualizer.to_show_cells(spheres))

        # Each cell adds a volume and a mesh.
        assert _actors(visualizer.to_show_cells(spheres, skip=skip)) == everything - 2
        assert _actors(visualizer.to_show_cells(spheres, skip=(1, 2, 3))) == _actors(visualizer.to_show_cell(spheres))

    @pytest.mark.parametrize('skip', [(1,), ('1',), (' 1 ',), (pymcnp.inp.literal.Integer('1'),)])
    def test_to_show_surfaces_skips(self, spheres: pymcnp.Inp, skip: tuple) -> None:
        visualizer = pymcnp.Visualize()
        everything = _actors(visualizer.to_show_surfaces(spheres))

        assert _actors(visualizer.to_show_surfaces(spheres, skip=skip)) == everything - 1
        assert _actors(visualizer.to_show_surfaces(spheres, skip=(1, 2))) == _actors(visualizer.to_show_surface(spheres))

    def test_to_pdf_skips(self, spheres: pymcnp.Inp, tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
        saved = []
        monkeypatch.setattr(pyvista.Plotter, 'save_graphic', lambda self, path: saved.append(_actors(self)))
        visualizer = pymcnp.Visualize()

        visualizer.to_pdf_cells(spheres, tmp_path / 'cells.pdf')
        visualizer.to_pdf_cells(spheres, tmp_path / 'cells.pdf', skip=(1,))
        visualizer.to_pdf_surfaces(spheres, tmp_path / 'surfaces.pdf')
        visualizer.to_pdf_surfaces(spheres, tmp_path / 'surfaces.pdf', skip=(1,))

        assert saved[1] == saved[0] - 2
        assert saved[3] == saved[2] - 1

    @pytest.mark.parametrize('number', [1, ' 1 ', pymcnp.inp.literal.Integer('1')])
    def test_to_show_cell_normalizes_numbers(self, spheres: pymcnp.Inp, number: object) -> None:
        visualizer = pymcnp.Visualize()

        assert _actors(visualizer.to_show_cell(spheres, number)) == _actors(visualizer.to_show_cell(spheres, '1'))
        assert _actors(visualizer.to_show_cell(spheres, number, 2)) == _actors(visualizer.to_show_cell(spheres, '1', '2'))
        assert _actors(visualizer.to_show_cell(spheres, '1')) > _actors(visualizer.to_show_cell(spheres))

    @pytest.mark.parametrize('number', [1, ' 1 ', pymcnp.inp.literal.Integer('1')])
    def test_to_show_surface_normalizes_numbers(self, spheres: pymcnp.Inp, number: object) -> None:
        visualizer = pymcnp.Visualize()

        assert _actors(visualizer.to_show_surface(spheres, number)) == _actors(visualizer.to_show_surface(spheres, '1'))
        assert _actors(visualizer.to_show_surface(spheres, '1')) > _actors(visualizer.to_show_surface(spheres))


# Cell 1 refers to cell 2, which comes after it, with ``#2``, as MCNP allows.
FORWARD = 'title\n1 0 -2 #2\n2 0 -1\n3 0 2\n\n1 so 1\n2 so 2\n\nnps 1\n'


class Test_Visualize_complements:
    def test_to_show_cells_complement_of_a_later_cell(self) -> None:
        inp = pymcnp.Inp.from_mcnp(FORWARD)[0]
        visualizer = pymcnp.Visualize()

        spheres = pymcnp.Inp.from_mcnp(SPHERES)[0]

        # The same cells as ``SPHERES``, whose ``#1`` refers back.
        assert _actors(visualizer.to_show_cells(inp)) == _actors(visualizer.to_show_cells(spheres))
        assert _actors(visualizer.to_show_cell(inp, 1)) == _actors(visualizer.to_show_cell(spheres, 2))

    def test_complements_in_a_loop(self) -> None:
        inp = pymcnp.Inp.from_mcnp(FORWARD.replace('2 0 -1\n', '2 0 -1 #1\n'))[0]

        with pytest.raises(pymcnp.abc.Error, match='complement'):
            pymcnp.Visualize().to_show_cells(inp)


@pytest.mark.parametrize(
    'cells, message',
    [
        ('1 0 -1 #9\n2 0 1\n', 'Cell 1 refers to cell 9, which is not in the file.'),
        ('1 0 -1 -7\n2 0 1\n', 'Cell 1 refers to surface 7, which is not in the file.'),
        ('1 0 -1 7\n2 0 1\n', 'Cell 1 refers to surface 7, which is not in the file.'),
        ('1 0 -1 +7\n2 0 1\n', 'Cell 1 refers to surface 7, which is not in the file.'),
        # Cell 1 is made with cell 2, which holds the missing surface.
        ('1 0 -1 #2\n2 0 1 -7\n', 'Cell 2 refers to surface 7, which is not in the file.'),
    ],
)
def test_missing_cell_or_surface_is_named(cells, message) -> None:
    inp = pymcnp.Inp.from_mcnp(f'title\n{cells}\n1 so 1\n\nnps 1\n')[0]

    with pytest.raises(pymcnp.abc.Error) as error:
        pymcnp.Visualize().to_show_cells(inp)

    assert error.value.title == message
