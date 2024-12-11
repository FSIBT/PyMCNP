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

    def test_valid(self):
        for formula in self.VALID_EXAMPLES:
            obj = pymcnp.inp.CellGeometry.from_mcnp(f'{formula}')

            assert obj.formula == formula

    def test_invalid(self):
        for formula in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.pymcnp.utils.errors.McnpError) as err:
                pymcnp.inp.CellGeometry.from_mcnp(f'{formula}')

            assert err.value.code == pymcnp.utils.errors.McnpCode.INVALID_CELL_GEOMETRY


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

    def test_valid(self):
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
        assert pymcnp.inp.CellKeyword.from_mcnp('bflcl') == pymcnp.inp.CellKeyword.BFLCL
        assert pymcnp.inp.CellKeyword.from_mcnp('unc') == pymcnp.inp.CellKeyword.UNC

    def test_invalid(self):
        for keyword in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError) as err:
                pymcnp.inp.CellKeyword.from_mcnp(f'{keyword}')

            assert err.value.code == pymcnp.utils.errors.McnpCode.UNRECOGNIZED_KEYWORD


class Test_CellImp:
    """
    Tests ``CellImp``.
    """

    VALID_EXAMPLES = [(0.5, ('n', 'p')), (1.5, 'n'), (-0.5, ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for importance, designator in self.VALID_EXAMPLES:
            _importance = pymcnp.utils.types.McnpReal(importance)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellImp(_importance, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.IMP
            assert obj.importance == pymcnp.utils.types.McnpReal(importance)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for importance, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                importance = pymcnp.utils.types.McnpReal(importance)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellImp(importance, designator)


class Test_CellVol:
    """
    Tests ``CellVol``.
    """

    VALID_EXAMPLES = [0.5, 1.5, 0.0]

    INVALID_EXAMPLES = [-1.5, -2.5, -0.1]

    def test_valid(self):
        for volume in self.VALID_EXAMPLES:
            _volume = pymcnp.utils.types.McnpReal(volume)

            obj = pymcnp.inp.CellVol(_volume)

            assert obj.keyword == pymcnp.inp.CellKeyword.VOL
            assert obj.volume == pymcnp.utils.types.McnpReal(volume)

    def test_invalid(self):
        for volume in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                volume = pymcnp.utils.types.McnpReal(volume)
                pymcnp.inp.CellVol(volume)


class Test_CellPwt:
    """
    Tests ``CellPwt``.
    """

    VALID_EXAMPLES = [0.5, 1.5, -0.5]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for weight in self.VALID_EXAMPLES:
            _weight = pymcnp.utils.types.McnpReal(weight)

            obj = pymcnp.inp.CellPwt(_weight)

            assert obj.keyword == pymcnp.inp.CellKeyword.PWT
            assert obj.weight == pymcnp.utils.types.McnpReal(weight)

    def test_invalid(self):
        for weight in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                weight = pymcnp.utils.types.McnpReal(weight)
                pymcnp.inp.CellPwt(weight)


class Test_CellExt:
    """
    Tests ``CellExt``.
    """

    VALID_EXAMPLES = [('0.5', ('n', 'p')), ('0.9', 'n'), ('-0.5', ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for stretch, designator in self.VALID_EXAMPLES:
            _stretch = stretch
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellExt(_stretch, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.EXT
            assert obj.stretch == stretch
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for stretch, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                stretch = stretch
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellExt(stretch, designator)


class Test_CellFcl:
    """
    Tests ``CellFcl``.
    """

    VALID_EXAMPLES = [(0.5, ('n', 'p')), (0.9, 'n'), (-0.5, ('n', '#'))]

    INVALID_EXAMPLES = [(2.51, ('n', 'p')), (3.94, 'n'), (-1.3, ('n', '#'))]

    def test_valid(self):
        for control, designator in self.VALID_EXAMPLES:
            _control = pymcnp.utils.types.McnpReal(control)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellFcl(_control, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.FCL
            assert obj.control == pymcnp.utils.types.McnpReal(control)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for control, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                control = pymcnp.utils.types.McnpReal(control)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellFcl(control, designator)


class Test_CellWwn:
    """
    Tests ``CellWwn``.
    """

    VALID_EXAMPLES = [(0.5, 3, ('n', 'p')), (0.9, 8, 'n'), (-1.0, 2, ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for bound, suffix, designator in self.VALID_EXAMPLES:
            _bound = pymcnp.utils.types.McnpReal(bound)
            _suffix = pymcnp.utils.types.McnpInteger(suffix)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellWwn(_bound, _suffix, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.WWN
            assert obj.bound == pymcnp.utils.types.McnpReal(bound)
            assert obj.suffix == pymcnp.utils.types.McnpInteger(suffix)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for bound, suffix, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                bound = pymcnp.utils.types.McnpReal(bound)
                suffix = pymcnp.utils.types.McnpInteger(suffix)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellWwn(bound, suffix, designator)


class Test_CellDxc:
    """
    Tests ``CellDxc``.
    """

    VALID_EXAMPLES = [(0.5, 3, ('n', 'p')), (0.9, 8, 'n'), (0.0, 2, ('n', '#'))]

    INVALID_EXAMPLES = [(-1.0, 2, 'n')]

    def test_valid(self):
        for probability, suffix, designator in self.VALID_EXAMPLES:
            _probability = pymcnp.utils.types.McnpReal(probability)
            _suffix = pymcnp.utils.types.McnpInteger(suffix)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellDxc(_probability, _suffix, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.DXC
            assert obj.probability == pymcnp.utils.types.McnpReal(probability)
            assert obj.suffix == pymcnp.utils.types.McnpInteger(suffix)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for probability, suffix, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                probability = pymcnp.utils.types.McnpReal(probability)
                suffix = pymcnp.utils.types.McnpInteger(suffix)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellDxc(probability, suffix, designator)


class Test_CellNonu:
    """
    Tests ``CellNonu``.
    """

    VALID_EXAMPLES = [0, 1, 2]

    INVALID_EXAMPLES = [-1, 3, 100]

    def test_valid(self):
        for setting in self.VALID_EXAMPLES:
            _setting = pymcnp.utils.types.McnpInteger(setting)

            obj = pymcnp.inp.CellNonu(_setting)

            assert obj.keyword == pymcnp.inp.CellKeyword.NONU
            assert obj.setting == pymcnp.utils.types.McnpInteger(setting)

    def test_invalid(self):
        for setting in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                setting = pymcnp.utils.types.McnpInteger(setting)
                pymcnp.inp.CellNonu(setting)


class Test_CellPd:
    """
    Tests ``CellPd``.
    """

    VALID_EXAMPLES = [(0, 5), (0.5, 7), (1, 3)]

    INVALID_EXAMPLES = [(-1, 1), (3, 2), (100, 5)]

    def test_valid(self):
        for probability, suffix in self.VALID_EXAMPLES:
            _probability = pymcnp.utils.types.McnpReal(probability)
            _suffix = pymcnp.utils.types.McnpInteger(suffix)

            obj = pymcnp.inp.CellPd(_probability, _suffix)

            assert obj.keyword == pymcnp.inp.CellKeyword.PD
            assert obj.probability == pymcnp.utils.types.McnpReal(probability)
            assert obj.suffix == pymcnp.utils.types.McnpInteger(suffix)

    def test_invalid(self):
        for probability, suffix in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                probability = pymcnp.utils.types.McnpReal(probability)
                suffix = pymcnp.utils.types.McnpInteger(suffix)
                pymcnp.inp.CellPd(probability, suffix)


class Test_CellTmp:
    """
    Tests ``CellTmp``.
    """

    VALID_EXAMPLES = [(4.26, 1), (3.14, 5), (0.24, 7), (9.43, 3)]

    INVALID_EXAMPLES = [(-0.53, 1), (0.0, 2), (-1.43, 5)]

    def test_valid(self):
        for temperature, suffix in self.VALID_EXAMPLES:
            _temperature = pymcnp.utils.types.McnpReal(temperature)
            _suffix = pymcnp.utils.types.McnpInteger(suffix)

            obj = pymcnp.inp.CellTmp(_temperature, _suffix)

            assert obj.keyword == pymcnp.inp.CellKeyword.TMP
            assert obj.temperature == pymcnp.utils.types.McnpReal(temperature)
            assert obj.suffix == pymcnp.utils.types.McnpInteger(suffix)

    def test_invalid(self):
        for temperature, suffix in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                temperature = pymcnp.utils.types.McnpReal(temperature)
                suffix = pymcnp.utils.types.McnpInteger(suffix)
                pymcnp.inp.CellTmp(temperature, suffix)


class Test_CellU:
    """
    Tests ``CellU``.
    """

    VALID_EXAMPLES = [-99999999, 99999999, 0, 1, -1]

    INVALID_EXAMPLES = [-100000000, 100000000, 100000432]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.McnpInteger(number)

            obj = pymcnp.inp.CellU(_number)

            assert obj.keyword == pymcnp.inp.CellKeyword.U
            assert obj.number == pymcnp.utils.types.McnpInteger(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                number = pymcnp.utils.types.McnpInteger(number)
                pymcnp.inp.CellU(number)


class Test_CellTrcl_Form1:
    """
    Tests ``CellTrcl``.
    """

    VALID_EXAMPLES = [1, 67, 999]

    INVALID_EXAMPLES = [-1000, 1000, 2343]

    def test_valid(self):
        for value in self.VALID_EXAMPLES:
            _value = int(value)

            obj = pymcnp.inp.CellTrcl_Form1(_value)

            assert obj.keyword == pymcnp.inp.CellKeyword.TRCL
            assert obj.value == int(value)

    def test_invalid(self):
        for value in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                value = int(value)
                pymcnp.inp.CellTrcl_Form1(value)


class Test_CellLat:
    """
    Tests ``CellLat``.
    """

    VALID_EXAMPLES = [1, 2]

    INVALID_EXAMPLES = [0, -1, 100]

    def test_valid(self):
        for shape in self.VALID_EXAMPLES:
            _shape = pymcnp.utils.types.McnpInteger(shape)

            obj = pymcnp.inp.CellLat(_shape)

            assert obj.keyword == pymcnp.inp.CellKeyword.LAT
            assert obj.shape == pymcnp.utils.types.McnpInteger(shape)

    def test_invalid(self):
        for shape in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                shape = pymcnp.utils.types.McnpInteger(shape)
                pymcnp.inp.CellLat(shape)


class Test_CellFill_Form1:
    """
    Tests ``CellFill_Form1``.
    """

    VALID_EXAMPLES = [0, 234, 99999999]

    INVALID_EXAMPLES = [-100, 100000000, -1]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.McnpInteger(number)

            obj = pymcnp.inp.CellFill_Form1(_number)

            assert obj.keyword == pymcnp.inp.CellKeyword.FILL
            assert obj.number == pymcnp.utils.types.McnpInteger(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                number = pymcnp.utils.types.McnpInteger(number)
                pymcnp.inp.CellFill_Form1(number)


class Test_CellElpt:
    """
    Tests ``CellElpt``.
    """

    VALID_EXAMPLES = [(-234.05434, ('n', 'p')), (345034950, 'n'), (34534.3453, ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for cutoff, designator in self.VALID_EXAMPLES:
            _cutoff = pymcnp.utils.types.McnpReal(cutoff)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellElpt(_cutoff, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.ELPT
            assert obj.cutoff == pymcnp.utils.types.McnpReal(cutoff)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for cutoff, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                cutoff = pymcnp.utils.types.McnpReal(cutoff)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellElpt(cutoff, designator)


class Test_CellCosy:
    """
    Tests ``CellCosy``.
    """

    VALID_EXAMPLES = [1, 2, 3, 4, 5, 6]

    INVALID_EXAMPLES = [0, 100000000, -1]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.McnpInteger(number)

            obj = pymcnp.inp.CellCosy(_number)

            assert obj.keyword == pymcnp.inp.CellKeyword.COSY
            assert obj.number == pymcnp.utils.types.McnpInteger(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                number = pymcnp.utils.types.McnpInteger(number)
                pymcnp.inp.CellCosy(number)


class Test_CellBflcl:
    """
    Tests ``CellBflcl``.
    """

    VALID_EXAMPLES = [0, 4, 10]

    INVALID_EXAMPLES = [-1, -345, -1000]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.McnpInteger(number)

            obj = pymcnp.inp.CellBflcl(_number)

            assert obj.keyword == pymcnp.inp.CellKeyword.BFLCL
            assert obj.number == pymcnp.utils.types.McnpInteger(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                number = pymcnp.utils.types.McnpInteger(number)
                pymcnp.inp.CellBflcl(number)


class Test_CellUnc:
    """
    Tests ``CellUnc``.
    """

    VALID_EXAMPLES = [(0, '#'), (1, 'e')]

    INVALID_EXAMPLES = [(-1, ('n', '#')), (345, ('@', '#')), (-1000, 'e'), (2, ('p', '_'))]

    def test_valid(self):
        for setting, designator in self.VALID_EXAMPLES:
            _setting = pymcnp.utils.types.McnpInteger(setting)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.CellUnc(_setting, _designator)

            assert obj.keyword == pymcnp.inp.CellKeyword.UNC
            assert obj.setting == pymcnp.utils.types.McnpInteger(setting)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for setting, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.McnpError):
                setting = pymcnp.utils.types.McnpInteger(setting)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.CellUnc(setting, designator)
