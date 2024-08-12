"""
'strategies'
"""


from typing import *

import hypothesis as hy
import hypothesis.strategies as st


@st.composite
def mcnp_polyhedron_sides(draw, condition=lambda _: True):
    """
    'mcnp_polyhedron_sides'
    """

    return draw(st.from_regex(r"\A([1-8][1-8][1-8][1-8]|0)\Z"))


@st.composite
def fortran_integers(draw, condition=lambda _: True):
    """
    'fortran_integers'
    """

    return str(draw(st.integers().filter(condition)))


@st.composite
def fortran_reals(draw, condition=lambda _: True):
    """
    'fortran_reals'
    """

    return str(draw(st.floats(allow_nan=False, allow_infinity=False).filter(condition)))


@st.composite
def mcnp_designator(draw, condition=lambda _: True) -> str:
    """
    'mcnp_designator'
    """

    return draw(st.sampled_from(DESIGNATORS).filter(condition))


@st.composite
def mcnp_geometries(draw, identifiers, depth=None) -> str:
    """
    'mcnp_geometries'
    """

    rule = draw(st.randoms()).randint(0, 5)
    next_depth = depth + 1 if depth is not None else None

    if depth and depth >= 20:
        return f"{draw(identifiers)}"
    elif rule == 0:
        # E -> Terminal
        return f"+{draw(identifiers)}"
    elif rule == 1:
        # E -> Terminal
        return f"-{draw(identifiers)}"
    elif rule == 2:
        # E -> Terminal
        return f"{draw(identifiers)}"
    elif rule == 3:
        # E -> E '#'
        return f"#({draw(mcnp_geometries(identifiers), next_depth)})"
    elif rule == 4:
        # E -> E E ':'
        return f"({draw(mcnp_geometries(identifiers), next_depth)}:{draw(mcnp_geometries(identifiers), next_depth)})"
    elif rule == 5:
        # E -> E E ' '
        return f"({draw(mcnp_geometries(identifiers), next_depth)} {draw(mcnp_geometries(identifiers), next_depth)})"
    else:
        assert False


@st.composite
def mcnp_cells(draw, has_void_material=False):
    """
    'mcnp_cells'
    """

    if not has_void_material:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_reals(lambda f: f != 0)),
            draw(mcnp_geometries(fortran_integers(lambda i: 1 <= i <= 99_999_999))),
        )
    else:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: 0 <= i <= 99_999_999)),
            draw(fortran_reals(lambda f: f != 0)),
            draw(mcnp_geometries(fortran_integers(lambda i: 1 <= i <= 99_999_999))),
        )


@st.composite
def mcnp_surfaces(draw):
    """
    'mcnp_surfaces'
    """

    return draw(
        st.sampled_from(
            [
                draw(mcnp_surface_planeGenerals()),
                draw(mcnp_surface_planeNormalXs()),
                draw(mcnp_surface_planeNormalYs()),
                draw(mcnp_surface_planeNormalZs()),
                draw(mcnp_surface_sphereOrigins()),
                draw(mcnp_surface_sphereGenerals()),
                draw(mcnp_surface_sphereNormalXs()),
                draw(mcnp_surface_sphereNormalYs()),
                draw(mcnp_surface_sphereNormalZs()),
                draw(mcnp_surface_cylinderParallelXs()),
                draw(mcnp_surface_cylinderParallelYs()),
                draw(mcnp_surface_cylinderParallelZs()),
                draw(mcnp_surface_cylinderOnXs()),
                draw(mcnp_surface_cylinderOnYs()),
                draw(mcnp_surface_cylinderOnZs()),
                draw(mcnp_surface_coneParallelXs()),
                draw(mcnp_surface_coneParallelYs()),
                draw(mcnp_surface_coneParallelZs()),
                draw(mcnp_surface_coneOnXs()),
                draw(mcnp_surface_coneOnYs()),
                draw(mcnp_surface_coneOnZs()),
                draw(mcnp_surface_quadraticSpecials()),
                draw(mcnp_surface_quadraticGenerals()),
                draw(mcnp_surface_torusParallelXs()),
                draw(mcnp_surface_torusParallelYs()),
                draw(mcnp_surface_torusParallelZs()),
                draw(mcnp_surface_surfaceXs()),
                draw(mcnp_surface_surfaceYs()),
                draw(mcnp_surface_surfaceZs()),
                draw(mcnp_surface_boxs()),
                draw(mcnp_surface_parallelepipeds()),
                draw(mcnp_surface_spheres()),
                draw(mcnp_surface_cylinderCirculars()),
                draw(mcnp_surface_hexagonalPrisms()),
                draw(mcnp_surface_cylinderEllipticals()),
                draw(mcnp_surface_coneTruncateds()),
                draw(mcnp_surface_ellipsoids()),
                draw(mcnp_surface_wedges()),
                draw(mcnp_surface_polyhedrons()),
            ]
        )
    )


