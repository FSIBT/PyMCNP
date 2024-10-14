"""
``test_cell`` tests the ``pymcnp.inp.cell`` module.
"""


import pytest
import hypothesis as hy
import hypothesis.strategies as st

import _config
import test_types
from pymcnp.files.inp.cell import Cell
from pymcnp.files.utils import errors
from pymcnp.files.utils import types


@st.composite
def cell_geometry(draw, valid: bool) -> str:
    """
    ``cell_geometry`` generates ``CellGeometry`` parameters.

    Parameters:
        valid: Validity setting.

    Returns:
        Valid/Invalid ``CellGeometry`` parameters.
    """

    if valid:
        identifiers = test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999)
    else:
        identifiers = test_types.mcnp_integer(lambda i: i > 99_999_999)

    @st.composite
    def cell_geometry_helper(draw, depth: int) -> str:
        # Base Case
        if depth >= 1:
            return f"{draw(identifiers)}"

        return draw(
            st.sampled_from(
                [
                    f"{draw(identifiers)}",
                    f"+{draw(identifiers)}",
                    f"-{draw(identifiers)}",
                    f"#({draw(cell_geometry_helper(depth + 1))})",
                    f"({draw(cell_geometry_helper(depth + 1))}:{draw(cell_geometry_helper(depth + 1))})",
                    f"({draw(cell_geometry_helper(depth + 1))} {draw(cell_geometry_helper(depth + 1))})",
                ]
            )
        )

    a = draw(cell_geometry_helper(0))
    open("out.txt", "a").write(a + "\n")
    return a


def format_cell_geometry(geometry: str):
    """
    ``format_cell_geometry``
    """

    return geometry


class Test_CellGeometry:
    """
    ``Test_CellGeometry`` tests ``CellGeometry``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``CellGeometry.__init__``.
        """

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(geometry=cell_geometry(True))
        def test_valid(self, geometry: str):
            """
            ``test_valid`` checks valid inputs work.

            Parameters:
                formula: Valid ``CellGeometry`` parameters.
            """

            formula = geometry

            obj = Cell.CellGeometry(formula)

            assert obj.formula == str(formula)

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(geometry=cell_geometry(False))
        def test_invalid(self, geometry: str):
            """
            ``test_invalid`` checks semantically invalid inputs work.

            Parameters:
                formula: Invalid ``CellGeometry`` parameters.
            """

            formula = geometry

            with pytest.raises(errors.MCNPSemanticError) as err:
                Cell.CellGeometry(formula)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY

    class Test_FromMcnp:
        """
        ``Test_FromMcnp`` tests ``CellGeometry.from_mcnp``.
        """

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(geometry=cell_geometry(True))
        def test_valid(self, geometry: str):
            """
            ``test_valid`` checks valid inputs work.

            Parameters:
                formula: Valid ``CellGeometry`` parameters.
            """

            formula = geometry
            source = formula

            obj = Cell.CellGeometry.from_mcnp(source)

            assert obj.formula == source

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(geometry=cell_geometry(False))
        def test_invalid(self, geometry: str):
            """
            ``test_invalid`` checks semantically invalid inputs work.

            Parameters:
                formula: Invalid ``CellGeometry`` parameters.
            """

            formula = geometry
            source = formula

            with pytest.raises(errors.MCNPSemanticError) as err:
                Cell.CellGeometry.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY


@st.composite
def cell_keyword(draw, valid) -> str:
    """
    ``cell_keyword`` generates ``CellKeyword`` parameters.

    Parameters:
        valid: Validity setting.

    Returns:
        Valid/Invalid ``CellKeyword`` parameters.
    """

    KEYWORDS = {
        "imp",
        "vol",
        "pwt",
        "ext",
        "fcl",
        "wwn",
        "dxc",
        "nonu",
        "pd",
        "tmp",
        "u",
        "trcl",
        "*trcl",
        "lat",
        "fill",
        "*fill",
        "elpt",
        "cosy",
        "bflcl",
        "unc",
    }

    if valid:
        return draw(st.samplefrom(KEYWORDS))
    else:
        return draw(st.text().filter(lambda s: s.lower() not in KEYWORDS))


def format_cell_keyword(keyword: str):
    """
    ``format_cell_keyword``
    """

    return keyword


class Test_CellKeyword:
    """
    ``Test_CellKeyword`` tests ``CellKeyword``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``CellKeyword.__init__``.
        """

        def test_valid(self):
            """
            ``test_valid`` checks valid inputs work.
            """

            assert Cell.CellOption.CellKeyword("imp") == Cell.CellOption.CellKeyword.IMPORTANCE
            assert Cell.CellOption.CellKeyword("vol") == Cell.CellOption.CellKeyword.VOLUME
            assert Cell.CellOption.CellKeyword("pwt") == Cell.CellOption.CellKeyword.PHOTON_WEIGHT
            assert Cell.CellOption.CellKeyword("ext") == Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM
            assert Cell.CellOption.CellKeyword("fcl") == Cell.CellOption.CellKeyword.FORCED_COLLISION
            assert Cell.CellOption.CellKeyword("wwn") == Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS
            assert Cell.CellOption.CellKeyword("dxc") == Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION
            assert Cell.CellOption.CellKeyword("nonu") == Cell.CellOption.CellKeyword.FISSION_TURNOFF
            assert Cell.CellOption.CellKeyword("pd") == Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION
            assert Cell.CellOption.CellKeyword("tmp") == Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE
            assert Cell.CellOption.CellKeyword("u") == Cell.CellOption.CellKeyword.UNIVERSE
            assert Cell.CellOption.CellKeyword("trcl") == Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION
            assert Cell.CellOption.CellKeyword("*trcl") == Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE
            assert Cell.CellOption.CellKeyword("lat") == Cell.CellOption.CellKeyword.LATTICE
            assert Cell.CellOption.CellKeyword("fill") == Cell.CellOption.CellKeyword.FILL
            assert Cell.CellOption.CellKeyword("*fill") == Cell.CellOption.CellKeyword.FILL_ANGLE
            assert Cell.CellOption.CellKeyword("elpt") == Cell.CellOption.CellKeyword.ENERGY_CUTOFF
            assert Cell.CellOption.CellKeyword("cosy") == Cell.CellOption.CellKeyword.COSY
            assert Cell.CellOption.CellKeyword("bflcl") == Cell.CellOption.CellKeyword.BFIELD
            assert Cell.CellOption.CellKeyword("unc") == Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(keyword=cell_keyword(False))
        def test_invalid(self, keyword: str):
            """
            ``test_invalid`` checks invalid inputs raise error.
            """

            with pytest.raises(ValueError) as err:
                Cell.CellOption.CellKeyword(keyword)

    class Test_FromMCNP:
        """
        ``Test_FromMcnp`` tests ``CellKeyword.from_mcnp``.
        """

        def test_valid(self):
            """
            ``test_valid`` checks valid inputs work.
            """

            assert Cell.CellOption.CellKeyword.from_mcnp("imp") == Cell.CellOption.CellKeyword.IMPORTANCE
            assert Cell.CellOption.CellKeyword.from_mcnp("vol") == Cell.CellOption.CellKeyword.VOLUME
            assert Cell.CellOption.CellKeyword.from_mcnp("pwt") == Cell.CellOption.CellKeyword.PHOTON_WEIGHT
            assert Cell.CellOption.CellKeyword.from_mcnp("ext") == Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM
            assert Cell.CellOption.CellKeyword.from_mcnp("fcl") == Cell.CellOption.CellKeyword.FORCED_COLLISION
            assert Cell.CellOption.CellKeyword.from_mcnp("wwn") == Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS
            assert Cell.CellOption.CellKeyword.from_mcnp("dxc") == Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION
            assert Cell.CellOption.CellKeyword.from_mcnp("nonu") == Cell.CellOption.CellKeyword.FISSION_TURNOFF
            assert Cell.CellOption.CellKeyword.from_mcnp("pd") == Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION
            assert Cell.CellOption.CellKeyword.from_mcnp("tmp") == Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE
            assert Cell.CellOption.CellKeyword.from_mcnp("u") == Cell.CellOption.CellKeyword.UNIVERSE
            assert Cell.CellOption.CellKeyword.from_mcnp("trcl") == Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION
            assert (
                Cell.CellOption.CellKeyword.from_mcnp("*trcl") == Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE
            )
            assert Cell.CellOption.CellKeyword.from_mcnp("lat") == Cell.CellOption.CellKeyword.LATTICE
            assert Cell.CellOption.CellKeyword.from_mcnp("fill") == Cell.CellOption.CellKeyword.FILL
            assert Cell.CellOption.CellKeyword.from_mcnp("*fill") == Cell.CellOption.CellKeyword.FILL_ANGLE
            assert Cell.CellOption.CellKeyword.from_mcnp("elpt") == Cell.CellOption.CellKeyword.ENERGY_CUTOFF
            assert Cell.CellOption.CellKeyword.from_mcnp("cosy") == Cell.CellOption.CellKeyword.COSY
            assert Cell.CellOption.CellKeyword.from_mcnp("bflcl") == Cell.CellOption.CellKeyword.BFIELD
            assert Cell.CellOption.CellKeyword.from_mcnp("unc") == Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES

        @hy.settings(max_examples=_config.HY_TRIALS)
        @hy.given(keyword=cell_keyword(False))
        def test_invalid(self, keyword: str):
            """
            ``test_invalid`` checks invalid inputs raise error.
            """
            source = format_cell_keyword(keyword)

            with pytest.raises(errors.MCNPSemanticError) as err:
                Cell.CellOption.CellKeyword.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD


@st.composite
def cell_option(draw, valid_keyword: bool, valid_values: bool, valid_suffix: bool, valid_designator: bool):
    """
    ``cell_keyword`` generates ``CellOption`` parameters.

    Parameters:
        valid_keyword: Keyword validity setting.
        valid_values: Value(s) validity setting.
        valid_suffix: Suffix validity setting.
        valid_desgnator: Designator validity setting.

    Returns:
        Valid/Invalid ``CellOption`` parameters.
    """

    @st.composite
    def cell_option_importance(draw, valid_values: bool, valid_designator: bool):
        """
        ``cell_option_importance`` generates ``Importance`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``Importance`` parameters.
        """

        keyword = "imp"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: i >= 0))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i < 0))

        return (keyword, value, None, designator)

    @st.composite
    def cell_option_volume(draw, valid_values: bool):
        """
        ``cell_option_volume`` generates ``Volume`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``Volume`` parameters.
        """

        keyword = "vol"

        if valid_values:
            value = draw(test_types.mcnp_real(lambda i: i > 0))
        else:
            value = draw(test_types.mcnp_real(lambda i: i <= 0))

        return (keyword, value, None, None)

    @st.composite
    def cell_option_photonweight(draw, valid_values: bool):
        """
        ``cell_option_photonweight`` generates ``PhotonWeight`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``PhotonWeight`` parameters.
        """

        keyword = "pwt"

        if valid_values:
            value = draw(test_types.mcnp_real(lambda i: i >= 0))
        else:
            value = None

        return (keyword, value, None, None)

    @st.composite
    def cell_option_exponentialtransform(draw, valid_values: bool, valid_designator: bool):
        """
        ``cell_option_exponentialtransform`` generates ``ExponentialTransform`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``ExponentialTransform`` parameters.
        """

        keyword = "ext"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_values:
            value = draw(test_types.mcnp_real(lambda i: i >= 0))
        else:
            value = None

        return (keyword, value, None, designator)

    @st.composite
    def cell_option_forcedcollision(draw, valid_values: bool, valid_designator: bool):
        """
        ``cell_option_forcedcollision`` generates ``ForcedCollision`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``ForcedCollision`` parameters.
        """

        keyword = "fcl"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: -1 <= i <= 1))
        else:
            value = draw(test_types.mcnp_integer(lambda i: -1 > i or i > 1))

        return (keyword, value, None, designator)

    @st.composite
    def cell_option_weightwindowbounds(draw, valid_values: bool, valid_suffix: bool, valid_designator: bool):
        """
        ``cell_option_weightwindowbounds`` generates ``WeightWindowBounds`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valud_suffix: Suffix validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``WeightWindowBounds`` parameters.
        """

        keyword = "wwn"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_suffix:
            suffix = draw(test_types.mcnp_integer(lambda i: 1 <= i))
        else:
            suffix = draw(test_types.mcnp_integer(lambda i: i < 1))

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: i == -1 or i >= 0))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i < -1))

        return (keyword, value, suffix, designator)

    @st.composite
    def cell_option_dxtrancontribution(draw, valid_values: bool, valid_suffix: bool, valid_designator: bool):
        """
        ``cell_option_dxtrancontribution`` generates ``DxtranContribution`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valud_suffix: Suffix validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``DxtranContribution`` parameters.
        """

        keyword = "dxc"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_suffix:
            suffix = draw(test_types.mcnp_integer())
        else:
            suffix = None

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: 0 <= i <= 1))
        else:
            value = draw(test_types.mcnp_integer(lambda i: 0 > i or 1 < i))

        return (keyword, value, suffix, designator)

    @st.composite
    def cell_option_fissionturnoff(draw, valid_values: bool):
        """
        ``cell_option_fissionturnoff`` generates ``FissionTurnoff`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``FissionTurnoff`` parameters.
        """

        keyword = "nonu"

        if valid_values:
            value = draw(st.sampled_from([0, 1, 2]))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i not in {0, 1, 2}))

        return (keyword, value, None, None)

    @st.composite
    def cell_option_detectorcontribution(draw, valid_values: bool, valid_suffix: bool):
        """
        ``cell_option_detectorcontribution`` generates ``DetectorContribution`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valid_suffix: Suffix validity setting.

        Returns:
            Valid/Invalid ``DetectorContribution`` parameters.
        """

        keyword = "pd"

        if valid_suffix:
            suffix = draw(test_types.mcnp_integer(lambda i: 1 <= i and i <= 9999))
        else:
            suffix = draw(test_types.mcnp_integer(lambda i: i > 9999))

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: 0 <= i <= 1))
        else:
            value = draw(test_types.mcnp_integer(lambda i: 0 > i or 1 < i))

        return (keyword, value, suffix, None)

    @st.composite
    def cell_option_gasthermaltemperature(draw, valid_values: bool, valid_suffix: bool):
        """
        ``cell_option_gasthermaltemperature`` generates ``GasThermalTemperature`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valud_suffix: Suffix validity setting.

        Returns:
            Valid/Invalid ``GasThermalTemperature`` parameters.
        """

        keyword = "tmp"

        if valid_suffix:
            suffix = draw(test_types.mcnp_integer(lambda i: 1 <= i and i <= 99))
        else:
            suffix = draw(test_types.mcnp_integer(lambda i: i < 1))

        if valid_values:
            value = draw(test_types.mcnp_real(lambda i: i > 0))
        else:
            value = draw(test_types.mcnp_real(lambda i: i <= 0))

        return (keyword, value, suffix, None)

    @st.composite
    def cell_option_universe(draw, valid_values: bool):
        """
        ``cell_option_universe`` generates ``Universe`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``Universe`` parameters.
        """

        keyword = "u"

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: -99_999_999 <= i <= 99_999_999))
        else:
            value = 1_000_000_000
            # value = draw(test_types.mcnp_integer(lambda i: i < -99_999_999 or i > 99_999_999))

        return (keyword, value, None, None)

    @st.composite
    def cell_option_coordinatetransformation(draw, valid_values: bool):
        """
        ``cell_option_coordinatetransformation`` generates ``CoordinateTransformation`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``CoordinateTransformation`` parameters.
        """

        keyword = draw(st.sampled_from(["trcl", "*trcl"]))

        if valid_values:
            value = draw(
                st.sampled_from(
                    [
                        draw(test_types.mcnp_integer(lambda i: 1 <= i <= 999)),
                        tuple([draw(test_types.mcnp_integer())] * 12 + [draw(st.sampled_from([-1, 1]))]),
                    ]
                )
            )
        else:
            value = draw(
                st.sampled_from(
                    [
                        draw(test_types.mcnp_integer(lambda i: i > 999)),
                        tuple(
                            [draw(test_types.mcnp_integer())] * 12
                            + [draw(test_types.mcnp_integer(lambda i: i not in {-1, 1}))]
                        ),
                    ]
                )
            )

        return (keyword, value, None, None)

    @st.composite
    def cell_option_lattice(draw, valid_values: bool):
        """
        ``cell_option_lattice`` generates ``Lattice`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``Lattice`` parameters.
        """

        keyword = "lat"

        if valid_values:
            value = draw(st.sampled_from([1, 2]))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i not in {1, 2}))

        return (keyword, value, None, None)

    @st.composite
    def cell_option_fill(draw, valid_values: bool):
        """
        ``cell_option_fill`` generates ``Fill`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``Fill`` parameters.
        """

        keyword = draw(st.sampled_from(["fill", "*fill"]))

        if valid_values:
            value = draw(
                st.sampled_from(
                    [
                        (draw(test_types.mcnp_integer(lambda i: 0 <= i <= 99_999_999)), None),
                        (
                            draw(test_types.mcnp_integer(lambda i: 0 <= i <= 99_999_999)),
                            draw(test_types.mcnp_integer(lambda i: 1 <= i <= 999)),
                        ),
                        (
                            draw(test_types.mcnp_integer(lambda i: 0 <= i <= 99_999_999)),
                            *[draw(test_types.mcnp_integer())] * 12 + [draw(st.sampled_from([-1, 1]))],
                        ),
                    ]
                )
            )
        else:
            value = draw(
                st.sampled_from(
                    [
                        (draw(test_types.mcnp_integer(lambda i: 0 > i or i > 99_999_999)), None),
                        (
                            draw(test_types.mcnp_integer(lambda i: 0 > i or i > 99_999_999)),
                            draw(test_types.mcnp_integer(lambda i: i > 999)),
                        ),
                        (
                            draw(test_types.mcnp_integer(lambda i: 0 > i or i > 99_999_999)),
                            *[draw(test_types.mcnp_integer())] * 12
                            + [draw(test_types.mcnp_integer(lambda i: i not in {-1, 1}))],
                        ),
                    ]
                )
            )

        return (keyword, value, None, None)

    @st.composite
    def cell_option_energycutoff(draw, valid_values: bool, valid_designator: bool):
        """
        ``cell_option_energycutoff`` generates ``EnergyCutoff`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``EnergyCutoff`` parameters.
        """

        keyword = "elpt"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_values:
            value = draw(test_types.mcnp_real())
        else:
            value = None

        return (keyword, value, None, designator)

    @st.composite
    def cell_option_cosy(draw, valid_values: bool):
        """
        ``cell_option_cosy`` generates ``Cosy`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``Cosy`` parameters.
        """

        keyword = "cosy"

        if valid_values:
            value = draw(st.sampled_from([1, 2, 3, 4, 5, 6]))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i not in {1, 2, 3, 4, 5, 6}))

        return (keyword, value, None, None)

    @st.composite
    def cell_option_bfield(draw, valid_values: bool):
        """
        ``cell_option_bfield`` generates ``Bfield`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.

        Returns:
            Valid/Invalid ``Bfield`` parameters.
        """

        keyword = "bflcl"

        if valid_values:
            value = draw(test_types.mcnp_integer(lambda i: i >= 0))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i < 0))

        return (keyword, value, None, None)

    @st.composite
    def cell_option_uncollidedsecondaries(draw, valid_values: bool, valid_designator: bool):
        """
        ``cell_option_uncollidedsecondaries`` generates ``UncollidedSecondaries`` parameters.

        Parameters:
            valid_values: Value(s) validity setting.
            valid_desgnator: Designator validity setting.

        Returns:
            Valid/Invalid ``UncollidedSecondaries`` parameters.
        """

        keyword = "unc"
        designator = draw(test_types.mcnp_designator(valid_designator))

        if valid_values:
            value = draw(st.sampled_from([0, 1]))
        else:
            value = draw(test_types.mcnp_integer(lambda i: i not in {0, 1}))

        return (keyword, value, None, designator)

    if valid_keyword:
        return (
            draw(cell_option_importance(valid_values, valid_designator)),
            draw(cell_option_volume(valid_values)),
            draw(cell_option_photonweight(valid_values)),
            draw(cell_option_exponentialtransform(valid_values, valid_designator)),
            draw(cell_option_forcedcollision(valid_values, valid_designator)),
            draw(cell_option_weightwindowbounds(valid_values, valid_suffix, valid_designator)),
            draw(cell_option_dxtrancontribution(valid_values, valid_suffix, valid_designator)),
            draw(cell_option_fissionturnoff(valid_values)),
            draw(cell_option_detectorcontribution(valid_values, valid_suffix)),
            draw(cell_option_gasthermaltemperature(valid_values, valid_suffix)),
            draw(cell_option_universe(valid_values)),
            draw(cell_option_coordinatetransformation(valid_values)),
            draw(cell_option_lattice(valid_values)),
            draw(cell_option_fill(valid_values)),
            draw(cell_option_energycutoff(valid_values, valid_designator)),
            draw(cell_option_cosy(valid_values)),
            draw(cell_option_bfield(valid_values)),
            draw(cell_option_uncollidedsecondaries(valid_values, valid_designator)),
        )
    else:
        return (
            (
                draw(cell_keyword(False)),
                draw(test_types.mcnp_integer()),
                draw(test_types.mcnp_integer()),
                draw(test_types.mcnp_designator(valid_designator)),
            ),
        )


