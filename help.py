def generate_subsurfaces():
    DATA = [
        (
            "PlaneGeneral",
            "general planes",
            [
                ("a", "Plane equation A coefficent"),
                ("b", "Plane equation B coefficent"),
                ("c", "Plane equation C coefficent"),
                ("d", "PLane equation D coefficent"),
            ],
        ),
        (
            "PlaneNormalX",
            "planes normal to the x-axis",
            [("d", "Plane equation D coefficent")],
        ),
        (
            "PlaneNormalY",
            "planes normal to the y-axis",
            [("d", "Plane equation D coefficent")],
        ),
        (
            "PlaneNormalZ",
            "planes normal to the z-axis",
            [("d", "Plane equation D coefficent")],
        ),
        ("SphereOrigin", "origin-centered spheres", [("r", "Sphere radius")]),
        (
            "SphereGeneral",
            "general spheres",
            [
                ("x", "Sphere center x component"),
                ("y", "Sphere center y component"),
                ("z", "Sphere center z component"),
                ("r", "Sphere radius"),
            ],
        ),
        (
            "SphereNormalX",
            "spheres on x-axis",
            [("x", "Sphere center x component"), ("r", "Sphere radius")],
        ),
        (
            "SphereNormalY",
            "spheres on y-axis",
            [("y", "Sphere center y component"), ("r", "Sphere radius")],
        ),
        (
            "SphereNormalZ",
            "spheres on z-axis",
            [("z", "Sphere center z component"), ("r", "Sphere radius")],
        ),
        (
            "CylinderParallelX",
            "cylinders parallel to x-axis",
            [
                ("y", "Cylinder center y component"),
                ("z", "Cylinder center z component"),
                ("r", "Cylinder radius"),
            ],
        ),
        (
            "CylinderParallelY",
            "cylinders parallel to y-axis",
            [
                ("x", "Cylinder center x component"),
                ("z", "Cylinder center z component"),
                ("r", "Cylinder radius"),
            ],
        ),
        (
            "CylinderParallelZ",
            "cylinders parallel to z-axis",
            [
                ("x", "Cylinder center x component"),
                ("y", "Cylinder center y component"),
                ("r", "Cylinder radius"),
            ],
        ),
        (
            "CylinderOnX",
            "cylinders on x-axis",
            [("x", "Cylinder center x component"), ("r", "Cylinder radius")],
        ),
        (
            "CylinderOnY",
            "cylinders on y-axis",
            [("y", "Cylinder center y component"), ("r", "Cylinder radius")],
        ),
        (
            "CylinderOnZ",
            "cylinders on z-axis",
            [("z", "Cylinder center z component"), ("r", "Cylinder radius")],
        ),
        (
            "ConeParallelX",
            "cones parallel to x-axis",
            [
                ("x", "Cone center x component"),
                ("y", "Cone center y component"),
                ("z", "Cone center z component"),
                ("t_2", "Cone t_2 coefficnet"),
                ("__1", "Cone sheet selector"),
            ],
        ),
        (
            "ConeParallelY",
            "cones parallel to y-axis",
            [
                ("x", "Cone center x component"),
                ("y", "Cone center y component"),
                ("z", "Cone center z component"),
                ("t_2", "Cone t_2 coefficnet"),
                ("__1", "Cone sheet selector"),
            ],
        ),
        (
            "ConeParallelZ",
            "cones parallel to z-axis",
            [
                ("x", "Cone center x component"),
                ("y", "Cone center y component"),
                ("z", "Cone center z component"),
                ("t_2", "Cone t_2 coefficnet"),
                ("__1", "Cone sheet selector"),
            ],
        ),
        (
            "ConeOnX",
            "cones on x-axis",
            [
                ("x", "Cone center x component"),
                ("t_2", "Cone t_2 coefficnet"),
                ("__1", "Cone sheet selector"),
            ],
        ),
        (
            "ConeOnY",
            "cones on y-axis",
            [
                ("y", "Cone center y component"),
                ("t_2", "Cone t_2 coefficnet"),
                ("__1", "Cone sheet selector"),
            ],
        ),
        (
            "ConeOnZ",
            "cones on z-axis",
            [
                ("z", "Cone center z component"),
                ("t_2", "Cone t_2 coefficnet"),
                ("__1", "Cone sheet selector"),
            ],
        ),
        (
            "QuadraticSpecial",
            "special quadratic not parallel to x-, y-, or z- axis",
            [
                ("a", "Quadratic surface equation A coefficent"),
                ("b", "Quadratic surface equation B coefficent"),
                ("c", "Quadratic surface equation C coefficent"),
                ("d", "Quadratic surface equation D coefficent"),
                ("e", "Quadratic surface equation E coefficent"),
                ("f", "Quadratic surface equation F coefficent"),
                ("g", "Quadratic surface equation G coefficent"),
                ("x", "Quadratic center x component"),
                ("y", "Quadratic center y component"),
                ("z", "Quadratic center z component"),
            ],
        ),
        (
            "QuadraticGeneral",
            "general quadratic parallel to x-, y-, or z- axis",
            [
                ("a", "Quadratic surface equation A coefficent"),
                ("b", "Quadratic surface equation B coefficent"),
                ("c", "Quadratic surface equation C coefficent"),
                ("d", "Quadratic surface equation D coefficent"),
                ("e", "Quadratic surface equation E coefficent"),
                ("f", "Quadratic surface equation F coefficent"),
                ("g", "Quadratic surface equation G coefficent"),
                ("h", "Quadratic surface equation H coefficent"),
                ("j", "Quadratic surface equation J coefficent"),
                ("k", "Quadratic surface equation K coefficent"),
            ],
        ),
        (
            "TorusParallelX",
            "tori parallel to x-axis",
            [
                ("x", "Torus center x component"),
                ("y", "Torus center y component"),
                ("z", "Torus center z component"),
                ("a", "Quadratic surface equation A coefficent"),
                ("b", "Quadratic surface equation B coefficent"),
                ("c", "Quadratic surface equation C coefficent"),
            ],
        ),
        (
            "TorusParallelY",
            "tori parallel to y-axis",
            [
                ("x", "Torus center x component"),
                ("y", "Torus center y component"),
                ("z", "Torus center z component"),
                ("a", "Quadratic surface equation A coefficent"),
                ("b", "Quadratic surface equation B coefficent"),
                ("c", "Quadratic surface equation C coefficent"),
            ],
        ),
        (
            "TorusParallelZ",
            "tori parallel to z-axis",
            [
                ("x", "Torus center x component"),
                ("y", "Torus center y component"),
                ("z", "Torus center z component"),
                ("a", "Quadratic surface equation A coefficent"),
                ("b", "Quadratic surface equation B coefficent"),
                ("c", "Quadratic surface equation C coefficent"),
            ],
        ),
        (
            "SurfaceX",
            "point-defined surface symmetric about x-axis",
            [
                ("x1", "Point #1 x component"),
                ("r1", "Point #1 modulus"),
                ("x2", "Point #2 x component"),
                ("r2", "Point #2 modulus"),
                ("x3", "Point #3 x component"),
                ("r3", "Point #3 modulus"),
            ],
        ),
        (
            "SurfaceY",
            "point-defined surface symmetric about x-axis",
            [
                ("y1", "Point #1 x component"),
                ("r1", "Point #1 modulus"),
                ("y2", "Point #2 x component"),
                ("r2", "Point #2 modulus"),
                ("y3", "Point #3 x component"),
                ("r3", "Point #3 modulus"),
            ],
        ),
        (
            "SurfaceZ",
            "point-defined surface symmetric about x-axis",
            [
                ("z1", "Point #1 x component"),
                ("r1", "Point #1 modulus"),
                ("z2", "Point #2 x component"),
                ("r2", "Point #2 modulus"),
                ("z3", "Point #3 x component"),
                ("r3", "Point #3 modulus"),
            ],
        ),
        (
            "PlanePoints",
            "point-defined plane",
            [
                ("x1", "Point #1 x component"),
                ("y1", "Point #1 y component"),
                ("z1", "Point #1 z component"),
                ("x2", "Point #2 x component"),
                ("y2", "Point #2 y component"),
                ("z2", "Point #2 z component"),
                ("x3", "Point #3 x component"),
                ("y3", "Point #3 y component"),
                ("z3", "Point #3 z component"),
            ],
        ),
        (
            "Box",
            "arbitrarily oriented orthogonal box",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobdoy center z component"),
                ("a1x", "1st side vector from coordiante x component"),
                ("a1y", "1st side vector from coordiante y component"),
                ("a1z", "1st side vector from coordinate z compoennt"),
                ("a2x", "2nd side vector from coordiante x component"),
                ("a2y", "2nd side vector from coordiante y component"),
                ("a2z", "2nd side vector from coordinate z compoennt"),
                ("a3x", "3rd side vector from coordiante x component"),
                ("a3y", "3rd side vector from coordiante y component"),
                ("a3z", "3rd side vector from coordinate z compoennt"),
            ],
        ),
        (
            "Parallelepiped",
            "rectangular parallelepiped",
            [
                ("xmin", "Minimum x of locus range"),
                ("xmax", "Maximum x of locus range"),
                ("ymin", "Minimum y of locus range"),
                ("ymax", "Maximum y of locus range"),
                ("zmin", "Minimum z of locus range"),
                ("zmax", "Maximum z of locus range"),
            ],
        ),
        (
            "Sphere",
            "sphere",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobody center z component"),
                ("r", "Sphere radius"),
            ],
        ),
        (
            "CylinderCircular",
            "right circular cylinder",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobody center z component"),
                ("hx", "Macrobody height vector x component"),
                ("hy", "Macrobody height vector y component"),
                ("hz", "Macrobody height vector z component"),
                ("r", "Right circular cylinder radius"),
            ],
        ),
        (
            "HexagonalPrism",
            "right hexagonal prism",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobody center z component"),
                ("hx", "Macrobody height vector x component"),
                ("hy", "Macrobody height vector y component"),
                ("hz", "Macrobody height vector z component"),
                ("r1", "Vector from center to facet #1"),
                ("r2", "Vector from center to facet #1"),
                ("r3", "Vector from center to facet #1"),
                ("s1", "Vector from center to facet #2"),
                ("s2", "Vector from center to facet #2"),
                ("s3", "Vector from center to facet #2"),
                ("t1", "Vector from center to facet #3"),
                ("t2", "Vector from center to facet #3"),
                ("t3", "Vector from center to facet #3"),
            ],
        ),
        (
            "CylinderElliptical",
            "right elliptical cylinder",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobody center z component"),
                ("hx", "Macrobody height vector x component"),
                ("hy", "Macrobody height vector y component"),
                ("hz", "Macrobody height vector z component"),
                ("v1x", "Macrobody vector #1 x component"),
                ("v1y", "Macrobody vector #1 y component"),
                ("v1z", "Macrobody vector #1 z component"),
            ],
        ),
        (
            "ConeTruncated",
            "truncated right-angle cone",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobody center z component"),
                ("hx", "Macrobody height vector x component"),
                ("hy", "Macrobody height vector y component"),
                ("hz", "Macrobody height vector z component"),
                ("r1", "Lower cone base radius"),
                ("r2", "Upper cone base radius"),
            ],
        ),
        (
            "Ellipsoid",
            "ellipsoid",
            [
                ("v1x", "Macrobody vector #1 x component"),
                ("v1y", "Macrobody vector #1 y component"),
                ("v1z", "Macrobody vector #1 z component"),
                ("v2x", "Macrobody vector #2 x component"),
                ("v2y", "Macrobody vector #2 y component"),
                ("v2z", "Macrobody vector #2 z component"),
                ("rm", "Minor/major radius length"),
            ],
        ),
        (
            "Wedge",
            "wedge",
            [
                ("vx", "Macrobody center x component"),
                ("vy", "Macrobody center y component"),
                ("vz", "Macrobdoy center z component"),
                ("v1x", "Macrobody vector #1 x component"),
                ("v1y", "Macrobody vector #1 y component"),
                ("v1z", "Macrobody vector #1 z component"),
                ("v2x", "Macrobody vector #2 x component"),
                ("v2y", "Macrobody vector #2 y component"),
                ("v2z", "Macrobody vector #2 z component"),
                ("v3x", "Macrobody vector #3 x component"),
                ("v3y", "Macrobody vector #3 y component"),
                ("v3z", "Macrobody vector #3 z component"),
            ],
        ),
        (
            "Polyhedron",
            "arbitrary polyhedron",
            [
                ("ax", "Coordnate #1 x component"),
                ("ay", "Coordnate #1 y component"),
                ("az", "Coordnate #1 z component"),
                ("bx", "Coordnate #2 x component"),
                ("by", "Coordnate #2 y component"),
                ("bz", "Coordnate #2 z component"),
                ("cx", "Coordnate #3 x component"),
                ("cy", "Coordnate #3 y component"),
                ("cz", "Coordnate #3 z component"),
                ("dx", "Coordnate #4 x component"),
                ("dy", "Coordnate #4 y component"),
                ("dz", "Coordnate #4 z component"),
                ("ex", "Coordnate #5 x component"),
                ("ey", "Coordnate #5 y component"),
                ("ez", "Coordnate #5 z component"),
                ("fx", "Coordnate #6 x component"),
                ("fy", "Coordnate #6 y component"),
                ("fz", "Coordnate #6 z component"),
                ("gx", "Coordnate #7 x component"),
                ("gy", "Coordnate #7 y component"),
                ("gz", "Coordnate #7 z component"),
                ("hx", "Coordnate #8 x component"),
                ("hy", "Coordnate #8 y component"),
                ("hz", "Coordnate #8 z component"),
                ("n1", "Corresponding corners specifier #1"),
                ("n2", "Corresponding corners specifier #2"),
                ("n3", "Corresponding corners specifier #3"),
                ("n4", "Corresponding corners specifier #4"),
                ("n5", "Corresponding corners specifier #5"),
                ("n6", "Corresponding corners specifier #6"),
            ],
        ),
    ]

    out = ""
    for className, classComment, parameters in DATA:
        out += f"class {className}(Surface):\n"
        out += f'\t"""\n'
        out += f"\t'{className}' represents {classComment} INP surface cards.\n"
        out += f"\n"
        out += f"\tMethods:\n"
        out += f"\t\t__init__: Initializes '{className}'.\n"
        out += f"\t\tset_parameters: Sets {classComment} parameters.\n"
        out += f'\t"""\n'
        out += f"\n"
        out += f"\n"
        out += f"\tdef __init__(self) -> Self:\n"
        out += f'\t\t"""\n'
        out += f"\t\t'__init__' initializes '{className}'.\n"
        out += f'\t\t"""\n'
        out += f"\n"

        for paramName, paramComment in parameters:
            out += f"\t\tself.{paramName}: float = None\n"

        out += f"\n"
        out += f"\t\tsuper().__init__()\n"

        out += f"\n"
        out += f"\n"
        out += f"\tdef set_parameters(self"

        for paramName, paramComment in parameters:
            out += f", {paramName}: float"

        out += f") -> None:\n"
        out += f'\t\t"""\n'
        out += f"\t\t'set_parameters' sets {classComment} parameters.\n"
        out += f"\n"
        out += f"\t\tParameters:\n"

        for paramName, paramComment in parameters:
            out += f"\t\t\t{paramName}: {paramComment}.\n"

        out += f'\t\t"""\n'

        for paramName, paramComment in parameters:
            out += f"\n"
            out += f"\t\tvalue = cast_fortran_real({paramName})\n"
            out += f"\t\tif value is None: raise ValueError\n"
            out += f"\t\tself.{paramName} = value\n"
            out += f"\t\tself.parameters['{paramName}'] = value\n"

        out += "\n"
        out += "\n"

    return out


# IMP integer
# VOL real
# PTW real
# EXT special
# FCL integer
# WWN real
# DXC real
# NONU integer
# PD real
# TMP real
# U integer
# TRCL integer
# LAT integer
# FILL integer
# ELPT real
# COSY integer
# BFLCL integer
# UNC integer
def generate_cellparameters():
    DATA = [
        (
            "Importance",
            "particle importance",
            "importance",
            "particle importance",
            "value >= 0",
            True,
            False,
        ),
        ("Volume", "volume", "volume", "volume", "value > 0", False, False),
        (
            "ProtonWeight",
            "proton weight",
            "weight",
            "collision-generated proton number/weight",
            "",
            False,
            False,
        ),
        (
            "ExponentialTransform",
            "exponential transformation",
            "stretch",
            "stretch specifier",
            "",
            True,
            False,
        ),
        (
            "ForcedCollision",
            "forced-collision",
            "control",
            "forced-collision",
            "-1 <= value <= 1",
            True,
            False,
        ),
        (
            "WeightWindowBounds",
            "space-, time-, and energy-dependent weight window bound",
            "weight",
            "weight window bounds",
            "value == -1 or value >= 0",
            True,
            True,
        ),
        (
            "DxtranContribution",
            "DXTRAN sphere contribution",
            "probability",
            "DXTRAN sphere contribution probability",
            "0 <= value <= 1",
            True,
            True,
        ),
        (
            "FissionTurnOff",
            "fission on/off",
            "setting",
            "fission on/off setting",
            "value in {0, 1, 2}",
            False,
            False,
        ),
        (
            "DetectorContribution",
            "point detector contribution",
            "probability",
            "point detector contribution probability",
            "1 <= value <= 0",
            False,
            True,
        ),
        (
            "GasThermalTemperature",
            "time-dependent thermal temperature",
            "temperature",
            "temperature",
            "value >= 0",
            False,
            True,
        ),
        (
            "Universe",
            "universe",
            "number",
            "universe number",
            "0 <= value <= 99_999_999",
            False,
            False,
        ),
        (
            "CoordinateTransformation",
            "transformation",
            "number",
            "transformation number",
            "",
            False,
            False,
        ),
        (
            "Lattice",
            "lattice shape",
            "shape",
            "shape setting",
            "value in {1, 2}",
            False,
            False,
        ),
        (
            "Fill",
            "filling universe",
            "number",
            "filling universe number",
            "0 <= number <= 99_999_999",
            True,
            False,
        ),
        (
            "EnergyCutoff",
            "lower energy cutoff",
            "cutoff",
            "energy cutoff",
            "",
            True,
            False,
        ),
        ("Cosy", "cosy map", "number", "cosy map number", "value >= 0", False, False),
        (
            "Bfield",
            "magnetic/B field",
            "number",
            "magnetic field number",
            "value >= 0",
            False,
            False,
        ),
        (
            "UncolidedSecondaries",
            "uncollided particle secondaries behavior",
            "setting",
            "uncollided secondaries setting",
            "value in {0, 1}",
            True,
            False,
        ),
    ]

    out = ""
    for (
        className,
        classComment,
        valueName,
        valueComment,
        valueCheck,
        has_designator,
        has_suffix,
    ) in DATA:
        out += f"class {className}(CellParameter):\n"
        out += f'\t"""\n'
        out += f"\t'{className}' represents INP cell card {classComment} parameters.\n"
        out += f"\n"
        out += f"\tMethods:\n"
        out += f"\t\t__init__: Initalizes '{className}'\n"
        out += f"\t\tset_value: Sets INP cell card {classComment} parameter values.\n"
        out += f'\t"""\n'
        out += f"\n"
        out += f"\n"
        out += f"\tdef __init__ ():\n"
        out += f'\t\t"""\n'
        out += f"\t\t'__init__' initalizes '{className}'\n"
        out += f'\t\t"""\n'
        out += f"\n"
        out += f"\t\tsuper().__init__()\n"
        out += f"\n"
        out += f"\t\tself.{valueName}: any = None\n"
        out += f"\t\tself.designator: Designator = None\n" if has_designator else ""
        out += f"\t\tself.suffix: int = None\n" if has_suffix else ""
        out += f"\n"
        out += f"\n"
        out += f"\tdef set_value(self, value: any) -> None:\n"
        out += f'\t\t"""\n'
        out += f"\t\t'set_value' sets INP cell card {classComment} parameter values.\n"
        out += f"\n"
        out += f"\t\tParameters:\n"
        out += f"\t\t\t{valueName} (any): Cell {valueComment}.\n"
        out += f'\t\t"""\n'
        out += f"\n"
        out += (
            f"\t\tif value is None or not ({valueCheck}):\n"
            if valueCheck
            else f"\t\tif value is None:\n"
        )
        out += f"\t\t\tself.{valueName} = value\n"

        if has_designator:
            out += f"\n"
            out += f"\n"
            out += f"\tdef set_designator(self, designator: Designator) -> None:\n"
            out += f'\t\t"""\n'
            out += f"\t\t'set_designator' sets INP cell card {classComment} parameter designator.\n"
            out += f"\t\n"
            out += f"\t\tParameters:\n"
            out += (
                f"\t\t\tdesignator (Designator): INP cell card parameter designator.\n"
            )
            out += f'\t\t"""\n'
            out += f"\t\n"
            out += f"\t\tif designator is not None:\n"
            out += f"\t\t\tself.designator = designator\n"

        if has_suffix:
            out += f"\n"
            out += f"\n"
            out += f"\tdef set_suffix(self, suffix: int) -> None:\n"
            out += f'\t\t"""\n'
            out += f"\t\t'set_suffix' sets INP cell card {classComment} parameter keyword suffix.\n"
            out += f"\t\n"
            out += f"\t\tParameters:\n"
            out += f"\t\t\tsuffix (int): INP cell card keyword suffix.\n"
            out += f'\t\t"""\n'
            out += f"\t\n"
            out += f"\t\tif suffix is not None:\n"
            out += f"\t\t\tself.suffix = suffix\n"

        out += f"\n"
        out += f"\n"

    return out


def generate_datacards():
    DATA = []

    out = ""

    return out


if __name__ == "__main__":
    FILENAME = "./out.txt"

    with open(FILENAME, "w") as file:
        file.write(generate_subsurfaces())
