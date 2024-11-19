import pymcnp
import pytest


class Test_CellGeometry:
    """
    Tests ``CellGeometry``.
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

    INVALID_EXAMPLES = []

    def test_init_valid(self):
        for formula in self.VALID_EXAMPLES:
            obj = pymcnp.inp.CellGeometry(formula)

            assert obj.formula == formula

    def test_init_invalid(self):
        for geometry in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellGeometry(geometry)

            assert (
                err.value.code
                == pymcnp.utils.pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY
            )

    def test_fromMcnp_valid(self):
        for formula in self.VALID_EXAMPLES:
            obj = pymcnp.inp.CellGeometry.from_mcnp(f'{formula}')

            assert obj.formula == formula

    def test_fromMcnp_invalid(self):
        for formula in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.pymcnp.utils.errors.MCNPSemanticError) as err:
                pymcnp.inp.CellGeometry.from_mcnp(f'{formula}')

            assert (
                err.value.code
                == pymcnp.utils.pymcnp.utils.errors.MCNPSemanticCodes.INVALID_CELL_GEOMETRY
            )


class Test_CellKeyword:
    """
    Tests ``CellKeyword``.
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

    def test_init_valid(self):
        assert pymcnp.inp.CellKeyword('imp') == pymcnp.inp.CellKeyword.IMP
        assert pymcnp.inp.CellKeyword('vol') == pymcnp.inp.CellKeyword.VOL
        assert pymcnp.inp.CellKeyword('pwt') == pymcnp.inp.CellKeyword.PWT
        assert pymcnp.inp.CellKeyword('ext') == pymcnp.inp.CellKeyword.EXT
        assert pymcnp.inp.CellKeyword('fcl') == pymcnp.inp.CellKeyword.FCL
        assert pymcnp.inp.CellKeyword('wwn') == pymcnp.inp.CellKeyword.WWN
        assert pymcnp.inp.CellKeyword('dxc') == pymcnp.inp.CellKeyword.DXC
        assert pymcnp.inp.CellKeyword('nonu') == pymcnp.inp.CellKeyword.NONU
        assert pymcnp.inp.CellKeyword('pd') == pymcnp.inp.CellKeyword.PD
        assert pymcnp.inp.CellKeyword('tmp') == pymcnp.inp.CellKeyword.TMP
        assert pymcnp.inp.CellKeyword('u') == pymcnp.inp.CellKeyword.U
        assert pymcnp.inp.CellKeyword('trcl') == pymcnp.inp.CellKeyword.TRCL
        assert pymcnp.inp.CellKeyword('lat') == pymcnp.inp.CellKeyword.LAT
        assert pymcnp.inp.CellKeyword('fill') == pymcnp.inp.CellKeyword.FILL
        assert pymcnp.inp.CellKeyword('elpt') == pymcnp.inp.CellKeyword.ELPT
        assert pymcnp.inp.CellKeyword('cosy') == pymcnp.inp.CellKeyword.COSY
        assert pymcnp.inp.CellKeyword('bflcl') == pymcnp.inp.CellKeyword.BFIELD
        assert pymcnp.inp.CellKeyword('unc') == pymcnp.inp.CellKeyword.UNC

    def test_init_invalid(self):
        for keyword in self.INVALID_EXAMPLES:
            with pytest.raises(ValueError):
                pymcnp.inp.CellKeyword(keyword)

    def test_fromMcnp_valid(self):
        assert pymcnp.inp.CellKeyword.from_mcnp('imp') == pymcnp.inp.CellKeyword.IMP
        assert pymcnp.inp.CellKeyword.from_mcnp('vol') == pymcnp.inp.CellKeyword.VOL
        assert pymcnp.inp.CellKeyword.from_mcnp('pwt') == pymcnp.inp.CellKeyword.PWT
        assert pymcnp.inp.CellKeyword.from_mcnp('ext') == pymcnp.inp.CellKeyword.EXT
        assert pymcnp.inp.CellKeyword.from_mcnp('fcl') == pymcnp.inp.CellKeyword.FCL
        assert pymcnp.inp.CellKeyword.from_mcnp('wwn') == pymcnp.inp.CellKeyword.WWN
        assert pymcnp.inp.CellKeyword.from_mcnp('dxc') == pymcnp.inp.CellKeyword.DXC
        assert pymcnp.inp.CellKeyword.from_mcnp('nonu') == pymcnp.inp.CellKeyword.NONU
        assert pymcnp.inp.CellKeyword.from_mcnp('pd') == pymcnp.inp.CellKeyword.PD
        assert pymcnp.inp.CellKeyword.from_mcnp('tmp') == pymcnp.inp.CellKeyword.TMP
        assert pymcnp.inp.CellKeyword.from_mcnp('u') == pymcnp.inp.CellKeyword.U
        assert pymcnp.inp.CellKeyword.from_mcnp('trcl') == pymcnp.inp.CellKeyword.TRCL
        assert pymcnp.inp.CellKeyword.from_mcnp('lat') == pymcnp.inp.CellKeyword.LAT
        assert pymcnp.inp.CellKeyword.from_mcnp('fill') == pymcnp.inp.CellKeyword.FILL
        assert pymcnp.inp.CellKeyword.from_mcnp('elpt') == pymcnp.inp.CellKeyword.ELPT
        assert pymcnp.inp.CellKeyword.from_mcnp('cosy') == pymcnp.inp.CellKeyword.COSY
        assert pymcnp.inp.CellKeyword.from_mcnp('bflcl') == pymcnp.inp.CellKeyword.BFIELD
        assert pymcnp.inp.CellKeyword.from_mcnp('unc') == pymcnp.inp.CellKeyword.UNC

    def test_fromMcnp_invalid(self):
        for keyword in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.MCNPSemanticError):
                pymcnp.inp.CellKeyword.from_mcnp(f'{keyword}')


