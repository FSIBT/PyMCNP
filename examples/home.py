import pathlib

import numpy as np

import pymcnp

rng = np.random.default_rng(20260101)

surfaces, cells = [], []
for ix in range(-10, 11):
    for iy in range(-10, 11):
        x, y, thick = ix * 10.0, iy * 10.0, float(rng.uniform(1, 10))

        disc = pymcnp.inp.card.surface.Rcc(j=len(surfaces) + 1, vx=x, vy=y, vz=50.0, h1=0.0, h2=0.0, h3=thick, r=4.0)
        cell = pymcnp.inp.card.Cell_0(j=len(cells) + 1, m=1, d=-7.874, geom=-disc, options=['imp:n=1'])

        surfaces.append(disc)
        cells.append(cell)

# ... air, ground, source and FMESH tally, then inp.to_file('ground.inp')

# After `pymcnp run`: one row per mesh voxel.

path = pathlib.Path('example.meshtal')
if path.exists():
    tally = next(pymcnp.Meshtal.iter_tallies(path))
    frame = tally.to_dataframe()
