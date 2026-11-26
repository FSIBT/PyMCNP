import os
import sys
import shutil
import pathlib
import subprocess

import pytest

from .executables import fake_executable

EXAMPLES = pathlib.Path(__file__).parent.parent / 'examples'

# Starts an example the way a user would, but without windows or the default mesh resolution.
DRIVER = """
import sys, runpy, pyvista, pymcnp
pyvista.OFF_SCREEN = True
pymcnp._show.pyvista.RESOLUTION = 24
pyvista.Plotter.show = lambda self, *args, **kwargs: None
name = sys.argv[1]
sys.argv = sys.argv[1:]
sys.path.insert(0, '.')
runpy.run_path(name, run_name='__main__')
"""

# Examples that need neither MCNP nor a display. Each is run in a temporary copy of ``examples/``.
RUNNABLE = [
    'create_cell.py',
    'create_inp.py',
    'create_material.py',
    'create_surface.py',
    'do_check.py',
    'do_convert.py',
    'do_parameter_scan.py',
    'do_plot.py',
    'do_run.py',
    'home.py',
    'read_cell.py',
    'read_inp.py',
    'read_material.py',
    'read_outp.py',
    'read_ptrac.py',
    'read_surface.py',
    'read_tally1.py',
    'read_tally2.py',
    'read_tally4.py',
    'read_tally8.py',
    'script_example_01_geometry.py',
    'script_example_02_ground_model.py',
]

# Examples that run MCNP itself, and examples that need output files only a real run makes.
NEEDS_MCNP = ['script_example_01_run.py', 'script_example_02_plot_flux.py']


@pytest.fixture
def examples(tmp_path: pathlib.Path) -> pathlib.Path:
    path = tmp_path / 'examples'
    shutil.copytree(EXAMPLES, path, ignore=shutil.ignore_patterns('__pycache__', 'output'))
    return path


def environment(examples: pathlib.Path) -> dict[str, str]:
    # Keeps the caller's environment (e.g. ``DISPLAY`` from a headless X server on CI), but puts
    # this interpreter first on ``PATH``, uses a non-interactive matplotlib backend and isolates
    # ``HOME`` in the temporary copy of ``examples/``.
    env = dict(os.environ)
    env['MPLBACKEND'] = 'Agg'
    env['PATH'] = os.pathsep.join([str(pathlib.Path(sys.executable).parent), '/usr/bin', '/bin'])
    env['HOME'] = str(examples)
    return env


def run(examples: pathlib.Path, name: str, *arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, '-c', DRIVER, name, *arguments],
        cwd=examples,
        env=environment(examples),
        capture_output=True,
        text=True,
    )


