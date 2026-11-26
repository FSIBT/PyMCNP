import re
import sys
import pathlib

import pytest
import pyvista
import matplotlib.pyplot

import pymcnp
from pymcnp.Ptrac import _events


@pytest.fixture(autouse=True)
def suppress_matplotlib(monkeypatch) -> None:
    matplotlib.use('Agg')
    monkeypatch.setattr(matplotlib.pyplot, 'show', lambda *args, **kwargs: None)
    yield
    matplotlib.pyplot.close('all')


@pytest.fixture(scope='session')
def pyvista_visualizations() -> tuple[pymcnp._show.pyvista.Visualization, ...]:
    return (pymcnp._show.pyvista.Sphere(0.5), pymcnp._show.pyvista.Sphere(1))


@pytest.fixture(scope='session')
def pyvista_shapes() -> dict[str, pymcnp._show.pyvista.Visualization]:
    """
    One instance of every concrete PyVista shape class.
    """

    show = pymcnp._show.pyvista

    return {
        'Box': show.Box(1.0, 1.5, 2.0),
        'ConeTruncated': show.ConeTruncated(1.0, 1.0, 0.5),
        'ConeUnbounded': show.ConeUnbounded(0.5, 1),
        'CylinderCircular': show.CylinderCircular(1.0, 1.0),
        'CylinderElliptical': show.CylinderElliptical(1.0, 0.5, 1.0),
        'CylinderHexagonal': show.CylinderHexagonal(1.0, 1.0, 1.0, 1.0),
        'CylinderUnbounded': show.CylinderUnbounded(1.0),
        'Ellipsoid': show.Ellipsoid(1.0, 0.5),
        'Empty': show.Empty(),
        'Parallelipiped': show.Parallelipiped(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0),
        'Plane': show.Plane(1.0, 0.5, 0.25, 0.5),
        'Sphere': show.Sphere(1.0),
        'Torus': show.Torus(0.5, 0.25, 1.0),
        'Wedge': show.Wedge(1.0, 1.0, 1.0),
    }


@pytest.fixture(scope='session', autouse=True)
def _pyvista_off_screen() -> None:
    """
    Renders off screen for the whole session.
    """

    pyvista.OFF_SCREEN = True


