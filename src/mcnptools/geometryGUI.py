"""
GUI program to look at geometry
"""

import matplotlib.pyplot as plt
from mcnptools import build_geometry as bg

plt.rc('font', size=14)
plt.style.use('seaborn-v0_8-darkgrid')
fig = plt.figure(constrained_layout=True, figsize=(16, 8))
gs = fig.add_gridspec(1, 2, width_ratios=[0.7, 0.3], height_ratios=[1])
ax_3d = fig.add_subplot(gs[0, 0], projection='3d')
ax_menu = fig.add_subplot(gs[0, 1])
ax_menu.set_xticks([])
ax_menu.set_yticks([])

# MCNP file
file_path = 'test_output_files/geom_gui.i'

soil = bg.Geometry(
    color='blue',
    name='Soil',
    h_menu=0,
    fig=fig,
    ax_3d=ax_3d,
    ax_menu=ax_menu,
    soil=True,
)
soil.make_object(x0=0, y0=0, z0=-200, height=150, radius=200, axis='z')

png = bg.Geometry(
    color='green', name='PNG (TR1)', h_menu=0.89, fig=fig, ax_3d=ax_3d, ax_menu=ax_menu
)
png.make_object(x0=0, y0=-30, z0=0, height=30, radius=10, axis='y')

rover = bg.Geometry(
    color='black',
    name='Rover (TR2)',
    h_menu=0.65,
    fig=fig,
    ax_3d=ax_3d,
    ax_menu=ax_menu,
)
rover.make_object(x0=30, y0=-50, z0=0, height=100, radius=12, axis='y')

detector = bg.Geometry(
    color='red',
    name='Detector (TR3)',
    h_menu=0.42,
    fig=fig,
    ax_3d=ax_3d,
    ax_menu=ax_menu,
)
detector.make_object(x0=60, y0=0, z0=0, height=-10, radius=5, axis='z')

gui = bg.Transform(file_path, [soil, png, rover, detector])
