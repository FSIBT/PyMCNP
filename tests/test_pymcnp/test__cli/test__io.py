import pathlib

import pytest

from pymcnp._cli import _io


@pytest.mark.parametrize(
    'path, ext, i, expected',
    [
        ('run/example_00.outp', 'csv', None, 'run/example_00.csv'),
        ('run/example_00.inp', 'pdf', 'cells', 'run/example_00-cells.pdf'),
        ('run/a.b.outp', 'csv', None, 'run/a.b.csv'),
        # MCNP's default output names have no extension.
        ('run/outp', 'csv', None, 'run/outp.csv'),
        ('run/ptrac', 'parquet', None, 'run/ptrac.parquet'),
        ('outp', 'pdf', None, 'outp.pdf'),
        ('run.d/meshtal', 'csv', None, 'run.d/meshtal.csv'),
        (pathlib.Path('run.d/inp'), 'pdf', 'surface_1', 'run.d/inp-surface_1.pdf'),
    ],
)
def test_get_outfile(path, ext, i, expected) -> None:
    assert _io.get_outfile(path, ext, i) == pathlib.Path(expected)