def format_cell_option(keyword: str, value: any, suffix: int, designator: tuple[str]):
    """
    ``format_cell_option``
    """

    keyword_str = format_cell_keyword(keyword)
    suffix_str = suffix if suffix is not None else ""
    designator_str = f":{", ".join(designator)}" if designator is not None else ""

    if isinstance(value, tuple):
        value_str = "".join(f" {str(val) if val is None else " "}" for val in value)
    else:
        value_str = str(value)

    return f"{keyword_str}{suffix_str}{designator_str}={value_str}"


class Test_CellOption:
    """
    ``Test_CellOption`` tests ``CellOption``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``CellOption.__init__``.
        """

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, True, True, True))
        def test_valid(self, options: tuple[tuple]):
            """
            ``test_valid`` checks valid inputs work.
            """

            for keyword, value, suffix, designator in options:
                keyword = Cell.CellOption.CellKeyword(keyword)

                if isinstance(value, int):
                    value = types.McnpInteger(value)
                elif isinstance(value, float):
                    value = types.McnpReal(value)
                elif isinstance(value, tuple):
                    if isinstance(value[0], int):
                        value = tuple([types.McnpInteger(val) if val is not None else None for val in value])
                    elif isinstance(value[0], float):
                        value = tuple([types.McnpReal(val) if val is not None else None for val in value])

                suffix = types.McnpInteger(suffix) if suffix is not None else None
                designator = types.Designator(designator) if designator is not None else None

                obj = Cell.CellOption(keyword, value, suffix=suffix, designator=designator)

                assert obj.keyword == keyword
                assert obj.value == value
                if hasattr(obj, "suffix"):
                    assert obj.suffix == suffix
                if hasattr(obj, "designator"):
                    assert obj.designator == designator

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(False, True, True, True))
        def test_invalid_keyword(self, options: tuple[tuple]):
            """
            ``test_invalid_keyword`` checks invalid keywords raise error.
            """

            for keyword, value, suffix, designator in options:
                keyword = None

                if isinstance(value, int):
                    value = types.McnpInteger(value)
                elif isinstance(value, float):
                    value = types.McnpReal(value)
                elif isinstance(value, tuple):
                    if isinstance(value[0], int):
                        value = tuple([types.McnpInteger(val) if val is not None else None for val in value])
                    elif isinstance(value[0], float):
                        value = tuple([types.McnpReal(val) if val is not None else None for val in value])

                designator = types.Designator(designator) if designator is not None else None

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Cell.CellOption(keyword, value, suffix=suffix, designator=designator)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, False, True, True))
        def test_invalid_value(self, options: tuple[tuple]):
            """
            ``test_invalid_value`` checks invalid values raise error.
            """

            for keyword, value, suffix, designator in options:
                keyword = Cell.CellOption.CellKeyword(keyword)
                value = None
                designator = types.Designator(designator) if designator is not None else None

                with pytest.raises(errors.MCNPSemanticError) as err:
                    Cell.CellOption(keyword, value, suffix=suffix, designator=designator)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, True, False, True))
        def test_invalid_suffix(self, options: tuple[tuple]):
            """
            ``test_invalid_suffix`` checks invalid suffixes raise error.
            """

            for keyword, value, suffix, designator in options:
                keyword = Cell.CellOption.CellKeyword(keyword)

                if isinstance(value, int):
                    value = types.McnpInteger(value)
                elif isinstance(value, float):
                    value = types.McnpReal(value)
                elif isinstance(value, tuple):
                    if isinstance(value[0], int):
                        value = tuple([types.McnpInteger(val) if val is not None else None for val in value])
                    elif isinstance(value[0], float):
                        value = tuple([types.McnpReal(val) if val is not None else None for val in value])

                designator = types.Designator(designator) if designator is not None else None

                if suffix is not None:
                    with pytest.raises(errors.MCNPSemanticError) as err:
                        Cell.CellOption(keyword, value, suffix=suffix, designator=designator)

                    assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, True, True, False))
        def test_invalid_designator(self, options: tuple[tuple]):
            """
            ``test_invalid_designator`` checks invalid designators raise error.
            """

            for keyword, value, suffix, designator in options:
                if designator is not None:
                    keyword = Cell.CellOption.CellKeyword(keyword)

                    if isinstance(value, int):
                        value = types.McnpInteger(value)
                    elif isinstance(value, float):
                        value = types.McnpReal(value)
                    elif isinstance(value, tuple):
                        if isinstance(value[0], int):
                            value = tuple([types.McnpInteger(val) if val is not None else None for val in value])
                        elif isinstance(value[0], float):
                            value = tuple([types.McnpReal(val) if val is not None else None for val in value])

                    designator = None

                    with pytest.raises(errors.MCNPSemanticError) as err:
                        Cell.CellOption(keyword, value, suffix=suffix, designator=designator)

                    assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR

    class Test_FromMcnp:
        """
        ``Test_FromMcnp`` tests ``CellOption.from_mcnp``.
        """

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, True, True, True))
        def test_valid(self, options: tuple[tuple]):
            """
            ``test_valid`` checks valid inputs work.
            """

            for keyword, value, suffix, designator in options:
                source = format_cell_option(keyword, value, suffix, designator)
                obj = Cell.CellOption.from_mcnp(source)

                assert obj.keyword == Cell.CellOption.CellKeyword(keyword)
                assert obj.value == value
                if hasattr(obj, "suffix"):
                    assert obj.suffix == suffix
                if hasattr(obj, "designator"):
                    assert obj.designator == types.Designator(designator)

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(False, True, True, True))
        def test_invalid_keyword(self, options: tuple[tuple]):
            """
            ``test_invalid_keyword`` checks invalid keywords raise error.
            """

            for keyword, value, suffix, designator in options:
                with pytest.raises(errors.MCNPSemanticError) as err:
                    source = format_cell_option(keyword, value, suffix, designator)
                    Cell.CellOption.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, False, True, True))
        def test_invalid_value(self, options: tuple[tuple]):
            """
            ``test_invalid_value`` checks invalid values raise error.
            """

            for keyword, value, suffix, designator in options:
                with pytest.raises(errors.MCNPSemanticError) as err:
                    if value is None:
                        assert True

                    print(keyword, value, suffix, designator)
                    source = format_cell_option(keyword, value, suffix, designator)
                    print(source)
                    Cell.CellOption.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, True, False, True))
        def test_invalid_suffix(self, options: tuple[tuple]):
            """
            ``test_invalid_suffix`` checks invalid suffixes raise error.
            """

            for keyword, value, suffix, designator in options:
                if suffix is not None:
                    with pytest.raises(errors.MCNPSemanticError) as err:
                        source = format_cell_option(keyword, value, suffix, designator)
                        Cell.CellOption.from_mcnp(source)

                    assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX

        @hy.settings(
            max_examples=max(1, _config.HY_TRIALS // 22),
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(options=cell_option(True, True, True, False))
        def test_invalid_designator(self, options: tuple[tuple]):
            """
            ``test_invalid_designator`` checks invalid designators raise error.
            """

            for keyword, value, suffix, designator in options:
                if designator is not None:
                    with pytest.raises(errors.MCNPSemanticError) as err:
                        source = format_cell_option(keyword, value, suffix, designator)
                        Cell.CellOption.from_mcnp(source)

                    assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR


@st.composite
def cell(draw, valid_number: bool, valid_material: bool, valid_density: bool, valid_geometry: bool, valid_option: bool):
    """
    ``cell_geometry`` generates ``CellGeometry`` parameters.

    Parameters:
        valid_number: Number validity setting.
        valid_material: Material validity setting.
        valid_density: Density validity setting.
        valid_geometry: Geometry validity setting.
        valid_option: Option validity setting.

    Returns:
        Valid/Invalid ``CellGeometry`` parameters.
    """

    if valid_number:
        number = draw(test_types.mcnp_integer(lambda i: 1 <= i <= 99_999_999))
    else:
        number = draw(test_types.mcnp_integer(lambda i: i < 1))

    if valid_material:
        material = draw(test_types.mcnp_integer(lambda i: 0 <= i <= 99_999_999))
    else:
        material = draw(test_types.mcnp_integer(lambda i: i < 0 or i > 99_999_999))

    if valid_density:
        density = draw(test_types.mcnp_real(lambda f: f != 0))
    else:
        density = 0

    if valid_geometry:
        geometry = draw(cell_geometry(True))
    else:
        geometry = draw(cell_geometry(False))

    if valid_option:
        option = draw(cell_option(True, True, True, True))
    else:
        option = draw(cell_option(True, False, True, True))

    return (number, material, density, geometry, option)


def format_cell(number: int, material: int, density: float, geometry: str, options: tuple[tuple]):
    """
    ``format_cell``
    """

    number_str = str(number)
    material_str = str(material)
    density_str = str(density) if material != 0 else " "
    geometry_str = format_cell_geometry(geometry)
    options_str = " ".join([format_cell_option(*option) for option in options])

    return f"{number_str} {material_str} {density_str} {geometry_str} {options_str}"


class Test_Cell:
    """
    ``Test_Cell`` tests ``Cell``.
    """

    class Test_Init:
        """
        ``Test_Init`` tests ``Cell.__init__``.
        """

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, True, True, True))
        def test_valid(self, cell: tuple):
            """
            ``test_valid`` checks valid inputs work.
            """

            number, material, density, geometry, options = cell
            geometry = Cell.CellGeometry(geometry)
            options = tuple([Cell.CellOption(*option) for option in options])

            obj = Cell(number, material, density, geometry, options)

            assert obj.number == number
            assert obj.material == material
            assert obj.density == (pytest.approx(density, _config.FLOAT_MARGIN) if material != 0 else None)
            assert obj.geometry.formula == geometry.formula
            for obj_option, option in zip(obj.options, options):
                assert obj_option.keyword == Cell.CellOption.CellKeyword(option.keyword)
                assert obj_option.value == option.value
                if hasattr(obj_option, "suffix"):
                    assert obj_option.suffix == option.suffix
                if hasattr(obj_option, "designator"):
                    assert (
                        obj_option.designator == types.Designator(option.designator) if option.designator is not None else None
                    )

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(False, True, True, True, True))
        def test_invalid_number(self, cell: tuple):
            """
            ``test_invalid_number`` checks invalid numbers raise error.
            """

            number, material, density, geometry, options = cell
            geometry = Cell.CellGeometry(geometry)
            options = tuple([Cell.CellOption(*option) for option in options])

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell(number, material, density, geometry, options)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_NUMBER

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, False, True, True, True))
        def test_invalid_material(self, cell: tuple):
            """
            ``test_invalid_material`` checks invalid material raise error.
            """

            number, material, density, geometry, options = cell
            geometry = Cell.CellGeometry(geometry)
            options = tuple([Cell.CellOption(*option) for option in options])

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell(number, material, density, geometry, options)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, False, True, True))
        def test_invalid_density(self, cell: tuple):
            """
            ``test_invalid_density`` checks invalid densities raise error.
            """

            number, material, density, geometry, options = cell
            geometry = Cell.CellGeometry(geometry)
            options = tuple([Cell.CellOption(*option) for option in options])

            if material != 0:
                with pytest.raises(errors.MCNPSemanticError) as err:
                    obj = Cell(number, material, density, geometry, options)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_DENSITY

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, True, False, True))
        def test_invalid_geometry(self, cell: tuple):
            """
            ``test_invalid_geometry`` checks invalid geometries raise error.
            """

            number, material, density, geometry, options = cell
            geometry = None
            options = tuple([Cell.CellOption(*option) for option in options])

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell(number, material, density, geometry, options)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, True, True, False))
        def test_invalid_option(self, cell: tuple):
            """
            ``test_invalid_option`` checks invalid options raise error.
            """

            number, material, density, geometry, options = cell
            geometry = Cell.CellGeometry(geometry)
            options = None

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell(number, material, density, geometry, options)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION

    class Test_FromMcnp:
        """
        ``Test_FromMcnp`` tests ``Cell.from_mcnp``.
        """

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, True, True, True))
        def test_valid(self, cell: tuple):
            """
            ``test_valid`` checks valid inputs work.
            """

            number, material, density, geometry, options = cell
            source = format_cell(number, material, density, geometry, options)

            obj = Cell.from_mcnp(source)

            assert obj.number == number
            assert obj.material == material
            assert obj.density == (pytest.approx(density, _config.FLOAT_MARGIN) if material != 0 else None)
            assert obj.geometry.formula == Cell.CellGeometry(geometry).formula
            for obj_option, option in zip(obj.options, options):
                option = Cell.CellOption(*option)

                assert obj_option.keyword == option.keyword
                assert obj_option.value == option.value
                if hasattr(obj_option, "suffix"):
                    assert obj_option.suffix == option.suffix
                if hasattr(obj_option, "designator"):
                    assert (
                        obj_option.designator == types.Designator(option.designator) if option.designator is not None else None
                    )

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(False, True, True, True, True))
        def test_invalid_number(self, cell: tuple):
            """
            ``test_invalid_number`` checks invalid numbers raise error.
            """

            number, material, density, geometry, options = cell
            source = format_cell(number, material, density, geometry, options)

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_NUMBER

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, False, True, True, True))
        def test_invalid_material(self, cell: tuple):
            """
            ``test_invalid_material`` checks invalid materials raise error.
            """

            number, material, density, geometry, options = cell
            source = format_cell(number, material, density, geometry, options)

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_MATERIAL

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, False, True, True))
        def test_invalid_density(self, cell: tuple):
            """
            ``test_invalid_density`` checks invalid densities raise error.
            """

            number, material, density, geometry, options = cell
            source = format_cell(number, material, density, geometry, options)

            if material != 0:
                with pytest.raises(errors.MCNPSemanticError) as err:
                    obj = Cell.from_mcnp(source)

                assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_DENSITY

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, True, False, True))
        def test_invalid_geometry(self, cell: tuple):
            """
            ``test_invalid_geometry`` checks invalid geometries raise error.
            """

            number, material, density, geometry, options = cell
            source = format_cell(number, material, density, geometry, options)

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY

        @hy.settings(
            max_examples=_config.HY_TRIALS,
            suppress_health_check=(hy.HealthCheck.filter_too_much, hy.HealthCheck.too_slow, hy.HealthCheck.data_too_large),
        )
        @hy.given(cell=cell(True, True, True, True, False))
        def test_invalid_option(self, cell: tuple):
            """
            ``test_invalid_option`` checks invalid options raise error.
            """

            number, material, density, geometry, options = cell
            source = format_cell(number, material, density, geometry, options)

            with pytest.raises(errors.MCNPSemanticError) as err:
                obj = Cell.from_mcnp(source)

            assert err.value.code == errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE
