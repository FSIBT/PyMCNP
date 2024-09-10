"""
'_strategies'
"""


import hypothesis.strategies as st


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
def mcnp_designators(draw, condition=lambda _: True):
    """
    'mcnp_designator'
    """

    return draw(
        st.sampled_from(
            [
                "n",
                "p",
                "e",
                "|",
                "q",
                "y",
                "v",
                "f",
                "h",
                "l",
                "+",
                "-",
                "x",
                "y",
                "o",
                "!",
                "<",
                ">",
                "g",
                "/",
                "z",
                "k",
                "%",
                "^",
                "b",
                "_",
                "~",
                "c",
                "w",
                "@",
                "d",
                "t",
                "s",
                "a",
                "*",
                "?",
                "#",
            ]
        )
    )


@st.composite
def mcnp_polyhedron_sides(draw, condition=lambda _: True):
    """
    'mcnp_polyhedron_sides'
    """

    return draw(st.from_regex(r"\A([1-8][1-8][1-8][1-8]|0)\Z"))


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
def mcnp_cells(draw, valid_number, valid_material, valid_density, valid_geometry, valid_parameter):
    """
    'mcnp_cells'
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_material is None:
        material = None
    elif valid_material:
        material = draw(fortran_integers(lambda i: 0 <= i <= 99_999_999))
    else:
        material = draw(fortran_integers(lambda i: i < 0 or i > 99_999_999))

    if valid_density is None:
        density = None
    elif valid_density:
        density = draw(fortran_reals(lambda f: f != 0))
    else:
        density = "0"

    if valid_geometry is None:
        geometry = None
    elif valid_geometry:
        geometry = draw(mcnp_geometries(fortran_integers(lambda i: 1 <= i <= 99_999_999)))
    else:
        geometry = draw(mcnp_geometries(fortran_integers(lambda i: i > 99_999_999)))

    if valid_parameter is None:
        parameters = None
    elif valid_parameter:
        parameters = draw(mcnp_parameters(True))
    else:
        parameters = draw(mcnp_parameters(False))

    return (number, material, density, geometry, parameters)


@st.composite
def mcnp_parameters(draw, valid_value):
    return [
        draw(mcnp_parameter_importance(valid_value, True)),
        draw(mcnp_parameter_volume(valid_value)),
        draw(mcnp_parameter_protonWeight(valid_value)),
        draw(mcnp_parameter_exponentialTransform(valid_value, True)),
        draw(mcnp_parameter_forcedCollision(valid_value, True)),
        draw(mcnp_parameter_weightWindowBounds(valid_value, True, True)),
        draw(mcnp_parameter_dxtranContribution(valid_value, True, True)),
        draw(mcnp_parameter_fissionTurnOff(valid_value)),
        draw(mcnp_parameter_detectorContribution(valid_value, True)),
        draw(mcnp_parameter_gasThermalTemperature(valid_value, True)),
        draw(mcnp_parameter_universe(valid_value)),
        draw(mcnp_parameter_coordinateTransformation_form1(valid_value)),
        draw(mcnp_parameter_coordinateTransformation_form2(valid_value)),
        draw(mcnp_parameter_lattice(valid_value)),
        draw(mcnp_parameter_fill_form1A(valid_value)),
        draw(mcnp_parameter_fill_form1B(valid_value)),
        draw(mcnp_parameter_fill_form2(valid_value)),
        draw(mcnp_parameter_energyCutoff(valid_value, True)),
        draw(mcnp_parameter_cosy(valid_value)),
        draw(mcnp_parameter_bfield(valid_value)),
        draw(mcnp_parameter_uncolidedSecondaries(valid_value, True)),
    ]


@st.composite
def mcnp_parameter_importance(draw, valid_value: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: i >= 0)))
    else:
        value = str(draw(fortran_integers(lambda i: i < 0)))

    designator = draw(mcnp_designators(valid_designator))

    return ("imp", None, designator, value)


@st.composite
def mcnp_parameter_volume(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_reals(lambda f: f > 0)))
    else:
        value = str(draw(fortran_reals(lambda f: f <= 0)))

    return ("vol", None, None, value)


@st.composite
def mcnp_parameter_protonWeight(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_reals()))
    else:
        value = "a"

    return ("pwt", None, None, value)


@st.composite
def mcnp_parameter_exponentialTransform(draw, valid_value: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers()))
    else:
        value = "a"

    designator = draw(mcnp_designators(valid_designator))

    return ("ext", None, designator, value)


@st.composite
def mcnp_parameter_forcedCollision(draw, valid_value: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: -1 <= i <= 1)))
    else:
        value = str(draw(fortran_integers(lambda i: -1 > i or i > 1)))

    designator = draw(mcnp_designators(valid_designator))

    return ("fcl", None, designator, value)


@st.composite
def mcnp_parameter_weightWindowBounds(draw, valid_value: bool, valid_suffix: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: i == -1 or i >= 0)))
    else:
        value = str(draw(fortran_integers(lambda i: i != -1 and i < 0)))

    if valid_suffix is None:
        suffix = None
    elif valid_suffix:
        suffix = str(draw(fortran_integers(lambda i: 1 <= i and i <= 99_999_999)))
    else:
        suffix = str(draw(fortran_integers(lambda i: 1 > i or i > 99_999_999)))

    designator = draw(mcnp_designators(valid_designator))

    return ("wwn", suffix, designator, value)


@st.composite
def mcnp_parameter_dxtranContribution(draw, valid_value: bool, valid_suffix: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: 0 <= i <= 1)))
    else:
        value = str(draw(fortran_integers(lambda i: 0 > i or 1 < i)))

    if valid_suffix is None:
        suffix = None
    elif valid_suffix:
        suffix = str(draw(fortran_integers(lambda i: 1 <= i and i <= 99_999_999)))
    else:
        suffix = str(draw(fortran_integers(lambda i: 1 > i or i > 99_999_999)))

    designator = draw(mcnp_designators(valid_designator))

    return ("dxc", suffix, designator, value)


@st.composite
def mcnp_parameter_fissionTurnOff(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(st.sampled_from([0, 1, 2])))
    else:
        value = str(draw(fortran_integers(lambda i: i not in {0, 1, 2})))

    return ("nonu", None, None, value)


@st.composite
def mcnp_parameter_detectorContribution(draw, valid_value: bool, valid_suffix: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: 0 <= i <= 1)))
    else:
        value = str(draw(fortran_integers(lambda i: 0 > i or 1 < i)))

    if valid_suffix is None:
        suffix = None
    elif valid_suffix:
        suffix = str(draw(fortran_integers(lambda i: 1 <= i and i <= 99_999_999)))
    else:
        suffix = str(draw(fortran_integers(lambda i: 1 > i or i > 99_999_999)))

    return ("pd", suffix, None, value)


@st.composite
def mcnp_parameter_gasThermalTemperature(draw, valid_value: bool, valid_suffix: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_reals(lambda i: i >= 0)))
    else:
        value = str(draw(fortran_reals(lambda i: i < 0)))

    if valid_suffix is None:
        suffix = None
    elif valid_suffix:
        suffix = str(draw(fortran_integers(lambda i: 1 <= i and i <= 99_999_999)))
    else:
        suffix = str(draw(fortran_integers(lambda i: 1 > i or i > 99_999_999)))

    return ("tmp", suffix, None, value)


@st.composite
def mcnp_parameter_universe(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: 1 <= i <= 99_999_999)))
    else:
        value = str(draw(fortran_integers(lambda i: 1 > i or i > 99_999_999)))

    return ("u", None, None, value)


@st.composite
def mcnp_parameter_coordinateTransformation_form1(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers()))
    else:
        value = "a"

    return ("trcl", None, None, value)


@st.composite
def mcnp_parameter_coordinateTransformation_form2(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = " ".join([draw(fortran_integers())] * 12 + [str(draw(st.sampled_from([-1, 1])))])
    else:
        value = "a"

    return ("trcl", None, None, value)


@st.composite
def mcnp_parameter_lattice(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(st.sampled_from([1, 2])))
    else:
        value = str(draw(fortran_integers(lambda i: i not in {1, 2})))

    return ("lat", None, None, value)


@st.composite
def mcnp_parameter_fill_form1A(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: 0 <= i <= 99_999_999)))
    else:
        value = str(draw(fortran_integers(lambda i: 0 > i or i > 99_999_999)))

    return ("fill", None, None, value)


@st.composite
def mcnp_parameter_fill_form1B(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = (
            str(draw(fortran_integers(lambda i: 0 <= i <= 99_999_999)))
            + " "
            + str(draw(fortran_integers(lambda i: 1 <= i <= 999)))
        )
    else:
        value = (
            str(draw(fortran_integers(lambda i: 0 > i or i > 99_999_999)))
            + " "
            + str(draw(fortran_integers(lambda i: i > 999)))
        )

    return ("fill", None, None, value)


@st.composite
def mcnp_parameter_fill_form2(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        i_lower = int(draw(fortran_integers(lambda i: 1 <= i < 3)))
        j_lower = int(draw(fortran_integers(lambda i: 1 <= i < 3)))
        k_lower = int(draw(fortran_integers(lambda i: 1 <= i < 3)))
        i_upper = int(draw(fortran_integers(lambda i: 3 <= i < 5)))
        j_upper = int(draw(fortran_integers(lambda i: 3 <= i < 5)))
        k_upper = int(draw(fortran_integers(lambda i: 3 <= i < 5)))
        count = (i_upper - i_lower) * (j_upper - j_lower) * (k_upper - k_lower)
        value = (
            f"{i_lower}:{i_upper} {j_lower}:{j_upper} {k_lower}:{k_upper} "
            + f"{draw(fortran_integers(lambda i: 0 <= i <= 99_999_999))} " * count
        )
    else:
        value = "2:1 4:3 5:2 14 6 2 58 0 1"

    return ("fill", None, None, value)


@st.composite
def mcnp_parameter_energyCutoff(draw, valid_value: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_reals()))
    else:
        value = "a"

    designator = draw(mcnp_designators(valid_designator))

    return ("elpt", None, designator, value)


@st.composite
def mcnp_parameter_cosy(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: i >= 0)))
    else:
        value = str(draw(fortran_integers(lambda i: i < 0)))

    return ("cosy", None, None, value)


@st.composite
def mcnp_parameter_bfield(draw, valid_value: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(fortran_integers(lambda i: i >= 0)))
    else:
        value = str(draw(fortran_integers(lambda i: i < 0)))

    return ("bflcl", None, None, value)


@st.composite
def mcnp_parameter_uncolidedSecondaries(draw, valid_value: bool, valid_designator: bool):
    if valid_value is None:
        value = None
    elif valid_value:
        value = str(draw(st.sampled_from([0, 1])))
    else:
        value = str(draw(fortran_integers(lambda i: i not in {0, 1})))

    designator = draw(mcnp_designators(valid_designator))

    return ("unc", None, designator, value)


@st.composite
def mcnp_surfaces(draw, valid_number, valid_transform, valid_mnemonic):
    return [
        draw(mcnp_surface_planeGenerals(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_planeNormalXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_planeNormalYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_planeNormalZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_sphereOrigins(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_sphereGenerals(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_sphereNormalXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_sphereNormalYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_sphereNormalZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderParallelXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderParallelYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderParallelZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderOnXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderOnYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderOnZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneParallelXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneParallelYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneParallelZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneOnXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneOnYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneOnZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_quadraticSpecials(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_quadraticGenerals(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_torusParallelXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_torusParallelYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_torusParallelZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_surfaceXs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_surfaceYs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_surfaceZs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_boxs(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_parallelepipeds(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_spheres(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderCirculars(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_hexagonalPrisms(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_cylinderEllipticals(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_coneTruncateds(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_ellipsoids(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_wedges(valid_number, valid_transform, valid_mnemonic)),
        draw(mcnp_surface_polyhedrons(valid_number, valid_transform, valid_mnemonic)),
    ]


@st.composite
def mcnp_surface_planeGenerals(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_planeGenerals
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 1)

    if rule == 0:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 1:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    else:
        assert False

    return (number, transform, "p" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_planeNormalXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_planeNormalXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "px" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_planeNormalYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_planeNormalYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "py" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_planeNormalZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_planeNormalZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "pz" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_sphereOrigins(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_sphereOrigins
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "so" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_sphereGenerals(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_sphereGenerals
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "s" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_sphereNormalXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_sphereNormalXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals()), draw(fortran_reals())]

    return (number, transform, "sx" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_sphereNormalYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_sphereNormalYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals()), draw(fortran_reals())]

    return (number, transform, "sy" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_sphereNormalZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_sphereNormalZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals()), draw(fortran_reals())]

    return (number, transform, "sz" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderParallelXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderParallelXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())]

    return (number, transform, "c/x" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderParallelYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderParallelYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())]

    return (number, transform, "c/y" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderParallelZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderParallelZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals()), draw(fortran_reals()), draw(fortran_reals())]

    return (number, transform, "c/z" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderOnXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderOnXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "cx" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderOnYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderOnYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "cy" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderOnZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderOnZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [draw(fortran_reals())]

    return (number, transform, "cz" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneParallelXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneParallelXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "k/x" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneParallelYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneParallelYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "k/y" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneParallelZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneParallelZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "k/z" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneOnXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneOnXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "kx" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneOnYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneOnYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "ky" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneOnZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneOnZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "kx" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_quadraticSpecials(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_quadraticSpecials
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
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
    ]

    return (number, transform, "sq" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_quadraticGenerals(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_quadraticGenerals
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
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
    ]

    return (number, transform, "gq" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_torusParallelXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_torusParallelXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "tx" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_torusParallelYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_torusParallelYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "ty" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_torusParallelZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_torusParallelZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "tz" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_surfaceXs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_surfaceXs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 2)

    if rule == 0:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 1:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 2:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    else:
        assert False

    return (number, transform, "x" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_surfaceYs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_surfaceYs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 2)

    if rule == 0:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 1:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 2:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    else:
        assert False

    return (number, transform, "y" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_surfaceZs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_surfaceZs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 2)

    if rule == 0:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 1:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 2:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    else:
        assert False

    return (number, transform, "z" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_boxs(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_boxs
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 1)

    if rule == 0:
        entries = [
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
            draw(fortran_reals()),
        ]
    elif rule == 1:
        entries = [
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
        ]
    else:
        assert False

    return (number, transform, "box" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_parallelepipeds(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_parallelepipeds
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "rpp" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_spheres(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_spheres
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "sph" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderCirculars(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderCirculars
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "rcc" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_hexagonalPrisms(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_hexagonalPrisms
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 1)

    if rule == 0:
        entries = [
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
        ]
    elif rule == 1:
        entries = [
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
        ]
    else:
        assert False

    return (number, transform, "rec" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_cylinderEllipticals(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_cylinderEllipticals
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    rule = draw(st.randoms()).randint(0, 1)

    if rule == 0:
        entries = [
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
        ]
    elif rule == 1:
        entries = [
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
        ]
    else:
        assert False

    return (number, transform, "rec" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_coneTruncateds(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_coneTruncateds
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "trc" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_ellipsoids(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_ellipsoids
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
        draw(fortran_reals()),
    ]

    return (number, transform, "ell" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_wedges(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_wedges
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
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
    ]

    return (number, transform, "wed" if valid_mnemonic else "hi", entries)


@st.composite
def mcnp_surface_polyhedrons(draw, valid_number, valid_transform, valid_mnemonic):
    """
    mcnp_surface_polyhedrons
    """

    if valid_number is None:
        number = None
    elif valid_number:
        number = draw(fortran_integers(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(fortran_integers(lambda i: i < 1 or i > 99_999_999))

    if valid_transform is None:
        transform = None
    elif valid_transform:
        transform = draw(fortran_integers(lambda i: -99_999_999 <= i <= 999))
    else:
        transform = draw(fortran_integers(lambda i: i > 999))

    entries = [
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
    ]

    return (number, transform, "arb" if valid_mnemonic else "hi", entries)