def test_environment_keeps_display(tmp_path: pathlib.Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv('DISPLAY', ':99')
    monkeypatch.setenv('MPLBACKEND', 'TkAgg')
    env = environment(tmp_path)
    assert env['DISPLAY'] == ':99'
    assert env['MPLBACKEND'] == 'Agg'
    assert env['HOME'] == str(tmp_path)
    assert env['PATH'].split(os.pathsep)[0] == str(pathlib.Path(sys.executable).parent)


def test_all_examples_are_listed() -> None:
    names = {path.name for path in EXAMPLES.glob('*.py')}
    assert names == set(RUNNABLE) | set(NEEDS_MCNP) | {'do_visualize.py', 'script_example_01_ptrac_to_parquet.py', 'script_example_02_plot_setup.py'}


@pytest.mark.parametrize('name', RUNNABLE)
def test_example(examples: pathlib.Path, name: str) -> None:
    done = run(examples, name)
    assert done.returncode == 0, done.stderr


@pytest.mark.render
def test_visualize(examples: pathlib.Path) -> None:
    done = run(examples, 'do_visualize.py')
    assert done.returncode == 0, done.stderr
    assert (examples / 'output' / 'example_05-surfaces.pdf').exists()


@pytest.mark.render
def test_plot_setup(examples: pathlib.Path) -> None:
    done = run(examples, 'script_example_02_plot_setup.py')
    assert done.returncode == 0, done.stderr
    assert (examples / 'script_example_02_output' / 'setup.png').exists()


def test_ptrac_to_parquet(examples: pathlib.Path) -> None:
    done = run(examples, 'script_example_01_ptrac_to_parquet.py', 'example_01.ptrac', 'out.parquet')
    assert done.returncode == 0, done.stderr
    assert (examples / 'out.parquet').exists()
    assert 'photons' in done.stdout


def test_ptrac_to_parquet_uses_path(examples: pathlib.Path) -> None:
    done = run(examples, 'script_example_01_ptrac_to_parquet.py', 'missing.ptrac', 'out.parquet')
    assert done.returncode != 0
    assert 'missing.ptrac' in done.stderr


def test_example_01_run_cases(examples: pathlib.Path) -> None:
    """Runs ``script_example_01_run`` with a fake MCNP that writes a PTRAC file."""

    fake = fake_executable(
        examples / 'fake-mcnp',
        'import sys, shutil\n'
        'arguments = dict(argument.split("=", 1) for argument in sys.argv[1:])\n'
        f'shutil.copy({str(examples / "example_01.ptrac")!r}, arguments["ptrac"])\n'
        'open(arguments["outp"], "w").write("ok\\n")\n',
    )
    script = examples / 'script_example_01_run.py'
    assert "command='mcnp6'" in script.read_text()
    script.write_text(script.read_text().replace("command='mcnp6'", f'command={fake!r}'))
    done = run(examples, 'script_example_01_run.py')
    assert done.returncode == 0, done.stderr
    assert sorted(path.name for path in examples.glob('script_example_01_output/*/*.parquet')) == sorted(f'{n}.parquet' for n in range(20))


def test_readme_example(examples: pathlib.Path) -> None:
    """Runs the Python code of the README on the example files."""

    text = (EXAMPLES.parent / 'README.md').read_text()
    code = text.split('```python\n')[1].split('```')[0]
    (examples / 'readme.py').write_text(code)
    done = run(examples, 'readme.py')
    assert done.returncode == 0, done.stderr
    assert len(list(examples.glob('sphere-*.inp'))) == 3


# A one-plane mesh tally like the FMESH of script_example_02, with the header of a real meshtal file.
MESHTAL_2D = ''.join((EXAMPLES.parent / 'files' / 'meshtal' / 'multi_00.meshtal').read_text().splitlines(keepends=True)[:3])
MESHTAL_2D += """
 Mesh Tally Number         4
 neutron  mesh tally.

 Tally bin boundaries:
    X direction:    -20.00    -10.00      0.00     10.00
    Y direction:    -20.00    -10.00      0.00     10.00
    Z direction:     29.00     31.00
    Energy bin boundaries: 0.00E+00 1.00E+36

        X         Y         Z     Result     Rel Error
"""
for x in (-15.0, -5.0, 5.0):
    for y in (-15.0, -5.0, 5.0):
        MESHTAL_2D += f'   {x:8.3f}  {y:8.3f}    30.000 {1e-3 * (2 + x / 20 + y / 40):.5E} {0.1:.5E}\n'


def test_example_02_automate_workflow(examples: pathlib.Path) -> None:
    """Follows docs/source/examples/automate.md with a fake ``mcnp6`` on ``PATH`` that writes a meshtal."""

    fakebin = examples / 'fakebin'
    fakebin.mkdir()
    (examples / 'fake.meshtal').write_text(MESHTAL_2D)
    fake_executable(
        fakebin / 'mcnp6',
        'import sys, shutil\n'
        'arguments = dict(argument.split("=", 1) for argument in sys.argv[1:])\n'
        f'shutil.copy({str(examples / "example_00.outp")!r}, arguments["outp"])\n'
        f'shutil.copy({str(examples / "fake.meshtal")!r}, "meshtal")\n',
    )
    env = environment(examples)
    env['PATH'] = os.pathsep.join([str(fakebin), env['PATH']])

    done = run(examples, 'script_example_02_ground_model.py')
    assert done.returncode == 0, done.stderr

    # The command of automate.md.
    command = [str(pathlib.Path(sys.executable).parent / 'pymcnp'), 'run', '-p', 'script_example_02_output/run', 'script_example_02_output/ground.inp']
    done = subprocess.run(command, cwd=examples, env=env, capture_output=True, text=True)
    assert done.returncode == 0, done.stdout + done.stderr
    assert len(list(examples.glob('script_example_02_output/run/pymcnp-*/run-00000/meshtal'))) == 1

    done = run(examples, 'script_example_02_plot_flux.py')
    assert done.returncode == 0, done.stderr
    assert (examples / 'script_example_02_output' / 'flux.png').exists()


def test_example_02_plot_flux_without_run(examples: pathlib.Path) -> None:
    done = run(examples, 'script_example_02_plot_flux.py')
    assert done.returncode != 0
    assert 'pymcnp run' in done.stderr
    assert 'IndexError' not in done.stderr


def test_example_02_plot_flux_given_path(examples: pathlib.Path) -> None:
    # A meshtal from elsewhere, before script_example_02_output/ exists.
    (examples / 'given.meshtal').write_text(MESHTAL_2D)
    shutil.rmtree(examples / 'script_example_02_output', ignore_errors=True)

    done = run(examples, 'script_example_02_plot_flux.py', 'given.meshtal')

    assert done.returncode == 0, done.stderr
    assert (examples / 'script_example_02_output' / 'flux.png').exists()
