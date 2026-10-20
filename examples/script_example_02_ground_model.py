"""
Isotropic neutron source 1 m above a rough concrete ground with an array of iron discs
at 50 cm, and a 2 cm resolution FMESH flux tally at 30 cm height.

Coordinates (cm): z up, ground tile bottoms at z=-100, nominal ground level z=0.
  * ground: 15 x 15 columns of 20x20 cm concrete tiles covering -150..150 in x and y,
    tile top random in 0..10 cm (air fills the rest of the column up to z=10)
  * discs: iron cylinders r=4 cm, bases at z=50, thickness random 1..10 cm, centres every
    10 cm over -100..100 in x and y (21 x 21, one at 0/0)
  * source: point, isotropic, 14.1 MeV (ASSUMED energy) at z=100
  * FMESH4:N: x,y from -150 to 150 in 2 cm bins, one 2 cm layer z=29..31 (centred at 30)
"""

import pathlib
import sys

import numpy as np
import pymcnp
from pymcnp.inp import card
from pymcnp.inp.card import data, surface

OUTPUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'script_example_02_output/ground.inp')
SEED = 20260101  # geometry randomness, reproducible
LIB = '80c'
SOURCE_Z, SOURCE_ENERGY = 100.0, 14.1
TILE, TILE_N, GROUND_BOTTOM, GROUND_MAX = 20.0, 15, -100.0, 10.0
DISC_PITCH, DISC_HALF_N, DISC_Z, DISC_R, DISC_HMIN, DISC_HMAX = 10.0, 10, 50.0, 4.0, 1.0, 10.0
MESH_HALF, MESH_BIN, MESH_Z, MESH_THICK = 150.0, 2.0, 30.0, 2.0
WORLD_R = 600.0

rng = np.random.default_rng(SEED)
imp = 'imp:n=1'
surfaces, cells = [], []
tile_surfaces, disc_surfaces = [], []  # for plotting

# --- Ground: columns of tile + air cap -------------------------------------
half = TILE * TILE_N / 2
env = surface.Rpp(j=1, xmin=-half, xmax=half, ymin=-half, ymax=half, zmin=GROUND_BOTTOM, zmax=GROUND_MAX)
world = surface.So(j=2, r=WORLD_R)
surfaces += [env, world]
j_surf, j_cell = 100, 1
for ix in range(TILE_N):
    for iy in range(TILE_N):
        x0, y0 = -half + ix * TILE, -half + iy * TILE
        top = float(rng.uniform(0.0, GROUND_MAX))
        body = surface.Rpp(j=j_surf, xmin=x0, xmax=x0 + TILE, ymin=y0, ymax=y0 + TILE, zmin=GROUND_BOTTOM, zmax=top)
        column = surface.Rpp(j=j_surf + 1, xmin=x0, xmax=x0 + TILE, ymin=y0, ymax=y0 + TILE, zmin=GROUND_BOTTOM, zmax=GROUND_MAX)
        surfaces += [body, column]
        tile_surfaces.append(body)
        cells.append(card.Cell_0(j=j_cell, m=2, d=-2.3, geom=-body, options=[imp]))  # concrete tile
        cells.append(card.Cell_0(j=j_cell + 1, m=4, d=-0.001205, geom=-column & +body, options=[imp]))  # air above it
        j_surf, j_cell = j_surf + 2, j_cell + 2

# --- Iron discs, each in its own 10x10 cm air pillar -------------------------
# (a single air cell excluding all 441 discs is too long for pymcnp's parser, see report)
n_disc = 2 * DISC_HALF_N + 1
slab_half = DISC_PITCH * n_disc / 2
slab = surface.Rpp(j=3, xmin=-slab_half, xmax=slab_half, ymin=-slab_half, ymax=slab_half, zmin=DISC_Z, zmax=DISC_Z + DISC_HMAX)
surfaces.append(slab)
for ix in range(-DISC_HALF_N, DISC_HALF_N + 1):
    for iy in range(-DISC_HALF_N, DISC_HALF_N + 1):
        x0, y0, h = ix * DISC_PITCH, iy * DISC_PITCH, DISC_PITCH / 2
        thick = float(rng.uniform(DISC_HMIN, DISC_HMAX))
        pillar = surface.Rpp(j=j_surf, xmin=x0 - h, xmax=x0 + h, ymin=y0 - h, ymax=y0 + h, zmin=DISC_Z, zmax=DISC_Z + DISC_HMAX)
        disc = surface.Rcc(j=j_surf + 1, vx=x0, vy=y0, vz=DISC_Z, h1=0.0, h2=0.0, h3=thick, r=DISC_R)
        surfaces += [pillar, disc]
        disc_surfaces.append(disc)
        cells.append(card.Cell_0(j=j_cell, m=1, d=-7.874, geom=-disc, options=[imp]))
        cells.append(card.Cell_0(j=j_cell + 1, m=4, d=-0.001205, geom=-pillar & +disc, options=[imp]))
        j_surf, j_cell = j_surf + 2, j_cell + 2

# --- Air everywhere else, and the outside ---------------------------------
cells.append(card.Cell_0(j=j_cell, m=4, d=-0.001205, geom=-world & +env & +slab, options=[imp]))
cells.append(card.Cell_1(j=j_cell + 1, m=0, geom=+world, options=['imp:n=0']))

# --- Materials, source, tally ---------------------------------------------
m_iron = data.M.from_formula(suffix=1, formulas={'Fe': 1}, library=LIB)
m_concrete = data.M.from_formula(  # ordinary concrete (NBS 04), weight fractions
    suffix=2,
    formulas={
        'H': 0.022100, 'C': 0.002484, 'O': 0.574930, 'Na': 0.015208, 'Mg': 0.001266,
        'Al': 0.019953, 'Si': 0.304627, 'K': 0.010045, 'Ca': 0.042951, 'Fe': 0.006435,
    },
    library=LIB,
    cutoff=0.003,
)  # fmt: skip
m_air = data.M.from_formula(suffix=4, formulas={'N2': 0.8, 'O2': 0.2}, is_weight=False, library=LIB)

sdef = data.Sdef(options=[f'POS=0 0 {SOURCE_Z}', f'ERG={SOURCE_ENERGY}', 'PAR=1'])  # isotropic by default
nbin = int(2 * MESH_HALF / MESH_BIN)
fmesh = data.Fmesh.from_mcnp(
    f'FMESH4:N GEOM=REC ORIGIN={-MESH_HALF} {-MESH_HALF} {MESH_Z - MESH_THICK / 2} IMESH={MESH_HALF} IINTS={nbin} JMESH={MESH_HALF} JINTS={nbin} KMESH={MESH_Z + MESH_THICK / 2} KINTS=1\n'
)[0]

inp = pymcnp.Inp(
    title='Neutron source over rough concrete ground with iron discs, FMESH flux at 30 cm\n',
    cells=cells,
    surfaces=surfaces,
    data=[m_iron, m_concrete, m_air, sdef, fmesh],
)
inp.nps = 1_000_000
inp.seed = 1232209489

if __name__ == '__main__':
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    inp.to_file(OUTPUT)
    print(f'{OUTPUT}: {len(cells)} cells, {len(surfaces)} surfaces')
