"""
Makes the images in ``docs/source/images`` from the example files, without MCNP or a display.

Run ``python docs/make_images.py`` (all images) or, e.g., ``python docs/make_images.py do_plot cli_check``. It needs the ``docs`` extra and ``pymcnp``
installed. PyVista renders off screen and matplotlib uses the Agg backend.
"""

import io
import os
import sys
import pathlib
import tempfile
import subprocess

import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot
import numpy
import pyvista
import rich.console
import rich.text

import pymcnp

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / 'examples'
FILES = ROOT / 'files'
IMAGES = ROOT / 'docs' / 'source' / 'images'

pyvista.OFF_SCREEN = True

# An input with a data line wider than 80 columns, for ``pymcnp check --diff``.
SPHERE = """Water sphere
1 1 -1.0 -1 imp:n=1
2 0 1 imp:n=0

1 so 10

m1 1001 2 8016 1
sdef erg=14
f4:n 1
e4 0.1 0.2 0.5 1 2 5 10 12 13 14 14.1 14.2 14.3 14.4 14.5 14.6 14.7 14.8 14.9 15 16 17
nps 1000

"""


def screenshot(plotter: pyvista.Plotter, name: str, camera=None, size=(900, 650)) -> None:
    plotter.set_background('white')
    plotter.window_size = size
    if camera is not None:
        plotter.camera_position = camera
    plotter.screenshot(str(IMAGES / name))
    plotter.close()
    print(IMAGES / name)


