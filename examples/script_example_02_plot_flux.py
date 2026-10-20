"""2D heatmap of the FMESH neutron flux at z = 30 cm, saved to script_example_02_output/flux.png.

python script_example_02_ground_model.py
pymcnp run -p script_example_02_output/run script_example_02_output/ground.inp
python script_example_02_plot_flux.py [meshtal_path]
"""

import glob
import pathlib
import sys

import matplotlib
import numpy as np
import pymcnp
from matplotlib import pyplot
from matplotlib.colors import LogNorm
from matplotlib.patches import Rectangle

matplotlib.use('Agg')
path = sys.argv[1] if len(sys.argv) > 1 else glob.glob('script_example_02_output/run/*/ground/meshtal')[0]

(tally,) = pymcnp.Meshtal.iter_tallies(path)
frame = tally.to_dataframe()
xs, ys = np.sort(frame.X.unique()), np.sort(frame.Y.unique())
shape = (len(ys), len(xs))
flux = frame.sort_values(['Y', 'X']).Result.to_numpy().reshape(shape)  # rows = y, columns = x
error = frame.sort_values(['Y', 'X']).loc[:, 'Rel Error'].to_numpy().reshape(shape)
step = xs[1] - xs[0]
extent = (xs[0] - step / 2, xs[-1] + step / 2, ys[0] - step / 2, ys[-1] + step / 2)

figure, axes = pyplot.subplots(1, 2, figsize=(15, 6.5), constrained_layout=True)
for ax, data, label, kwargs in (
    (axes[0], np.ma.masked_less_equal(flux, 0), 'neutron flux (n cm$^{-2}$ per source neutron)', {'norm': LogNorm(*np.percentile(flux[flux > 0], (2, 99.5))), 'cmap': 'inferno'}),
    (axes[1], error, 'relative error', {'cmap': 'viridis', 'vmin': 0, 'vmax': 1}),
):
    image = ax.imshow(data, origin='lower', extent=extent, interpolation='nearest', **kwargs)
    ax.add_patch(Rectangle((-100, -100), 200, 200, fill=False, ec='white', ls='--', lw=1))  # iron disc array
    ax.plot(0, 0, marker='*', color='cyan', ms=12, mec='k')  # source below this point
    ax.set(xlabel='x (cm)', ylabel='y (cm)', aspect='equal')
    figure.colorbar(image, ax=ax, label=label, shrink=0.85)
axes[0].set_title(f'Neutron flux at z = 30 cm, {step:.0f} cm bins')
axes[1].set_title('Statistical error (dashed: disc array, star: source axis)')
output = pathlib.Path('script_example_02_output/flux.png')
figure.savefig(output, dpi=150)
print(output, f'total={flux.sum():.3e}', f'mean rel err={error.mean():.2f}')
