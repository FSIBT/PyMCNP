"""Angled view from above of the ground, iron discs and source (pyvista), saved to script_example_02_output/setup.png."""

import pyvista
import script_example_02_ground_model as g

pyvista.OFF_SCREEN = True
plotter = pyvista.Plotter(window_size=(1800, 1200))
plotter.set_background('white')

for s in g.tile_surfaces:
    box = pyvista.Box(bounds=[float(v) for v in (s.xmin, s.xmax, s.ymin, s.ymax, -15.0, s.zmax)])  # only the top of each column
    plotter.add_mesh(box, color='#b8b2a7', show_edges=True, edge_color='#8a857c', line_width=0.5)
for s in g.disc_surfaces:
    h = float(s.h3)
    disc = pyvista.Cylinder(center=(float(s.vx), float(s.vy), float(s.vz) + h / 2), direction=(0, 0, 1),
                            radius=float(s.r), height=h, resolution=32)
    plotter.add_mesh(disc, color='#c0392b', smooth_shading=True)

source = (0.0, 0.0, g.SOURCE_Z)
plotter.add_mesh(pyvista.Sphere(radius=6, center=source), color='gold')
plotter.add_mesh(pyvista.Line((0, 0, g.GROUND_MAX), source), color='gold', line_width=2)
plotter.add_point_labels([source], ['source (14.1 MeV)'], font_size=26, text_color='black', shape=None, always_visible=True)

mesh = pyvista.Plane(center=(0, 0, g.MESH_Z), i_size=2 * g.MESH_HALF, j_size=2 * g.MESH_HALF)
plotter.add_mesh(mesh, color='#2e86de', style='wireframe', line_width=2, opacity=0.8)  # FMESH outline at 30 cm
plotter.add_axes()
plotter.camera_position = [(420, -420, 330), (0, 0, 40), (0, 0, 1)]
g.OUTPUT.parent.mkdir(parents=True, exist_ok=True)
plotter.screenshot(str(g.OUTPUT.parent / 'setup.png'))
print(g.OUTPUT.parent / 'setup.png')
