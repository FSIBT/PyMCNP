import cadquery as cq

surface_2 = cq.Workplane().polyline([(-0.5, -0.5, 0.0), (0.5, -0.5, 0.0), (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0)]).close().polyline([(-0.5, -0.5, 1.0), (0.5, -0.5, 1.0), (0.5, 0.5, 1.0), (-0.5, 0.5, 1.0)]).close().loft()
surface_3 = cq.Workplane().box(1.0, 1.0, 1.0).translate((0.0, 0.0, 2.5))
surface_4 = cq.Workplane().sphere(0.5).translate((0.0, 0.0, 4.5))
surface_5 = cq.Workplane().cylinder(1.0, 0.5).translate((0.0, 0.0, 6.5))
surface_6 = cq.Workplane().sketch().regularPolygon(0.5773502691896258, 6).finalize().extrude(1.0).translate((0.0, 0.0, 8.0))
surface_7 = cq.Workplane().ellipse(0.5, 0.25).extrude(1.0).translate((0.0, 0.0, 10.0))
surface_8 = cq.Workplane().circle(0.5).workplane(offset=1.0).circle(0.25).loft().translate((0.0, 0.0, 12.0))
surface_9 = cq.Workplane().ellipseArc(0.25, 0.5, -90, 90).close().revolve(axisStart=(0, -0.5, 0), axisEnd=(0, 0.5, 0)).translate((0.0, -0.5, 14.5)).rotate((0.0, 0.0, 15.0), (0.0, 0.0, 14.0), 90.0)
surface_10 = cq.Workplane().polyline([(0.0, 1.0, 0.0), (0, 0, 0), (1.0, 0.0, 0.0)]).close().polyline([(0.0, 1.0, 1.0), (0.0, 0.0, 1.0), (1.0, 0.0, 1.0)]).close().loft().translate((-0.5, -0.5, 16.0))

surfaces = cq.Workplane().add(surface_2).add(surface_3).add(surface_4).add(surface_5).add(surface_6).add(surface_7).add(surface_8).add(surface_9).add(surface_10)

