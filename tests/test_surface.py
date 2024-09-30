"""
``test_surface`` tests the ``pymcnp.inp.surface`` module.
"""


import pytest
import hypothesis as hy
import hypothesis.strategies as st

import _config
import test_types
from pymcnp.files.inp.surface import Surface
from pymcnp.files.utils import errors
from pymcnp.files.utils import types


@st.composite
def surface_mnemonic(draw, valid: bool):
    """
    ``surface_mnemonic`` generates ``SurfaceMnemonic`` parameters.

    Parameters:
        valid: Validity setting.

    Returns:
        Valid/Invalid ``SurfaceMnemonic`` parameters.
    """

    MNEMONICS = {
        "p",
        "px",
        "py",
        "pz",
        "so",
        "s",
        "sx",
        "sy",
        "sz",
        "c/x",
        "c/y",
        "c/z",
        "cx",
        "cy",
        "cz",
        "k/x",
        "k/y",
        "k/z",
        "kx",
        "ky",
        "kx",
        "sq",
        "gq",
        "tx",
        "ty",
        "tz",
        "x",
        "y",
        "z",
        "box",
        "rpp",
        "sph",
        "rcc",
        "rhp",
        "rec",
        "trc",
        "ell",
        "wed",
        "arb",
    }

    if valid:
        return draw(st.samplefrom(MNEMONICS))
    else:
        return draw(st.text().filter(lambda s: s.lower() not in MNEMONICS))


def format_surface_mnemonic(mnemonic: str):
    """
    ``format_surface_mnemonic``
    """

    return mnemonic


