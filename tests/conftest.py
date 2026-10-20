import pathlib

import pytest

import pymcnp


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
    return pymcnp.inp.card.Cell_2(j=2, n=1, options='rho=3.1')


@pytest.fixture(scope='session')
def surface_a() -> pymcnp.inp.card.Surface:
    return pymcnp.inp.card.surface.So(j='101', r='1')


@pytest.fixture(scope='session')
def surface_b() -> pymcnp.inp.card.Surface:
    return pymcnp.inp.card.surface.Rpp(j='102', xmin='0', xmax='1', ymin='0', ymax='1', zmin='0', zmax='1')


@pytest.fixture(scope='session')
def geometry_a() -> pymcnp.inp.literal.Geometry:
    return pymcnp.inp.literal.Geometry.from_mcnp('1:(3 #(4 5 6):(6:7) #6)')[0]


@pytest.fixture(scope='session')
def geometry_b() -> pymcnp.inp.literal.Geometry:
    return pymcnp.inp.literal.Geometry.from_mcnp('1 3 #4')[0]


@pytest.fixture(scope='session')
def a_shape() -> pymcnp.abc.Visualization:
    return pymcnp._show.pyvista.Sphere(0.5)


@pytest.fixture(scope='session')
def b_shape() -> pymcnp.abc.Visualization:
    return pymcnp._show.pyvista.Sphere(1)


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


@pytest.fixture(scope='session')
def check(path_inp: pathlib.Path) -> pymcnp.Check:
    return pymcnp.Check(path_inp)


@pytest.fixture(scope='session')
def convert(outp: pymcnp.Outp) -> pymcnp.Convert:
    return pymcnp.Convert(outp)


@pytest.fixture(scope='session')
def plot(outp: pymcnp.Outp) -> pymcnp.Plot:
    return pymcnp.Plot(outp)


@pytest.fixture(scope='session')
def run(inp: pymcnp.Inp) -> pymcnp.Run:
    return pymcnp.Run((inp,), command='echo')


@pytest.fixture(scope='session')
def visualize(inp: pymcnp.Inp) -> pymcnp.Visualize:
    return pymcnp.Visualize(inp)