class Test_CellImp:
    """
    Tests ``CellImp``.
    """

    VALID_EXAMPLES = [
        (0.5, ('n', 'p')),
        (1.5, ('n')),
        (-0.5, ('n', '#')),
    ]

    INVALID_EXAMPLES = []

    exec(pymcnp.inp.cell._CellImpFactory.build_test())


class Test_CellVol:
    """
    Tests ``CellVol``.
    """

    VALID_EXAMPLES = [
        0.5,
        1.5,
        0.0,
    ]

    INVALID_EXAMPLES = [
        -1.5,
        -2.5,
        -0.1,
    ]

    exec(pymcnp.inp.cell._CellVolFactory.build_test())


class Test_CellPwt:
    """
    Tests ``CellPwt``.
    """

    VALID_EXAMPLES = [
        0.5,
        1.5,
        -0.5,
    ]

    INVALID_EXAMPLES = []

    exec(pymcnp.inp.cell._CellPwtFactory.build_test())


class Test_CellExt:
    """
    Tests ``CellExt``.
    """

    VALID_EXAMPLES = [
        ('0.5', 'p'),
        ('0.9', '#'),
        ('-0.5', 'n'),
    ]

    INVALID_EXAMPLES = []

    exec(pymcnp.inp.cell._CellExtFactory.build_test())


class Test_CellFcl:
    """
    Tests ``CellFcl``.
    """

    VALID_EXAMPLES = [
        (0.5, 'p'),
        (0.9, '#'),
        (-0.5, 'n'),
    ]

    INVALID_EXAMPLES = [
        (2.51, 'p'),
        (3.94, '#'),
        (-1.3, 'n'),
    ]

    exec(pymcnp.inp.cell._CellFclFactory.build_test())


class Test_CellWwn:
    """
    Tests ``CellWwn``.
    """

    VALID_EXAMPLES = [
        (0.5, 3, 'p'),
        (0.9, 8, '#'),
        (-1.0, 2, 'n'),
    ]

    INVALID_EXAMPLES = []

    exec(pymcnp.inp.cell._CellWwnFactory.build_test())


class Test_CellDxc:
    """
    Tests ``CellDxc``.
    """

    VALID_EXAMPLES = [
        (0.5, 3, 'p'),
        (0.9, 8, '#'),
        (0.0, 2, 'n'),
    ]

    INVALID_EXAMPLES = [
        (1.5, 3, 'e'),
        (5.9, 8, '@'),
        (-0.5, 2, '_'),
    ]

    exec(pymcnp.inp.cell._CellDxcFactory.build_test())


# class Test_CellNonu:
#     """
#     Tests ``CellNonu``.
#     """

#     exec(pymcnp.inp.cell._CellNonuFactory.build_test())

# class Test_CellPd:
#     """
#     Tests ``CellPd``.
#     """

#     exec(pymcnp.inp.cell._CellPdFactory.build_test())

# class Test_CellTmp:
#     """
#     Tests ``CellTmp``.
#     """

#     exec(pymcnp.inp.cell._CellTmpFactory.build_test())

# class Test_CellU:
#     """
#     Tests ``CellU``.
#     """

#     exec(pymcnp.inp.cell._CellUFactory.build_test())

# class Test_CellTrcl:
#     """
#     Tests ``CellTrcl``.
#     """

#     exec(pymcnp.inp.cell._CellTrclFactory.build_test())

# class Test_CellLat:
#     """
#     Tests ``CellLat``.
#     """

#     exec(pymcnp.inp.cell._CellLatFactory.build_test())

# class Test_CellFill:
#     """
#     Tests ``CellFill``.
#     """

#     exec(pymcnp.inp.cell._CellFillFactory.build_test())

# class Test_CellElpt:
#     """
#     Tests ``CellElpt``.
#     """

#     exec(pymcnp.inp.cell._CellElptFactory.build_test())

# class Test_CellCosy:
#     """
#     Tests ``CellCosy``.
#     """

#     exec(pymcnp.inp.cell._CellCosyFactory.build_test())

# class Test_CellBflcl:
#     """
#     Tests ``CellBflcl``.
#     """

#     exec(pymcnp.inp.cell._CellBflclFactory.build_test())

# class Test_CellUnc:
#     """
#     Tests ``CellUnc``.
#     """

#     exec(pymcnp.inp.cell._CellUncFactory.build_test())
