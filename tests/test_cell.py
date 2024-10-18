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
            obj = pymcnp.inp.Cell.CellGeometry(formula)

            assert obj.formula == formula

    def test_invalid(self):
        for geometry in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.Cell.CellGeometry(geometry)

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
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('imp')
            == pymcnp.inp.Cell.CellOption.CellKeyword.IMPORTANCE
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('vol')
            == pymcnp.inp.Cell.CellOption.CellKeyword.VOLUME
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('pwt')
            == pymcnp.inp.Cell.CellOption.CellKeyword.PHOTON_WEIGHT
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('ext')
            == pymcnp.inp.Cell.CellOption.CellKeyword.EXPONENTIAL_TRANSFORM
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('fcl')
            == pymcnp.inp.Cell.CellOption.CellKeyword.FORCED_COLLISION
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('wwn')
            == pymcnp.inp.Cell.CellOption.CellKeyword.WEIGHT_WINDOW_BOUNDS
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('dxc')
            == pymcnp.inp.Cell.CellOption.CellKeyword.DXTRAN_CONTRIBUTION
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('nonu')
            == pymcnp.inp.Cell.CellOption.CellKeyword.FISSION_TURNOFF
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('pd')
            == pymcnp.inp.Cell.CellOption.CellKeyword.DETECTOR_CONTRIBUTION
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('tmp')
            == pymcnp.inp.Cell.CellOption.CellKeyword.GAS_THERMAL_TEMPERATURE
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('u')
            == pymcnp.inp.Cell.CellOption.CellKeyword.UNIVERSE
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('trcl')
            == pymcnp.inp.Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('*trcl')
            == pymcnp.inp.Cell.CellOption.CellKeyword.COORDINATE_TRANSFORMATION_ANGLE
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('lat')
            == pymcnp.inp.Cell.CellOption.CellKeyword.LATTICE
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('fill')
            == pymcnp.inp.Cell.CellOption.CellKeyword.FILL
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('*fill')
            == pymcnp.inp.Cell.CellOption.CellKeyword.FILL_ANGLE
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('elpt')
            == pymcnp.inp.Cell.CellOption.CellKeyword.ENERGY_CUTOFF
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('cosy')
            == pymcnp.inp.Cell.CellOption.CellKeyword.COSY
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('bflcl')
            == pymcnp.inp.Cell.CellOption.CellKeyword.BFIELD
        )
        assert (
            pymcnp.inp.Cell.CellOption.CellKeyword('unc')
            == pymcnp.inp.Cell.CellOption.CellKeyword.UNCOLLIDED_SECONDARIES
        )

    def test_invalid(self):
        for keyword in self.INVALID_EXAMPLES:
            with pytest.raises(ValueError):
                pymcnp.inp.Cell.CellOption.CellKeyword(keyword)


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
    _VALID_FILL2 = (pymcnp.utils.types.McnpInteger(0), pymcnp.utils.types.McnpInteger(0))
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
    _INVALID_FILL2 = (pymcnp.utils.types.McnpInteger(-1), pymcnp.utils.types.McnpInteger(-1))
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
            pymcnp.inp.Cell.CellOption.CellKeyword('imp'),
            pymcnp.utils.types.McnpReal(0.5),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('vol'),
            pymcnp.utils.types.McnpReal(1.12),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('pwt'),
            pymcnp.utils.types.McnpReal(1e-3),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('ext'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('fcl'),
            pymcnp.utils.types.McnpReal(-0.9),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('wwn'),
            pymcnp.utils.types.McnpReal(-1.0),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('dxc'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(0),
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('nonu'),
            pymcnp.utils.types.McnpInteger(2),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('pd'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(0),
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('tmp'),
            pymcnp.utils.types.McnpReal(1.22),
            pymcnp.utils.types.McnpInteger(0),
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('u'),
            pymcnp.utils.types.McnpInteger(0),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('trcl'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('trcl'),
            _VALID_TRCL2,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('*trcl'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('*trcl'),
            _VALID_TRCL2,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('lat'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('fill'),
            _VALID_FILL1,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('fill'),
            _VALID_FILL2,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('fill'),
            _VALID_FILL3,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('*fill'),
            _VALID_FILL1,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('*fill'),
            _VALID_FILL2,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('*fill'),
            _VALID_FILL3,
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('elpt'),
            pymcnp.utils.types.McnpReal(1.33),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('cosy'),
            pymcnp.utils.types.McnpInteger(6),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('bflcl'),
            pymcnp.utils.types.McnpInteger(4),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('unc'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            pymcnp.utils.types.Designator(('n', 'p')),
        ),
    ]

    INVALID_KEYWORD_EXAMPLES = [
        (None, _, _, _),
    ]

    INVALID_VALUE_EXAMPLES = [
        (pymcnp.inp.Cell.CellOption.CellKeyword('imp'), pymcnp.utils.types.McnpInteger(-1), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('vol'), pymcnp.utils.types.McnpReal(-1.12), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('fcl'), pymcnp.utils.types.McnpReal(-1.95), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('wwn'), pymcnp.utils.types.McnpReal(-1.03), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('dxc'), pymcnp.utils.types.McnpReal(-1.83), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('nonu'), pymcnp.utils.types.McnpInteger(32), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('pd'), pymcnp.utils.types.McnpReal(-0.83), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('tmp'), pymcnp.utils.types.McnpReal(-1.12), _, _),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('u'),
            pymcnp.utils.types.McnpInteger(-100_000_000),
            _,
            _,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('trcl'),
            pymcnp.utils.types.McnpInteger(1000),
            _,
            _,
        ),
        (pymcnp.inp.Cell.CellOption.CellKeyword('trcl'), _INVALID_TRCL2, _, _),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('*trcl'),
            pymcnp.utils.types.McnpInteger(1000),
            _,
            _,
        ),
        (pymcnp.inp.Cell.CellOption.CellKeyword('*trcl'), _INVALID_TRCL2, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('lat'), pymcnp.utils.types.McnpInteger(3), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('fill'), _INVALID_FILL1, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('fill'), _INVALID_FILL2, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('fill'), _INVALID_FILL3, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('*fill'), _INVALID_FILL1, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('*fill'), _INVALID_FILL2, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('*fill'), _INVALID_FILL3, _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('cosy'), pymcnp.utils.types.McnpInteger(70), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('bflcl'), pymcnp.utils.types.McnpInteger(-1), _, _),
        (pymcnp.inp.Cell.CellOption.CellKeyword('unc'), pymcnp.utils.types.McnpInteger(-1), _, _),
    ]

    INVALID_SUFFIX_EXAMPLES = [
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('wwn'),
            pymcnp.utils.types.McnpReal(-1.0),
            pymcnp.utils.types.McnpInteger(-1),
            _,
        ),
        (pymcnp.inp.Cell.CellOption.CellKeyword('dxc'), pymcnp.utils.types.McnpReal(0.83), None, _),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('pd'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(-1),
            _,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('tmp'),
            pymcnp.utils.types.McnpReal(1.12),
            pymcnp.utils.types.McnpInteger(-1),
            _,
        ),
    ]

    INVALID_DESGINATOR_EXAMPLES = [
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('imp'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('ext'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('fcl'),
            pymcnp.utils.types.McnpReal(-0.9),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('wwn'),
            pymcnp.utils.types.McnpReal(-1.0),
            pymcnp.utils.types.McnpInteger(1),
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('dxc'),
            pymcnp.utils.types.McnpReal(0.83),
            pymcnp.utils.types.McnpInteger(0),
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('elpt'),
            pymcnp.utils.types.McnpReal(1.33),
            None,
            None,
        ),
        (
            pymcnp.inp.Cell.CellOption.CellKeyword('unc'),
            pymcnp.utils.types.McnpInteger(1),
            None,
            None,
        ),
    ]

    def test_valid(self):
        for keyword, value, suffix, designator in self.VALID_EXAMPLES:
            obj = pymcnp.inp.Cell.CellOption(keyword, value, suffix, designator)

            assert obj.keyword == keyword
            assert obj.value == value
            if hasattr(obj, 'suffix'):
                assert obj.suffix == suffix
            if hasattr(obj, 'designator'):
                assert obj.designator == designator

    def test_invalid_keyword(self):
        for keyword, value, suffix, designator in self.INVALID_KEYWORD_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.Cell.CellOption(keyword, value, suffix, designator)

            assert (
                err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_KEYWORD
            )

    def test_invalid_value(self):
        for keyword, value, suffix, designator in self.INVALID_VALUE_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.Cell.CellOption(keyword, value, suffix, designator)

            assert err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE

    def test_invalid_suffix(self):
        for keyword, value, suffix, designator in self.INVALID_SUFFIX_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.Cell.CellOption(keyword, value, suffix, designator)

            assert (
                err.value.code == pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX
            )

    def test_invalid_designator(self):
        for keyword, value, suffix, designator in self.INVALID_DESGINATOR_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.Cell.CellOption(keyword, value, suffix, designator)

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
            pymcnp.inp.Cell.CellGeometry('+3:2'),
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
        (pymcnp.utils.types.McnpInteger(1), pymcnp.utils.types.McnpInteger(-92), _, _, _, _),
        (pymcnp.utils.types.McnpInteger(1), pymcnp.utils.types.McnpInteger(-321), _, _, _, _),
    ]

    INVALID_DENSITY_EXAMPLES = [
        (pymcnp.utils.types.McnpInteger(1), pymcnp.utils.types.McnpInteger(1), None, _, _, _),
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
            pymcnp.inp.Cell.CellGeometry('#1'),
            (),
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(3.232),
            pymcnp.inp.Cell.CellGeometry('#1'),
            (pymcnp.inp.Cell.CellOption.from_mcnp('imp:n=1')),
        ),
        (
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpInteger(1),
            pymcnp.utils.types.McnpReal(3.232),
            pymcnp.inp.Cell.CellGeometry('#1'),
            (
                pymcnp.inp.Cell.CellOption.from_mcnp('imp:n=1'),
                pymcnp.inp.Cell.CellOption.from_mcnp('vol=3.4'),
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