class Test_SurfaceMnemonic:
    """
    ``Test_SurfaceMnemonic`` tests ``SurfaceMnemonic``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``CellKeyword.__init__``.
        """

        def test_valid(self):
            """
            ``test_valid`` checks valid inputs work.
            """

            assert Surface.SurfaceMnemonic("p") == Surface.SurfaceMnemonic.PLANEGENERAL
            assert Surface.SurfaceMnemonic("px") == Surface.SurfaceMnemonic.PLANENORMALX
            assert Surface.SurfaceMnemonic("py") == Surface.SurfaceMnemonic.PLANENORMALY
            assert Surface.SurfaceMnemonic("pz") == Surface.SurfaceMnemonic.PLANENORMALZ
            assert Surface.SurfaceMnemonic("so") == Surface.SurfaceMnemonic.SPHEREORIGIN
            assert Surface.SurfaceMnemonic("s") == Surface.SurfaceMnemonic.SPHEREGENERAL
            assert Surface.SurfaceMnemonic("sx") == Surface.SurfaceMnemonic.SPHERENORMALX
            assert Surface.SurfaceMnemonic("sy") == Surface.SurfaceMnemonic.SPHERENORMALY
            assert Surface.SurfaceMnemonic("sz") == Surface.SurfaceMnemonic.SPHERENORMALZ
            assert Surface.SurfaceMnemonic("c/x") == Surface.SurfaceMnemonic.CYLINDERPARALLELX
            assert Surface.SurfaceMnemonic("c/y") == Surface.SurfaceMnemonic.CYLINDERPARALLELY
            assert Surface.SurfaceMnemonic("c/z") == Surface.SurfaceMnemonic.CYLINDERPARALLELZ
            assert Surface.SurfaceMnemonic("cx") == Surface.SurfaceMnemonic.CYLINDERONX
            assert Surface.SurfaceMnemonic("cy") == Surface.SurfaceMnemonic.CYLINDERONY
            assert Surface.SurfaceMnemonic("cz") == Surface.SurfaceMnemonic.CYLINDERONZ
            assert Surface.SurfaceMnemonic("k/x") == Surface.SurfaceMnemonic.CONEPARALLELX
            assert Surface.SurfaceMnemonic("k/y") == Surface.SurfaceMnemonic.CONEPARALLELY
            assert Surface.SurfaceMnemonic("k/z") == Surface.SurfaceMnemonic.CONEPARALLELZ
            assert Surface.SurfaceMnemonic("kx") == Surface.SurfaceMnemonic.CONEONX
            assert Surface.SurfaceMnemonic("ky") == Surface.SurfaceMnemonic.CONEONY
            assert Surface.SurfaceMnemonic("kx") == Surface.SurfaceMnemonic.CONEONZ
            assert Surface.SurfaceMnemonic("sq") == Surface.SurfaceMnemonic.QUADRATICSPECIAL
            assert Surface.SurfaceMnemonic("gq") == Surface.SurfaceMnemonic.QUADRATICGENERAL
            assert Surface.SurfaceMnemonic("tx") == Surface.SurfaceMnemonic.TORUSPARALLELX
            assert Surface.SurfaceMnemonic("ty") == Surface.SurfaceMnemonic.TORUSPARALLELY
            assert Surface.SurfaceMnemonic("tz") == Surface.SurfaceMnemonic.TORUSPARALLELZ
            assert Surface.SurfaceMnemonic("x") == Surface.SurfaceMnemonic.SURFACEX
            assert Surface.SurfaceMnemonic("y") == Surface.SurfaceMnemonic.SURFACEY
            assert Surface.SurfaceMnemonic("z") == Surface.SurfaceMnemonic.SURFACEZ
            assert Surface.SurfaceMnemonic("box") == Surface.SurfaceMnemonic.BOX
            assert Surface.SurfaceMnemonic("rpp") == Surface.SurfaceMnemonic.PARALLELEPIPED
            assert Surface.SurfaceMnemonic("sph") == Surface.SurfaceMnemonic.SPHERE
            assert Surface.SurfaceMnemonic("rcc") == Surface.SurfaceMnemonic.CYLINDERCIRCULAR
            assert Surface.SurfaceMnemonic("rhp") == Surface.SurfaceMnemonic.HEXAGONALPRISM
            assert Surface.SurfaceMnemonic("rec") == Surface.SurfaceMnemonic.CYLINDERELLIPTICAL
            assert Surface.SurfaceMnemonic("trc") == Surface.SurfaceMnemonic.CONETRUNCATED
            assert Surface.SurfaceMnemonic("ell") == Surface.SurfaceMnemonic.ELLIPSOID
            assert Surface.SurfaceMnemonic("wed") == Surface.SurfaceMnemonic.WEDGE
            assert Surface.SurfaceMnemonic("arb") == Surface.SurfaceMnemonic.POLYHEDRON

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(mnemonic=surface_mnemonic(False))
        def test_invalid(self, mnemonic: str):
            """
            ``test_invalid`` checks invalid inputs raise error.
            """

            with pytest.raises(ValueError) as err:
                Surface.SurfaceMnemonic(mnemonic)

    class Test_FromMcnp:
        """
        ``Test_FromMcnp`` tests ``CellKeyword.from_mcnp``.
        """

        def test_valid(self):
            """
            ``test_valid`` checks valid inputs work.
            """

            assert Surface.SurfaceMnemonic.from_mcnp("p") == Surface.SurfaceMnemonic.PLANEGENERAL
            assert Surface.SurfaceMnemonic.from_mcnp("px") == Surface.SurfaceMnemonic.PLANENORMALX
            assert Surface.SurfaceMnemonic.from_mcnp("py") == Surface.SurfaceMnemonic.PLANENORMALY
            assert Surface.SurfaceMnemonic.from_mcnp("pz") == Surface.SurfaceMnemonic.PLANENORMALZ
            assert Surface.SurfaceMnemonic.from_mcnp("so") == Surface.SurfaceMnemonic.SPHEREORIGIN
            assert Surface.SurfaceMnemonic.from_mcnp("s") == Surface.SurfaceMnemonic.SPHEREGENERAL
            assert Surface.SurfaceMnemonic.from_mcnp("sx") == Surface.SurfaceMnemonic.SPHERENORMALX
            assert Surface.SurfaceMnemonic.from_mcnp("sy") == Surface.SurfaceMnemonic.SPHERENORMALY
            assert Surface.SurfaceMnemonic.from_mcnp("sz") == Surface.SurfaceMnemonic.SPHERENORMALZ
            assert Surface.SurfaceMnemonic.from_mcnp("c/x") == Surface.SurfaceMnemonic.CYLINDERPARALLELX
            assert Surface.SurfaceMnemonic.from_mcnp("c/y") == Surface.SurfaceMnemonic.CYLINDERPARALLELY
            assert Surface.SurfaceMnemonic.from_mcnp("c/z") == Surface.SurfaceMnemonic.CYLINDERPARALLELZ
            assert Surface.SurfaceMnemonic.from_mcnp("cx") == Surface.SurfaceMnemonic.CYLINDERONX
            assert Surface.SurfaceMnemonic.from_mcnp("cy") == Surface.SurfaceMnemonic.CYLINDERONY
            assert Surface.SurfaceMnemonic.from_mcnp("cz") == Surface.SurfaceMnemonic.CYLINDERONZ
            assert Surface.SurfaceMnemonic.from_mcnp("k/x") == Surface.SurfaceMnemonic.CONEPARALLELX
            assert Surface.SurfaceMnemonic.from_mcnp("k/y") == Surface.SurfaceMnemonic.CONEPARALLELY
            assert Surface.SurfaceMnemonic.from_mcnp("k/z") == Surface.SurfaceMnemonic.CONEPARALLELZ
            assert Surface.SurfaceMnemonic.from_mcnp("kx") == Surface.SurfaceMnemonic.CONEONX
            assert Surface.SurfaceMnemonic.from_mcnp("ky") == Surface.SurfaceMnemonic.CONEONY
            assert Surface.SurfaceMnemonic.from_mcnp("kx") == Surface.SurfaceMnemonic.CONEONZ
            assert Surface.SurfaceMnemonic.from_mcnp("sq") == Surface.SurfaceMnemonic.QUADRATICSPECIAL
            assert Surface.SurfaceMnemonic.from_mcnp("gq") == Surface.SurfaceMnemonic.QUADRATICGENERAL
            assert Surface.SurfaceMnemonic.from_mcnp("tx") == Surface.SurfaceMnemonic.TORUSPARALLELX
            assert Surface.SurfaceMnemonic.from_mcnp("ty") == Surface.SurfaceMnemonic.TORUSPARALLELY
            assert Surface.SurfaceMnemonic.from_mcnp("tz") == Surface.SurfaceMnemonic.TORUSPARALLELZ
            assert Surface.SurfaceMnemonic.from_mcnp("x") == Surface.SurfaceMnemonic.SURFACEX
            assert Surface.SurfaceMnemonic.from_mcnp("y") == Surface.SurfaceMnemonic.SURFACEY
            assert Surface.SurfaceMnemonic.from_mcnp("z") == Surface.SurfaceMnemonic.SURFACEZ
            assert Surface.SurfaceMnemonic.from_mcnp("box") == Surface.SurfaceMnemonic.BOX
            assert Surface.SurfaceMnemonic.from_mcnp("rpp") == Surface.SurfaceMnemonic.PARALLELEPIPED
            assert Surface.SurfaceMnemonic.from_mcnp("sph") == Surface.SurfaceMnemonic.SPHERE
            assert Surface.SurfaceMnemonic.from_mcnp("rcc") == Surface.SurfaceMnemonic.CYLINDERCIRCULAR
            assert Surface.SurfaceMnemonic.from_mcnp("rhp") == Surface.SurfaceMnemonic.HEXAGONALPRISM
            assert Surface.SurfaceMnemonic.from_mcnp("rec") == Surface.SurfaceMnemonic.CYLINDERELLIPTICAL
            assert Surface.SurfaceMnemonic.from_mcnp("trc") == Surface.SurfaceMnemonic.CONETRUNCATED
            assert Surface.SurfaceMnemonic.from_mcnp("ell") == Surface.SurfaceMnemonic.ELLIPSOID
            assert Surface.SurfaceMnemonic.from_mcnp("wed") == Surface.SurfaceMnemonic.WEDGE
            assert Surface.SurfaceMnemonic.from_mcnp("arb") == Surface.SurfaceMnemonic.POLYHEDRON

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(mnemonic=surface_mnemonic(False))
        def test_invalid(self, mnemonic: str):
            """
            ``test_invalid`` checks invalid inputs raise error.
            """

            source = format_surface_mnemonic(mnemonic)

            with pytest.raises(errors.MCNPSemanticError) as err:
                Surface.SurfaceMnemonic.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC


@st.composite
def surface(draw, valid_number: bool, valid_transform_periodic: bool, valid_mnemonic: bool, valid_parameters: bool):
    """
    ``surface`` generates ``Surface`` parameters.

    Parameters:
        valid_number: Number validity setting.
        valid_transform_periodic: Number validity setting.
        valid_mnemonic: Mnemonic validity setting.
        valid_parameters: Parameters Validity setting.

    Returns:
        Valid/Invalid ``Surface`` parameters.
    """

    @st.composite
    def surface_planegeneralpoint(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "p"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 9)])
        else:
            parameters = tuple([None for _ in range(0, 9)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_planegeneralequation(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "p"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 4)])
        else:
            parameters = tuple([None for _ in range(0, 4)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_planenormalx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "px"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_planenormaly(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "py"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_planenormalz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "pz"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_sphereorigin(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "so"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_spheregeneral(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "s"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 4)])
        else:
            parameters = tuple([None for _ in range(0, 4)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_spherenormalx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "sx"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 2)])
        else:
            parameters = tuple([None for _ in range(0, 2)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_spherenormaly(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "sy"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 2)])
        else:
            parameters = tuple([None for _ in range(0, 2)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_spherenormalz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "sz"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 2)])
        else:
            parameters = tuple([None for _ in range(0, 2)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderparallelx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "c/x"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 3)])
        else:
            parameters = tuple([None for _ in range(0, 3)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderparallely(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "c/y"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 3)])
        else:
            parameters = tuple([None for _ in range(0, 3)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderparallelz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "c/z"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 3)])
        else:
            parameters = tuple([None for _ in range(0, 3)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderonx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "cx"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderony(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "cy"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderonz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "cz"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 1)])
        else:
            parameters = tuple([None for _ in range(0, 1)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_coneparallelx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "k/x"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 5)])
        else:
            parameters = tuple([None for _ in range(0, 5)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_coneparallely(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "k/y"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 5)])
        else:
            parameters = tuple([None for _ in range(0, 5)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_coneparallelz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "k/z"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 5)])
        else:
            parameters = tuple([None for _ in range(0, 5)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_coneonx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "kx"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 3)])
        else:
            parameters = tuple([None for _ in range(0, 3)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_coneony(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "ky"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 3)])
        else:
            parameters = tuple([None for _ in range(0, 3)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_coneonz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "kx"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 3)])
        else:
            parameters = tuple([None for _ in range(0, 3)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_quadraticspecial(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "sq"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 10)])
        else:
            parameters = tuple([None for _ in range(0, 10)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_quadraticgeneral(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "gq"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 10)])
        else:
            parameters = tuple([None for _ in range(0, 10)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_torusparallelx(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "tx"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)])
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_torusparallely(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "ty"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)])
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_torusparallelz(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "tz"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)])
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_surfacex(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "x"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = draw(
                st.sampled_from(
                    [
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 2)] + [None, None, None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 4)] + [None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)]),
                    ]
                )
            )
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_surfacey(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "y"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = draw(
                st.sampled_from(
                    [
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 2)] + [None, None, None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 4)] + [None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)]),
                    ]
                )
            )
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_surfacez(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "z"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = draw(
                st.sampled_from(
                    [
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 2)] + [None, None, None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 4)] + [None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)]),
                    ]
                )
            )
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_box(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "box"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = draw(
                st.sampled_from(
                    [
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 9)] + [None, None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 12)]),
                    ]
                )
            )
        else:
            parameters = tuple([None for _ in range(0, 12)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_parallelepiped(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "rpp"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (*tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)]),)
        else:
            parameters = tuple([None for _ in range(0, 6)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_sphere(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "sph"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (*tuple([draw(test_types.mcnp_real()) for _ in range(0, 4)]),)
        else:
            parameters = tuple([None for _ in range(0, 4)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_sphere(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "rcc"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (*tuple([draw(test_types.mcnp_real()) for _ in range(0, 7)]),)
        else:
            parameters = tuple([None for _ in range(0, 7)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_hexagonalprism(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "rhp"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = draw(
                st.sampled_from(
                    [
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 9)] + [None, None, None, None, None, None]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 15)]),
                    ]
                )
            )
        else:
            parameters = tuple([None for _ in range(0, 15)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_cylinderelliptical(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "rec"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = draw(
                st.sampled_from(
                    [
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 10)]),
                        tuple([draw(test_types.mcnp_real()) for _ in range(0, 12)]),
                    ]
                )
            )
        else:
            parameters = tuple([None for _ in range(0, 10)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_conetruncated(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "trc"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (*tuple([draw(test_types.mcnp_real()) for _ in range(0, 8)]),)
        else:
            parameters = tuple([None for _ in range(0, 8)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_ellipsoid(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "ell"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (
                *tuple([draw(test_types.mcnp_real()) for _ in range(0, 6)] + [draw(test_types.mcnp_real(lambda i: i != 0))]),
            )
        else:
            parameters = tuple([None for _ in range(0, 7)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_wedge(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "wed"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (*tuple([draw(test_types.mcnp_real()) for _ in range(0, 12)]),)
        else:
            parameters = tuple([None for _ in range(0, 12)])

        return (number, mnemonic, transform_periodic, parameters)

    @st.composite
    def surface_polyhedron(draw, valid_number: bool, valid_transform_periodic: bool, valid_parameters: bool):
        mnemonic = "arb"

        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i != 0 and -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        if valid_parameters:
            parameters = (*tuple([draw(test_types.mcnp_real()) for _ in range(0, 30)]),)
        else:
            parameters = tuple([None for _ in range(0, 30)])

        return (number, mnemonic, transform_periodic, parameters)

    if valid_mnemonic:
        return (
            draw(surface_planegeneralpoint(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_planegeneralequation(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_planenormalx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_planenormaly(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_planenormalz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_sphereorigin(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_spheregeneral(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_spherenormalx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_spherenormaly(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_spherenormalz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderparallelx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderparallely(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderparallelz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderonx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderony(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderonz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_coneparallelx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_coneparallely(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_coneparallelz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_coneonx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_coneony(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_coneonz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_quadraticspecial(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_quadraticgeneral(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_torusparallelx(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_torusparallely(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_torusparallelz(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_surfacex(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_surfacey(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_surfacez(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_box(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_parallelepiped(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_sphere(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_sphere(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_hexagonalprism(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_cylinderelliptical(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_conetruncated(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_ellipsoid(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_wedge(valid_number, valid_transform_periodic, valid_parameters)),
            draw(surface_polyhedron(valid_number, valid_transform_periodic, valid_parameters)),
        )
    else:
        if valid_number:
            number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
        else:
            number = draw(test_types.mcnp_integer(lambda i: 1 > i or i > 99_999_999))

        if valid_transform_periodic:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 999))
        else:
            transform_periodic = draw(test_types.mcnp_integer(lambda i: i > 999))

        return ((draw(surface_mnemonic(False)), number, transform_periodic, tuple([])),)


def format_surface(number: int, mnemonic: str, transform_periodic: int, parameters: tuple):
    """
    ``format_surface``
    """

    parameters_str = " ".join([str(parameter) for parameter in parameters])
    return f"{number} {transform_periodic} {mnemonic} {parameters_str}"


class Test_Surface:
    """
    ``Test_Surface`` tests ``Surface``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``Surface.__init__``.
        """

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, True, True, True))
        def test_valid(self, surfaces: tuple):
            """
            ``test_valid`` checks valid inputs work.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                mnemonic = Surface.SurfaceMnemonic(mnemonic)

                obj = Surface(number, mnemonic, transform_periodic, parameters)

                assert obj.number == number
                assert obj.mnemonic == mnemonic
                if transform_periodic > 0:
                    assert obj.transform == transform_periodic
                    assert obj.periodic == None
                elif transform_periodic < 0:
                    assert obj.transform == None
                    assert obj.periodic == transform_periodic
                else:
                    assert obj.transform == None
                    assert obj.periodic == None
                for obj_parameter, parameter in zip(obj.parameters, parameters):
                    assert obj_parameter == pytest.approx(parameter, _config.FLOAT_MARGIN)

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(False, True, True, True))
        def test_invalid_number(self, surfaces: tuple):
            """
            ``test_invalid_number`` checks invalid numbers raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                mnemonic = Surface.SurfaceMnemonic(mnemonic)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface(number, mnemonic, transform_periodic, parameters)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, False, True, True))
        def test_invalid_transformperiodic(self, surfaces: tuple):
            """
            ``test_invalid_transformperiodic`` checks invalid transform/periodic numbers raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                mnemonic = Surface.SurfaceMnemonic(mnemonic)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface(number, mnemonic, transform_periodic, parameters)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, True, False, True))
        def test_invalid_mnemonic(self, surfaces: tuple):
            """
            ``test_invalid_mnemonic`` checks invalid mnemonic raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                mnemonic = None

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface(number, mnemonic, transform_periodic, parameters)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, True, True, False))
        def test_invalid_parameter(self, surfaces: tuple):
            """
            ``test_invalid_parameter`` checks invalid parameters raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                mnemonic = Surface.SurfaceMnemonic(mnemonic)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface(number, mnemonic, transform_periodic, parameters)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER

    class Test_FromMcnp:
        """
        ``Test_FromMcnp`` tests ``Surface.from_mcnp``.
        """

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, True, True, True))
        def test_valid(self, surfaces: tuple):
            """
            ``test_valid`` checks valid inputs work.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                source = format_surface(number, mnemonic, transform_periodic, parameters)
                obj = Surface.from_mcnp(source)

                assert obj.number == number
                assert obj.mnemonic == Surface.SurfaceMnemonic(mnemonic)
                if transform_periodic > 0:
                    assert obj.transform == transform_periodic
                    assert obj.periodic == None
                elif transform_periodic < 0:
                    assert obj.transform == None
                    assert obj.periodic == transform_periodic
                else:
                    assert obj.transform == None
                    assert obj.periodic == None
                for obj_parameter, parameter in zip(obj.parameters, parameters):
                    assert obj_parameter == pytest.approx(parameter, _config.FLOAT_MARGIN)

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(False, True, True, True))
        def test_invalid_number(self, surfaces: tuple):
            """
            ``test_invalid_number`` checks invalid numbers raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                source = format_surface(number, mnemonic, transform_periodic, parameters)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, False, True, True))
        def test_invalid_transformperiodic(self, surfaces: tuple):
            """
            ``test_invalid_transformperiodic`` checks invalid transform/periodic numbers raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                source = format_surface(number, mnemonic, transform_periodic, parameters)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, True, False, True))
        def test_invalid_mnemonic(self, surfaces: tuple):
            """
            ``test_invalid_mnemonic`` checks invalid mnemonic raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                mnemonic = "hello"
                source = format_surface(number, mnemonic, transform_periodic, parameters)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_MNEMONIC

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 49),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow),
        )
        @hy.given(surfaces=surface(True, True, True, False))
        def test_invalid_parameter(self, surfaces: tuple):
            """
            ``test_invalid_parameter`` checks invalid parameters raise error.
            """

            for surface in surfaces:
                number, mnemonic, transform_periodic, parameters = surface
                parameters = tuple([])
                source = format_surface(number, mnemonic, transform_periodic, parameters)

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Surface.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER
