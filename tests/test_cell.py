import pymcnp
import pytest


_ = None


class Test_CellGeometry:
    """
    ``Test_CellGeometry`` tests ``CellGeometry``.
    """

    VALID_EXAMPLES = [
        '-15158',
        '(116 8810)',
        '#(16270052)',
        '(127 4699712)',
        '#(55912)',
        '(38406:38406)',
        '(61781 8810)',
        '(8459955:54415642)',
        '10002 4736',
        '1000 25488',
        '(43 2832)',
        '59909',
        '#(24)',
        '+1',
        '(20552 66588:10001 6572)',
        '(46413 53335)',
        '-203',
        '(60608 60608)',
        '82811712',
        '(10001 7004 112147 7320)',
        '+1000 00057',
        '(17 17)',
        '#(999 99998)',
        '-1000 11505',
        '#(1000 00100)',
        '(85:38406)',
        '-100022 492',
        '-100000 010',
    ]

    INVALID_EXAMPLES = [
        None,
    ]

    def test_valid(self):
        for formula in self.VALID_EXAMPLES:
            obj = pymcnp.inp.CellGeometry(formula)

            assert obj.formula == formula

    def test_invalid(self):
        for geometry in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellGeometry(geometry)

            assert err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY


class Test_CellKeyword:
    """
    ``Test_CellKeyword`` tests ``CellKeyword``.
    """

    INVALID_EXAMPLES = [
        'The',
        'Fusion',
        'Science',
        'and',
        'Ion',
        'Beam',
        'Technology',
        'FS',
        'IBT',
        'Program',
        'develops',
        'particle',
        'beam',
    ]

    def test_valid(self):
        assert pymcnp.inp.CellKeyword('imp') == pymcnp.inp.CellKeyword.IMPORTANCE
        assert pymcnp.inp.CellKeyword('vol') == pymcnp.inp.CellKeyword.VOLUME
        assert pymcnp.inp.CellKeyword('pwt') == pymcnp.inp.CellKeyword.PHOTON_WEIGHT
        assert pymcnp.inp.CellKeyword('ext') == pymcnp.inp.CellKeyword.EXPONENTIAL_TRANSFORM
        assert pymcnp.inp.CellKeyword('fcl') == pymcnp.inp.CellKeyword.FORCED_COLLISION
        assert pymcnp.inp.CellKeyword('wwn') == pymcnp.inp.CellKeyword.WEIGHT_WINDOW_BOUNDS
        assert pymcnp.inp.CellKeyword('dxc') == pymcnp.inp.CellKeyword.DXTRAN_CONTRIBUTION
        assert pymcnp.inp.CellKeyword('nonu') == pymcnp.inp.CellKeyword.FISSION_TURNOFF
        assert pymcnp.inp.CellKeyword('pd') == pymcnp.inp.CellKeyword.DETECTOR_CONTRIBUTION
        assert pymcnp.inp.CellKeyword('tmp') == pymcnp.inp.CellKeyword.GAS_THERMAL_TEMPERATURE
        assert pymcnp.inp.CellKeyword('u') == pymcnp.inp.CellKeyword.UNIVERSE
        assert pymcnp.inp.CellKeyword('trcl') == pymcnp.inp.CellKeyword.COORDINATE_TRANSFORMATION
        assert (
            pymcnp.inp.CellKeyword('*trcl')
            == pymcnp.inp.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE
        )
        assert pymcnp.inp.CellKeyword('lat') == pymcnp.inp.CellKeyword.LATTICE
        assert pymcnp.inp.CellKeyword('fill') == pymcnp.inp.CellKeyword.FILL
        assert pymcnp.inp.CellKeyword('*fill') == pymcnp.inp.CellKeyword.FILL_ANGLE
        assert pymcnp.inp.CellKeyword('elpt') == pymcnp.inp.CellKeyword.ENERGY_CUTOFF
        assert pymcnp.inp.CellKeyword('cosy') == pymcnp.inp.CellKeyword.COSY
        assert pymcnp.inp.CellKeyword('bflcl') == pymcnp.inp.CellKeyword.BFIELD
        assert pymcnp.inp.CellKeyword('unc') == pymcnp.inp.CellKeyword.UNCOLLIDED_SECONDARIES

    def test_invalid(self):
        for keyword in self.INVALID_EXAMPLES:
            with pytest.raises(ValueError):
                pymcnp.inp.CellKeyword(keyword)


class Test_CellOption:
    """
    ``Test_CellOption`` tests ``CellOption``.
    """

    _VALID_TRCL2 = (
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpInteger(1),
    )
    _VALID_FILL1 = (pymcnp.utils.types.McnpInteger(0), None)
    _VALID_FILL2 = (
        pymcnp.utils.types.McnpInteger(0),
        pymcnp.utils.types.McnpInteger(0),
    )
    _VALID_FILL3 = (
        pymcnp.utils.types.McnpInteger(1),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpInteger(1),
    )

    _INVALID_TRCL2 = (
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpReal(1.12),
        pymcnp.utils.types.McnpReal(5.23),
        pymcnp.utils.types.McnpReal(7.52),
        pymcnp.utils.types.McnpInteger(2),
    )
    _INVALID_FILL1 = (pymcnp.utils.types.McnpInteger(-1), None)
    _INVALID_FILL2 = (
        pymcnp.utils.types.McnpInteger(-1),
        pymcnp.utils.types.McnpInteger(-1),
    )
    _INVALID_FILL3 = (
        pymcnp.utils.types.McnpInteger(-1),
        pymcnp.utils.types.McnpReal(1.123),
        pymcnp.utils.types.McnpReal(5.233),
        pymcnp.utils.types.McnpReal(7.528),
        pymcnp.utils.types.McnpReal(1.126),
        pymcnp.utils.types.McnpReal(5.235),
        pymcnp.utils.types.McnpReal(7.524),
        pymcnp.utils.types.McnpReal(1.126),
        pymcnp.utils.types.McnpReal(5.238),
        pymcnp.utils.types.McnpReal(7.527),
        pymcnp.utils.types.McnpReal(1.124),
        pymcnp.utils.types.McnpReal(5.233),
        pymcnp.utils.types.McnpReal(7.525),
        pymcnp.utils.types.McnpInteger(23),
    )

    VALID_EXAMPLES = [
        (
            pymcnp.inp.CellKeyword('imp'),
            pymcnp.utils.types.McnpReal(0.5),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.CellKeyword('vol'),
            pymcnp.utils.types.McnpReal(1.12),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('pwt'),
            pymcnp.utils.types.McnpReal(1e-3),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('ext'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.CellKeyword('fcl'),
            pymcnp.utils.types.McnpReal(-0.9),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.CellKeyword('wwn'),
            pymcnp.utils.types.McnpReal(-1.0),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.CellKeyword('dxc'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(0),
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.CellKeyword('nonu'),
            pymcnp.utils.types.McnpInteger(2),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('pd'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(0),
            None,
        ),
        (
            pymcnp.inp.CellKeyword('tmp'),
            pymcnp.utils.types.McnpReal(1.22),
            pymcnp.utils.types.McnpInteger(0),
            None,
        ),
        (
            pymcnp.inp.CellKeyword('u'),
            pymcnp.utils.types.McnpInteger(0),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('trcl'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('trcl'),
            _VALID_TRCL2,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('*trcl'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('*trcl'),
            _VALID_TRCL2,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('lat'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('fill'),
            _VALID_FILL1,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('fill'),
            _VALID_FILL2,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('fill'),
            _VALID_FILL3,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('*fill'),
            _VALID_FILL1,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('*fill'),
            _VALID_FILL2,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('*fill'),
            _VALID_FILL3,
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('elpt'),
            pymcnp.utils.types.McnpReal(1.33),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.CellKeyword('cosy'),
            pymcnp.utils.types.McnpInteger(6),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('bflcl'),
            pymcnp.utils.types.McnpInteger(4),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('unc'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
    ]

    INVALID_KEYWORD_EXAMPLES = [
        (None, _, _, _),
    ]

    INVALID_VALUE_EXAMPLES = [
        (pymcnp.inp.CellKeyword('imp'), pymcnp.utils.types.McnpInteger(-1), _, _),
        (pymcnp.inp.CellKeyword('vol'), pymcnp.utils.types.McnpReal(-1.12), _, _),
        (pymcnp.inp.CellKeyword('fcl'), pymcnp.utils.types.McnpReal(-1.95), _, _),
        (pymcnp.inp.CellKeyword('wwn'), pymcnp.utils.types.McnpReal(-1.03), _, _),
        (pymcnp.inp.CellKeyword('dxc'), pymcnp.utils.types.McnpReal(-1.83), _, _),
        (pymcnp.inp.CellKeyword('nonu'), pymcnp.utils.types.McnpInteger(32), _, _),
        (pymcnp.inp.CellKeyword('pd'), pymcnp.utils.types.McnpReal(-0.83), _, _),
        (pymcnp.inp.CellKeyword('tmp'), pymcnp.utils.types.McnpReal(-1.12), _, _),
        (
            pymcnp.inp.CellKeyword('u'),
            pymcnp.utils.types.McnpInteger(-100_000_000),
            _,
            _,
        ),
        (
            pymcnp.inp.CellKeyword('trcl'),
            pymcnp.utils.types.McnpInteger(1000),
            _,
            _,
        ),
        (pymcnp.inp.CellKeyword('trcl'), _INVALID_TRCL2, _, _),
        (
            pymcnp.inp.CellKeyword('*trcl'),
            pymcnp.utils.types.McnpInteger(1000),
            _,
            _,
        ),
        (pymcnp.inp.CellKeyword('*trcl'), _INVALID_TRCL2, _, _),
        (pymcnp.inp.CellKeyword('lat'), pymcnp.utils.types.McnpInteger(3), _, _),
        (pymcnp.inp.CellKeyword('fill'), _INVALID_FILL1, _, _),
        (pymcnp.inp.CellKeyword('fill'), _INVALID_FILL2, _, _),
        (pymcnp.inp.CellKeyword('fill'), _INVALID_FILL3, _, _),
        (pymcnp.inp.CellKeyword('*fill'), _INVALID_FILL1, _, _),
        (pymcnp.inp.CellKeyword('*fill'), _INVALID_FILL2, _, _),
        (pymcnp.inp.CellKeyword('*fill'), _INVALID_FILL3, _, _),
        (pymcnp.inp.CellKeyword('cosy'), pymcnp.utils.types.McnpInteger(70), _, _),
        (pymcnp.inp.CellKeyword('bflcl'), pymcnp.utils.types.McnpInteger(-1), _, _),
        (pymcnp.inp.CellKeyword('unc'), pymcnp.utils.types.McnpInteger(-1), _, _),
    ]

    INVALID_SUFFIX_EXAMPLES = [
        (
            pymcnp.inp.CellKeyword('wwn'),
            pymcnp.utils.types.McnpReal(-1.0),
            pymcnp.utils.types.McnpInteger(-1),
            _,
        ),
        (pymcnp.inp.CellKeyword('dxc'), pymcnp.utils.types.McnpReal(0.83), None, _),
        (
            pymcnp.inp.CellKeyword('pd'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(-1),
            _,
        ),
        (
            pymcnp.inp.CellKeyword('tmp'),
            pymcnp.utils.types.McnpReal(1.12),
            pymcnp.utils.types.McnpInteger(-1),
            _,
        ),
    ]

    INVALID_DESGINATOR_EXAMPLES = [
        (
            pymcnp.inp.CellKeyword('imp'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('ext'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('fcl'),
            pymcnp.utils.types.McnpReal(-0.9),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('wwn'),
            pymcnp.utils.types.McnpReal(-1.0),
            pymcnp.utils.types.McnpInteger(1),
            None,
        ),
        (
            pymcnp.inp.CellKeyword('dxc'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(0),
            None,
        ),
        (
            pymcnp.inp.CellKeyword('elpt'),
            pymcnp.utils.types.McnpReal(1.33),
            None,
            None,
        ),
        (
            pymcnp.inp.CellKeyword('unc'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
    ]

    def test_valid(self):
        for value, suffix, designator in self.VALID_EXAMPLES:
            obj = pymcnp.inp.CellOption.from_mcnp(value)

            # assert obj.keyword == keyword
            assert obj.value == value
            if hasattr(obj, 'suffix'):
                assert obj.suffix == suffix
            if hasattr(obj, 'designator'):
                assert obj.designator == designator

    def test_invalid_keyword(self):
        for value, suffix, designator in self.INVALID_KEYWORD_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellOption.from_mcnp(value)

            assert (
                err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD
            )

    def test_invalid_value(self):
        for value, suffix, designator in self.INVALID_VALUE_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellOption.from_mcnp(value)

            assert err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE

    def test_invalid_suffix(self):
        for value, suffix, designator in self.INVALID_SUFFIX_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellOption.from_mcnp(value)

            assert (
                err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX
            )

    def test_invalid_designator(self):
        for value, suffix, designator in self.INVALID_DESGINATOR_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellOption.from_mcnp(value)

            assert (
                err.value.code
                == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR
            )


class Test_Cell:
    """
    ``Test_Cell`` tests ``Cell``.
    """

    VALID_EXAMPLES = [
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(4),
            pymcnp.utils.types.McnpReal(0.232),
            pymcnp.inp.CellGeometry('+3:2'),
            (),
        ),
    ]

    INVALID_NUMBER_EXAMPLES = [
        (None, _, _, _, _),
        (pymcnp.utils.types.McnpInteger(-99), _, _, _, _),
        (pymcnp.utils.types.McnpInteger(-132), _, _, _, _),
    ]

    INVALID_MATERIAL_EXAMPLES = [
        (pymcnp.utils.types.McnpInteger(1), None, _, _, _, _),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(-92),
            _,
            _,
            _,
            _,
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(-321),
            _,
            _,
            _,
            _,
        ),
    ]

    INVALID_DENSITY_EXAMPLES = [
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            None,
            _,
            _,
            _,
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(-0.232),
            _,
            _,
            _,
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(-3.232),
            _,
            _,
            _,
        ),
    ]

    INVALID_GEOMETRY_EXAMLPES = [
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(3.232),
            None,
            _,
        ),
    ]

    INVALID_OPTIONS_EXAMPLES = [
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(3.232),
            pymcnp.inp.CellGeometry('#1'),
            (),
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(3.232),
            pymcnp.inp.CellGeometry('#1'),
            (pymcnp.inp.CellOption.from_mcnp('imp:n=1')),
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(3.232),
            pymcnp.inp.CellGeometry('#1'),
            (
                pymcnp.inp.CellOption.from_mcnp('imp:n=1'),
                pymcnp.inp.CellOption.from_mcnp('vol=3.4'),
            ),
        ),
    ]

    def test_valid(self):
        pass

    def test_invalid_number(self):
        pass

    def test_invalid_material(self):
        pass

    def test_invalid_density(self):
        pass

    def test_invalid_geometry(self):
        pass

    def test_invalid_options(self):
        pass