@pytest.fixture(autouse=True)
def _coarse_resolution(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Uses a coarse mesh resolution, since the default 256**3 voxel grid per cell takes minutes and gigabytes to render.
    """

    monkeypatch.setattr(pymcnp._show.pyvista, 'RESOLUTION', 24)


@pytest.fixture(autouse=True)
def _no_plot_window(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Never opens an interactive window.
    """

    monkeypatch.setattr(pyvista.Plotter, 'show', lambda self, *args, **kwargs: None)


@pytest.fixture(autouse=True)
def _run_in_tmp_path(tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Runs every test inside its own temporary directory, so files and directories that tests write, e.g., ``pymcnp-<timestamp>`` run directories, never land in the repository.
    """

    monkeypatch.chdir(tmp_path)


_FAKE_MCNP = """#!{python}
import sys, pathlib
arguments = dict(argument.split('=', 1) for argument in sys.argv[1:])
pathlib.Path(arguments['outp']).write_text('ok\\n')
"""

_FAKE_MCNP_FAIL = """#!{python}
import sys, pathlib
arguments = dict(argument.split('=', 1) for argument in sys.argv[1:])
pathlib.Path(arguments['outp']).write_text('ok\\n')
sys.exit(1)
"""


@pytest.fixture
def fake_mcnp(tmp_path: pathlib.Path) -> str:
    """
    Path to a stand-in for ``mcnp6`` that writes an output file and exits with 0.
    """

    path = tmp_path / 'fake-mcnp'
    path.write_text(_FAKE_MCNP.format(python=sys.executable))
    path.chmod(0o755)
    return str(path)


@pytest.fixture
def fake_mcnp_fail(tmp_path: pathlib.Path) -> str:
    """
    Path to a stand-in for ``mcnp6`` that writes an output file and exits with 1.
    """

    path = tmp_path / 'fake-mcnp'
    path.write_text(_FAKE_MCNP_FAIL.format(python=sys.executable))
    path.chmod(0o755)
    return str(path)


@pytest.fixture(scope='session')
def cell_a() -> pymcnp.inp.card.Cell:
    return pymcnp.inp.card.Cell_2(
        j=pymcnp.inp.literal.Integer('2'), n=pymcnp.inp.literal.Integer('1'), options=pymcnp.abc.Array[pymcnp.inp.option.Cell, pymcnp.inp.OptionSpace].from_mcnp('rho=3.1')[0]
    )


@pytest.fixture(scope='session')
def surface_a() -> pymcnp.inp.card.Surface:
    return pymcnp.inp.card.surface.So(j=pymcnp.inp.literal.Integer('101'), r=pymcnp.inp.literal.Integer('1'))


@pytest.fixture(scope='session')
def surface_b() -> pymcnp.inp.card.Surface:
    return pymcnp.inp.card.surface.Rpp(
        j=pymcnp.inp.literal.Integer('102'),
        xmin=pymcnp.inp.literal.Integer('0'),
        xmax=pymcnp.inp.literal.Integer('1'),
        ymin=pymcnp.inp.literal.Integer('0'),
        ymax=pymcnp.inp.literal.Integer('1'),
        zmin=pymcnp.inp.literal.Integer('0'),
        zmax=pymcnp.inp.literal.Integer('1'),
    )


@pytest.fixture(scope='session')
def geometry_a() -> pymcnp.inp.literal.Geometry:
    return pymcnp.inp.literal.Geometry.from_mcnp('1:(3 #(4 5 6):(6:7) #6)')[0]


@pytest.fixture(scope='session')
def geometry_b() -> pymcnp.inp.literal.Geometry:
    return pymcnp.inp.literal.Geometry.from_mcnp('1 3 #4')[0]


@pytest.fixture(scope='session')
def path_inp() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'valid_38.inp'


@pytest.fixture(scope='session')
def path_outp() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'valid_39.outp'


@pytest.fixture(scope='session')
def path_ptrac() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent / 'files' / 'ptrac' / 'valid_38.ptrac'


@pytest.fixture(scope='session')
def inp(path_inp: pathlib.Path) -> pymcnp.Inp:
    return pymcnp.Inp.from_file(path_inp)[0]


@pytest.fixture(scope='session')
def outp(path_outp: pathlib.Path) -> pymcnp.Outp:
    return pymcnp.Outp.from_file(path_outp)[0]


@pytest.fixture(scope='session')
def ptrac(path_ptrac: pathlib.Path) -> pymcnp.Ptrac:
    return pymcnp.Ptrac.from_file(path_ptrac)[0]


@pytest.fixture(scope='session')
def event(ptrac: pymcnp.Ptrac) -> pymcnp.ptrac.Event:
    return next(_events(ptrac))


@pytest.fixture(scope='session')
def head(tmp_path_factory: pytest.TempPathFactory):
    """Makes files with only the header and the first histories of a ptrac file, since parsing whole 1 MB files is slow."""

    directory = tmp_path_factory.mktemp('head')

    def make(name: str, histories: int = 3) -> pathlib.Path:
        path = directory / f'{histories}_{name}'
        if not path.exists():
            lines = (pathlib.Path(__file__).parent.parent / 'files' / 'ptrac' / name).read_text().split('\n')
            # History lines, as in `Ptrac.iter_histories`: after the header, a number then the first event type.
            starts = [i for i, line in enumerate(lines) if i >= 6 and re.match(r' *\d+ +(?:[1345]000|-?20\d\d)(?: |$)', line)]
            assert starts or len(lines) <= 9, f'no histories found in {name}'  # else a header only
            path.write_text('\n'.join(lines[: starts[histories]]) + '\n' if len(starts) > histories else '\n'.join(lines))
        return path

    return make


@pytest.fixture(scope='session')
def valid_27(head) -> pathlib.Path:
    return head('valid_27.ptrac', 4)
