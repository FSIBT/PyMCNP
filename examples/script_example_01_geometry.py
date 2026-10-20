"""
Neutron source -> iron cube -> NaI gamma detector, over a concrete floor.

Coordinates (cm): origin at the neutron source, z up, detector axis in the
x-z plane. Writes one MCNP input per value of NPS (logspace 1e2..1e4, 20 steps),
numbered 0.inp .. 19.inp. `script_example_01_run.py` generates, runs and post-processes them.
The PTRAC card records every neutron and photon event with full phase space
(WRITE=ALL), so a photon's position, direction, energy and originating isotope
can be recovered from the file afterwards.

    python script_example_01_geometry.py [output_dir]
"""

import math
import pathlib
import sys

import numpy as np
import pymcnp
from pymcnp.inp import card
from pymcnp.inp.card import data, surface

OUTPUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'script_example_01_output')
SEED = 1232209489
LIB = '80c'

# --- Geometry parameters (cm) ----------------------------------------------
SOURCE_ENERGY = 14.1  # MeV
CONE_RADIUS, CONE_HEIGHT = 25.0, 100.0  # 50 cm diameter at 1 m
CUBE_SIDE, CUBE_Z = 10.0, -25.0  # iron cube centre below the source
FLOOR_TOP, FLOOR_THICK, FLOOR_WIDTH = -100.0, 200.0, 500.0
WORLD_RADIUS = 500.0  # 10 m diameter
DET_DISTANCE, DET_ELEVATION = 30.0, 30.0  # iron centre -> detector front face, deg
DET_RADIUS, DET_LENGTH = 3.81, 7.62  # ASSUMED: 3"x3" NaI(Tl) cylinder

# --- Derived detector placement ----------------------------------------------
elev = math.radians(DET_ELEVATION)
axis = (math.cos(elev), 0.0, math.sin(elev))  # unit vector, tilted up from +x
front = tuple(c * DET_DISTANCE + o for c, o in zip(axis, (0.0, 0.0, CUBE_Z)))

# --- Surfaces ------------------------------------------------------------------
h = CUBE_SIDE / 2
w = FLOOR_WIDTH / 2
s_iron = surface.Rpp(j=1, xmin=-h, xmax=h, ymin=-h, ymax=h, zmin=CUBE_Z - h, zmax=CUBE_Z + h)
s_floor = surface.Rpp(j=2, xmin=-w, xmax=w, ymin=-w, ymax=w, zmin=FLOOR_TOP - FLOOR_THICK, zmax=FLOOR_TOP)
s_det = surface.Rcc(
    j=3,
    vx=front[0], vy=front[1], vz=front[2],
    h1=axis[0] * DET_LENGTH, h2=axis[1] * DET_LENGTH, h3=axis[2] * DET_LENGTH,
    r=DET_RADIUS,
)  # fmt: skip
s_world = surface.So(j=99, r=WORLD_RADIUS)

# --- Materials -------------------------------------------------------------------
# This xsdir only has isotopic ENDF/B-VII.1 (.80c) tables and lacks 6012.80c and
# 8018.80c, which M.from_formula would emit for minor constituents at a low cutoff.
# The cutoffs below drop nuclides under that mass/atom fraction (MCNP renormalises).
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
m_nai = data.M.from_formula(suffix=3, formulas={'NaI': 1}, is_weight=False, library=LIB)
m_air = data.M.from_formula(suffix=4, formulas={'N2': 0.8, 'O2': 0.2}, is_weight=False, library=LIB)

# --- Cells ---------------------------------------------------------------------
imp = 'imp:n,p=1'
c_iron = card.Cell_0(j=1, m=1, d=-7.874, geom=-s_iron, options=[imp])
c_floor = card.Cell_0(j=2, m=2, d=-2.3, geom=-s_floor, options=[imp])
c_det = card.Cell_0(j=3, m=3, d=-3.67, geom=-s_det, options=[imp])
c_air = card.Cell_0(j=4, m=4, d=-0.001205, geom=-s_world & +s_iron & +s_floor & +s_det, options=[imp])
c_out = card.Cell_1(j=5, m=0, geom=+s_world, options=['imp:n,p=0'])

# --- Source: 14.1 MeV point source, uniform in a downward cone -----------------
# DIR is the cosine of the angle to VEC; the cone half-angle is atan(R/H).
cos_max = CONE_HEIGHT / math.hypot(CONE_HEIGHT, CONE_RADIUS)
sdef = data.Sdef(options=['POS=0 0 0', 'VEC=0 0 -1', 'DIR=D1', f'ERG={SOURCE_ENERGY}', 'PAR=1'])
si1 = data.Si.from_mcnp(f'SI1 {cos_max:.8f} 1\n')[0]
sp1 = data.Sp.from_mcnp('SP1 0 1\n')[0]  # uniform in cosine = uniform in solid angle

# --- Event record -----------------------------------------------------------------
# WRITE=ALL stores x y z u v w erg wgt time for each event. No EVENT/CELL filter, so
# neutron collisions (nuclide ZAID) and photon creation are in the file, which the
# photon's originating isotope needs. SURFACE=3.1 3.2 3.3 would not parse (see report).
# Order matters: pymcnp's PTRAC parser stops at `WRITE=` if it follows `TYPE=`.
# Warning: ~20 kB per history, so the 1e4 case writes a PTRAC file of about 200 MB.
ptrac = data.Ptrac.from_mcnp('PTRAC FILE=ASC WRITE=ALL TYPE=N,P MAX=1000000000\n')[0]
mode = data.Mode(p=['N', 'P'])

base = pymcnp.Inp(
    title='14.1 MeV cone source, Fe cube, NaI detector, concrete floor\n',
    cells=[c_iron, c_floor, c_det, c_air, c_out],
    surfaces=[s_iron, s_floor, s_det, s_world],
    data=[mode, m_iron, m_concrete, m_nai, m_air, sdef, si1, sp1, ptrac],
)
base.seed = SEED

# --- One file per NPS ------------------------------------------------------------
NPS_VALUES = np.logspace(2, 4, 20).round().astype(int)  # 1e2 .. 1e4, 20 steps
assert len(set(NPS_VALUES)) == 20


if __name__ == '__main__':
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for index, inp in enumerate(base.scan(nps=[int(n) for n in NPS_VALUES])):
        inp.to_file(OUTPUT / f'{index}.inp')