def do_plot() -> None:
    """The figures of ``Plot().to_show`` for tally 1 of ``example_00.outp`` (``examples/do_plot.py``), as one image."""

    outp, _ = pymcnp.Outp.from_file(EXAMPLES / 'example_00.outp')
    figures = pymcnp.Plot().to_show(outp, '1')
    columns = 3
    rows = -(-len(figures) // columns)
    grid, axes = matplotlib.pyplot.subplots(rows, columns, figsize=(4 * columns, 3 * rows))

    for axis in axes.flat:
        axis.axis('off')

    for axis, figure in zip(axes.flat, figures):
        buffer = io.BytesIO()
        figure.savefig(buffer, format='png', dpi=80)
        buffer.seek(0)
        axis.imshow(matplotlib.pyplot.imread(buffer))

    grid.tight_layout(pad=0.2)
    grid.savefig(IMAGES / 'do_plot.png', dpi=80)
    matplotlib.pyplot.close('all')
    print(IMAGES / 'do_plot.png')


def do_visualize() -> None:
    """``Visualize().to_show_surfaces(inp, skip=(1, 3))`` of ``example_05.inp`` (``examples/do_visualize.py``)."""

    inp, _ = pymcnp.Inp.from_file(EXAMPLES / 'example_05.inp')
    plotter = pymcnp.Visualize().to_show_surfaces(inp, skip=(1, 3))
    plotter.show_bounds(grid='back', location='outer', color='black')
    plotter.camera.zoom(0.8)
    screenshot(plotter, 'do_visualize.png')


def do_parameter_scan() -> None:
    """The five inputs of ``examples/do_parameter_scan.py`` in one view: the sphere moves along y, the box stays."""

    inp, _ = pymcnp.Inp.from_file(EXAMPLES / 'example_04.inp')
    inps = tuple(inp.scan(**{'surfaces[11].vy': [-2, -1, 0, 1, 2]}))
    plotter = pyvista.Plotter()
    plotter.add_axes()
    colors = matplotlib.colormaps['viridis']

    for index, scanned in enumerate(inps):
        sphere = scanned.surfaces[0]
        plotter.add_mesh(sphere.to_show().surface, color=colors(index / (len(inps) - 1)), opacity=0.8)
        plotter.add_point_labels([(float(sphere.vx), float(sphere.vy), float(sphere.r) + 0.3)], [f'vy = {sphere.vy}'], font_size=14, shape=None, always_visible=True)

    plotter.add_mesh(inp.surfaces[1].to_show().surface, color='lightgray', opacity=0.6)
    plotter.show_bounds(grid='back', location='outer', color='black', xtitle='x', ytitle='y', ztitle='z')
    screenshot(plotter, 'do_parameter_scan.png', camera=[(9, -9, 8), (2.5, 0, 0), (0, 0, 1)])


def getting_started_surfaces() -> None:
    """The two detectors of ``example_00.inp``, as ``pymcnp visualize -s 2,3 example_00.inp`` shows them."""

    inp, _ = pymcnp.Inp.from_file(EXAMPLES / 'example_00.inp')
    plotter = pymcnp.Visualize().to_show_surface(inp, 2, 3)
    plotter.add_point_labels([(32.0, 0.0, 13.0), (-60.0, 0.0, 10.0)], ['surface 2 (LaBr3)', 'surface 3 (CeBr3)'], font_size=20, shape=None, always_visible=True)
    plotter.add_mesh(pyvista.Line((-70.0, 0.0, 0.0), (66.0, 0.0, 0.0)), color='gray')
    plotter.add_point_labels([(66.0, 0.0, 0.0)], ['x'], font_size=18, shape=None, always_visible=True)
    screenshot(plotter, 'getting_started_surfaces.png', camera=[(0, -105, 40), (0, 0, 3), (0, 0, 1)], size=(900, 380))


def getting_started_tally() -> None:
    """Tally 1 of ``example_00.outp``, plotted with the code shown on the Getting Started page."""

    outp, _ = pymcnp.Outp.from_file(EXAMPLES / 'example_00.outp')
    tally = outp.tally(1)
    spectra = tally.groupby(['surface', 'facet', 'bins'], as_index=False)['counts'].sum()  # add up the two angle bins

    figure, axis = matplotlib.pyplot.subplots(figsize=(7, 4))
    for (surface, facet), rows in spectra.groupby(['surface', 'facet']):
        edges = numpy.concatenate(([0.0], rows['bins']))  # the bins are upper edges; the first bin starts at 0
        axis.stairs(rows['counts'], edges, label=f'surface {surface}.{facet}')
    axis.set_yscale('log')
    axis.set_xlabel('Energy (MeV)')
    axis.set_ylabel('Photons per source neutron')
    axis.legend()
    figure.tight_layout()
    figure.savefig(IMAGES / 'getting_started_tally.png', dpi=90)
    matplotlib.pyplot.close('all')
    print(IMAGES / 'getting_started_tally.png')


def cli(name: str, *arguments: str, cwd: pathlib.Path = EXAMPLES) -> None:
    """The rich output of ``pymcnp <arguments>`` as SVG (standard output only)."""

    environment = dict(os.environ, COLUMNS='88', FORCE_COLOR='1', TERM='xterm-256color')
    done = subprocess.run([sys.executable, '-m', 'pymcnp._cli.main', *arguments], cwd=cwd, env=environment, capture_output=True, text=True)
    console = rich.console.Console(record=True, width=88, file=io.StringIO(), force_terminal=True)
    console.print(rich.text.Text.from_ansi(done.stdout.rstrip('\n')))
    title = f'pymcnp {" ".join(arguments)}   (exit code {done.returncode})'
    console.save_svg(str(IMAGES / name), title=title)
    print(IMAGES / name, done.returncode)


def cli_check() -> None:
    """``pymcnp check`` with exit code 0, ``pymcnp check --diff`` with exit code 1, and ``pymcnp check`` with exit code 3."""

    cli('cli_check_ok.svg', 'check', 'example_00.inp')
    # ``files/inp/todo_13.inp`` has a lattice card PyMCNP cannot parse yet (line 5, ``2(3)`` in a ``fill`` array), the usual case: a valid card of
    # MCNP that PyMCNP does not know; ``check`` names the line.
    cli('cli_check_unparsed.svg', 'check', 'todo_13.inp', cwd=FILES / 'inp')
    with tempfile.TemporaryDirectory() as directory:
        directory = pathlib.Path(directory)
        (directory / 'sphere.inp').write_text(SPHERE)
        cli('cli_check_diff.svg', 'check', '--diff', 'sphere.inp', cwd=directory)


MAKERS = (do_plot, do_visualize, do_parameter_scan, getting_started_surfaces, getting_started_tally, cli_check)

if __name__ == '__main__':
    # Makes all images, or only those whose function names are given as arguments.
    IMAGES.mkdir(exist_ok=True)
    for maker in MAKERS:
        if len(sys.argv) == 1 or maker.__name__ in sys.argv[1:]:
            maker()
