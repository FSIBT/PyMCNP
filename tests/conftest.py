import sys
import pathlib

import pytest

import pymcnp


@pytest.fixture(scope='session')
def pyvista_visualizations() -> tuple[pymcnp._show.pyvista.Visualization, ...]:
    return (pymcnp._show.pyvista.Sphere(0.5), pymcnp._show.pyvista.Sphere(1))


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
import os, sys, pathlib
arguments = dict(argument.split('=', 1) for argument in sys.argv[1:])
pathlib.Path(arguments['outp']).write_text('ok\\n')
os.exit(1)
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
    Path to a stand-in for ``mcnp6`` that writes an output file and exits with 0.
    """

    path = tmp_path / 'fake-mcnp'
    path.write_text(_FAKE_MCNP_FAIL.format(python=sys.executable))
    path.chmod(0o755)
    return str(path)


@pytest.fixture(scope='session')
def integer_a() -> pymcnp.inp.literal.Integer:
    return pymcnp.inp.literal.Integer('1')


@pytest.fixture(scope='session')
def integer_b() -> pymcnp.inp.literal.Integer:
    return pymcnp.inp.literal.Integer('2')


@pytest.fixture(scope='session')
def real_a() -> pymcnp.inp.literal.Real:
    return pymcnp.inp.literal.Real('1.1')


@pytest.fixture(scope='session')
def real_b() -> pymcnp.inp.literal.Real:
    return pymcnp.inp.literal.Real('2.1')


@pytest.fixture(scope='session')
def str_b() -> str:
    return 'a'


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
def event(ptrac: pymcnp.Ptrac) -> pymcnp.ptrac.block.Event:
    return ptrac.histories[0]