@st.composite
def mcnp_surface_planePoints(draw):
    """
    mcnp_surface_planePoints
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "p",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_planeGenerals(draw):
    """
    mcnp_surface_planeGenerals
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "p",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_planeNormalXs(draw):
    """
    mcnp_surface_planeNormalXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "px",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_planeNormalYs(draw):
    """
    mcnp_surface_planeNormalYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "py",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_planeNormalZs(draw):
    """
    mcnp_surface_planeNormalZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "pz",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_sphereOrigins(draw):
    """
    mcnp_surface_sphereOrigins
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "so",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_sphereGenerals(draw):
    """
    mcnp_surface_sphereGenerals
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "s",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_sphereNormalXs(draw):
    """
    mcnp_surface_sphereNormalXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "sx",
        [draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_sphereNormalYs(draw):
    """
    mcnp_surface_sphereNormalYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "sy",
        [draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_sphereNormalZs(draw):
    """
    mcnp_surface_sphereNormalZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "sz",
        [draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_cylinderParallelXs(draw):
    """
    mcnp_surface_cylinderParallelXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "c/x",
        [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_cylinderParallelYs(draw):
    """
    mcnp_surface_cylinderParallelYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "c/y",
        [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_cylinderParallelZs(draw):
    """
    mcnp_surface_cylinderParallelZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "c/z",
        [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_cylinderOnXs(draw):
    """
    mcnp_surface_cylinderOnXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "cx",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_cylinderOnYs(draw):
    """
    mcnp_surface_cylinderOnYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "cy",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_cylinderOnZs(draw):
    """
    mcnp_surface_cylinderOnZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "cz",
        [draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_coneParallelXs(draw):
    """
    mcnp_surface_coneParallelXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "k/x",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_coneParallelYs(draw):
    """
    mcnp_surface_coneParallelYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "k/y",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_coneParallelZs(draw):
    """
    mcnp_surface_coneParallelZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "k/z",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_coneOnXs(draw):
    """
    mcnp_surface_coneOnXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "kx",
        [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_coneOnYs(draw):
    """
    mcnp_surface_coneOnYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "ky",
        [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_coneOnZs(draw):
    """
    mcnp_surface_coneOnZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "kx",
        [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())],
    )


@st.composite
def mcnp_surface_quadraticSpecials(draw):
    """
    mcnp_surface_quadraticSpecials
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "sq",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_quadraticGenerals(draw):
    """
    mcnp_surface_quadraticGenerals
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "gq",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_torusParallelXs(draw):
    """
    mcnp_surface_torusParallelXs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "tx",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_torusParallelYs(draw):
    """
    mcnp_surface_torusParallelYs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "ty",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_torusParallelZs(draw):
    """
    mcnp_surface_torusParallelZs
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "tz",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_surfaceXs(draw):
    """
    mcnp_surface_surfaceXs
    """

    rule = draw(st.randoms()).randint(0, 2)

    if rule == 0:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
            "x",
            [draw(fortran_reals()), draw(fortran_reals())],
        )
    elif rule == 1:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
            "x",
            [
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
            ],
        )
    elif rule == 2:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
            "x",
            [
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
            ],
        )
    else:
        assert False


@st.composite
def mcnp_surface_surfaceYs(draw):
    """
    mcnp_surface_surfaceYs
    """

    rule = draw(st.randoms()).randint(0, 2)

    if rule == 0:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
            "y",
            [draw(fortran_reals()), draw(fortran_reals())],
        )
    elif rule == 1:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
            "y",
            [
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
            ],
        )
    elif rule == 2:
        return (
            draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
            draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
            "y",
            [
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
                draw(fortran_reals()),
            ],
        )
    else:
        assert False


@st.composite
def mcnp_surface_surfaceZs(draw):
    """
    mcnp_surface_surfaceZs
    """

    rule = draw(st.randoms()).randint(0, 2)

    return draw(
        st.sampled_from(
            [
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "z",
                    [draw(fortran_reals()), draw(fortran_reals())],
                ),
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "z",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "z",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
            ]
        )
    )


@st.composite
def mcnp_surface_boxs(draw):
    """
    mcnp_surface_boxs
    """

    return draw(
        st.sampled_from(
            [
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "box",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "box",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
            ]
        )
    )


@st.composite
def mcnp_surface_parallelepipeds(draw):
    """
    mcnp_surface_parallelepipeds
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "rpp",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_spheres(draw):
    """
    mcnp_surface_spheres
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "sph",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_cylinderCirculars(draw):
    """
    mcnp_surface_cylinderCirculars
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "rcc",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_hexagonalPrisms(draw):
    """
    mcnp_surface_hexagonalPrisms
    """

    return draw(
        st.sampled_from(
            [
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "rhp",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "rhp",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
            ]
        )
    )


@st.composite
def mcnp_surface_cylinderEllipticals(draw):
    """
    mcnp_surface_cylinderEllipticals
    """

    rule = draw(st.randoms()).randint(0, 2)

    return draw(
        st.sampled_from(
            [
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "rec",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
                (
                    draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
                    draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
                    "rec",
                    [
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                        draw(fortran_reals()),
                    ],
                ),
            ]
        )
    )


@st.composite
def mcnp_surface_coneTruncateds(draw):
    """
    mcnp_surface_coneTruncateds
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "trc",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_ellipsoids(draw):
    """
    mcnp_surface_ellipsoids
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "ell",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_wedges(draw):
    """
    mcnp_surface_wedges
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "wed",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ],
    )


@st.composite
def mcnp_surface_polyhedrons(draw):
    """
    mcnp_surface_polyhedrons
    """

    return (
        draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)),
        draw(fortran_integers(lambda i: -99_999_999 <= i <= 999)),
        "arb",
        [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(mcnp_polyhedron_sides()),
            draw(mcnp_polyhedron_sides()),
            draw(mcnp_polyhedron_sides()),
            draw(mcnp_polyhedron_sides()),
            draw(mcnp_polyhedron_sides()),
            draw(mcnp_polyhedron_sides()),
        ],
    )
