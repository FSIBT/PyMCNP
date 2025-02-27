import pymcnp
import pytest


# class Test_CellEntry_Geometry:
#     """
#     Tests ``CellEntry_Geometry``.
#     """
#
#     VALID_EXAMPLES = [
#         '-15158',
#         '(116 8810)',
#         '#(16270052)',
#         '(127 4699712)',
#         '#(55912)',
#         '(38406:38406)',
#         '(61781 8810)',
#         '(8459955:54415642)',
#         '10002 4736',
#         '1000 25488',
#         '(43 2832)',
#         '59909',
#         '#(24)',
#         '+1',
#         '(20552 66588:10001 6572)',
#         '(46413 53335)',
#         '-203',
#         '(60608 60608)',
#         '82811712',
#         '(10001 7004 112147 7320)',
#         '+1000 00057',
#         '(17 17)',
#         '#(999 99998)',
#         '-1000 11505',
#         '#(1000 00100)',
#         '(85:38406)',
#         '-100022 492',
#         '-100000 010',
#     ]
#
#     INVALID_EXAMPLES = []
#
#     def test_valid(self):
#         for infix in self.VALID_EXAMPLES:
#             obj = pymcnp.inp.cell.CellEntry_Geometry.from_mcnp(f'{infix}')
#
#             assert obj.infix == infix
#
#     def test_invalid(self):
#         for infix in self.INVALID_EXAMPLES:
#             with pytest.raises(pymcnp.utils.pymcnp.utils.errors.InpError) as err:
#                 pymcnp.inp.cell.CellEntry_Geometry.from_mcnp(f'{infix}')
#
#             assert err.value.code == pymcnp.utils.errors.InpCode.INVALID_CELL_GEOMETRY


class Test_Imp:
    """
    Tests ``Imp``.
    """

    VALID_EXAMPLES = [(0.5, ('n', 'p')), (1.5, ('n',)), (-0.5, ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for importance, designator in self.VALID_EXAMPLES:
            _importance = pymcnp.utils.types.Real(importance)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Imp(_designator, _importance)

            assert obj.importance == pymcnp.utils.types.Real(importance)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for importance, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                importance = pymcnp.utils.types.Real(importance)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Imp(designator, importance)


class Test_Vol:
    """
    Tests ``Vol``.
    """

    VALID_EXAMPLES = [0.5, 1.5, 0.0]

    INVALID_EXAMPLES = [-1.5, -2.5, -0.1]

    def test_valid(self):
        for volume in self.VALID_EXAMPLES:
            _volume = pymcnp.utils.types.Real(volume)

            obj = pymcnp.inp.cell.Vol(_volume)

            assert obj.volume == pymcnp.utils.types.Real(volume)

    def test_invalid(self):
        for volume in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                volume = pymcnp.utils.types.Real(volume)
                pymcnp.inp.cell.Vol(volume)


class Test_Pwt:
    """
    Tests ``Pwt``.
    """

    VALID_EXAMPLES = [0.5, 1.5, -0.5]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for weight in self.VALID_EXAMPLES:
            _weight = pymcnp.utils.types.Real(weight)

            obj = pymcnp.inp.cell.Pwt(_weight)

            assert obj.weight == pymcnp.utils.types.Real(weight)

    def test_invalid(self):
        for weight in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                weight = pymcnp.utils.types.Real(weight)
                pymcnp.inp.cell.Pwt(weight)


class Test_Ext:
    """
    Tests ``Ext``.
    """

    VALID_EXAMPLES = [('0.5', ('n', 'p')), ('0.9', ('n',)), ('-0.5', ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for stretch, designator in self.VALID_EXAMPLES:
            _stretch = stretch
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Ext(_designator, _stretch)

            assert obj.stretch == stretch
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for stretch, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                stretch = stretch
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Ext(designator, stretch)


class Test_Fcl:
    """
    Tests ``Fcl``.
    """

    VALID_EXAMPLES = [(0.5, ('n', 'p')), (0.9, ('n',)), (-0.5, ('n', '#'))]

    INVALID_EXAMPLES = [(2.51, ('n', 'p')), (3.94, ('n',)), (-1.3, ('n', '#'))]

    def test_valid(self):
        for control, designator in self.VALID_EXAMPLES:
            _control = pymcnp.utils.types.Real(control)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Fcl(_designator, _control)

            assert obj.control == pymcnp.utils.types.Real(control)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for control, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                control = pymcnp.utils.types.Real(control)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Fcl(designator, control)


class Test_Wwn:
    """
    Tests ``Wwn``.
    """

    VALID_EXAMPLES = [(0.5, 3, ('n', 'p')), (0.9, 8, ('n',)), (-1.0, 2, ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for bound, suffix, designator in self.VALID_EXAMPLES:
            _bound = pymcnp.utils.types.Real(bound)
            _suffix = pymcnp.utils.types.Integer(suffix)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Wwn(_suffix, _designator, _bound)

            assert obj.bound == pymcnp.utils.types.Real(bound)
            assert obj.suffix == pymcnp.utils.types.Integer(suffix)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for bound, suffix, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                bound = pymcnp.utils.types.Real(bound)
                suffix = pymcnp.utils.types.Integer(suffix)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Wwn(suffix, designator, bound)


class Test_Dxc:
    """
    Tests ``Dxc``.
    """

    VALID_EXAMPLES = [(0.5, 3, ('n', 'p')), (0.9, 8, ('n',)), (0.0, 2, ('n', '#'))]

    INVALID_EXAMPLES = [(-1.0, 2, ('n',))]

    def test_valid(self):
        for probability, suffix, designator in self.VALID_EXAMPLES:
            _probability = pymcnp.utils.types.Real(probability)
            _suffix = pymcnp.utils.types.Integer(suffix)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Dxc(_suffix, _designator, _probability)

            assert obj.probability == pymcnp.utils.types.Real(probability)
            assert obj.suffix == pymcnp.utils.types.Integer(suffix)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for probability, suffix, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                probability = pymcnp.utils.types.Real(probability)
                suffix = pymcnp.utils.types.Integer(suffix)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Dxc(suffix, designator, probability)


class Test_Nonu:
    """
    Tests ``Nonu``.
    """

    VALID_EXAMPLES = [0, 1, 2]

    INVALID_EXAMPLES = [-1, 3, 100]

    def test_valid(self):
        for setting in self.VALID_EXAMPLES:
            _setting = pymcnp.utils.types.Integer(setting)

            obj = pymcnp.inp.cell.Nonu(_setting)

            assert obj.setting == pymcnp.utils.types.Integer(setting)

    def test_invalid(self):
        for setting in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                setting = pymcnp.utils.types.Integer(setting)
                pymcnp.inp.cell.Nonu(setting)


class Test_Pd:
    """
    Tests ``Pd``.
    """

    VALID_EXAMPLES = [(0, 5), (0.5, 7), (1, 3)]

    INVALID_EXAMPLES = [(-1, 1), (3, 2), (100, 5)]

    def test_valid(self):
        for probability, suffix in self.VALID_EXAMPLES:
            _probability = pymcnp.utils.types.Real(probability)
            _suffix = pymcnp.utils.types.Integer(suffix)

            obj = pymcnp.inp.cell.Pd(_suffix, _probability)

            assert obj.probability == pymcnp.utils.types.Real(probability)
            assert obj.suffix == pymcnp.utils.types.Integer(suffix)

    def test_invalid(self):
        for probability, suffix in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                probability = pymcnp.utils.types.Real(probability)
                suffix = pymcnp.utils.types.Integer(suffix)
                pymcnp.inp.cell.Pd(suffix, probability)


class Test_Tmp:
    """
    Tests ``Tmp``.
    """

    VALID_EXAMPLES = [(4.26, 1), (3.14, 5), (0.24, 7), (9.43, 3)]

    INVALID_EXAMPLES = [(-0.53, 1), (0.0, 2), (-1.43, 5)]

    def test_valid(self):
        for temperature, suffix in self.VALID_EXAMPLES:
            _temperature = pymcnp.utils.types.Real(temperature)
            _suffix = pymcnp.utils.types.Integer(suffix)

            obj = pymcnp.inp.cell.Tmp(_suffix, _temperature)

            assert obj.temperature == pymcnp.utils.types.Real(temperature)
            assert obj.suffix == pymcnp.utils.types.Integer(suffix)

    def test_invalid(self):
        for temperature, suffix in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                temperature = pymcnp.utils.types.Real(temperature)
                suffix = pymcnp.utils.types.Integer(suffix)
                pymcnp.inp.cell.Tmp(suffix, temperature)


class Test_U:
    """
    Tests ``U``.
    """

    VALID_EXAMPLES = [-99999999, 99999999, 0, 1, -1]

    INVALID_EXAMPLES = [-100000000, 100000000, 100000432]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.Integer(number)

            obj = pymcnp.inp.cell.U(_number)

            assert obj.number == pymcnp.utils.types.Integer(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                number = pymcnp.utils.types.Integer(number)
                pymcnp.inp.cell.U(number)


class Test_Trcl_0:
    """
    Tests ``Trcl_0``.
    """

    VALID_EXAMPLES = [1, 67, 999]

    INVALID_EXAMPLES = [-1000, 1000, 2343]

    def test_valid(self):
        for transformation in self.VALID_EXAMPLES:
            _transformation = int(transformation)

            obj = pymcnp.inp.cell.Trcl_0(_transformation)

            assert obj.transformation == _transformation

    def test_invalid(self):
        for value in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                value = int(value)
                pymcnp.inp.cell.Trcl_0(value)


class Test_Lat:
    """
    Tests ``Lat``.
    """

    VALID_EXAMPLES = [1, 2]

    INVALID_EXAMPLES = [0, -1, 100]

    def test_valid(self):
        for shape in self.VALID_EXAMPLES:
            _shape = pymcnp.utils.types.Integer(shape)

            obj = pymcnp.inp.cell.Lat(_shape)

            assert obj.shape == _shape

    def test_invalid(self):
        for shape in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                shape = pymcnp.utils.types.Integer(shape)
                pymcnp.inp.cell.Lat(shape)


class Test_Fill_0:
    """
    Tests ``Fill_0``.
    """

    VALID_EXAMPLES = [0, 234, 99999999]

    INVALID_EXAMPLES = [-100, 100000000, -1]

    def test_valid(self):
        for universe in self.VALID_EXAMPLES:
            _universe = pymcnp.utils.types.Integer(universe)

            obj = pymcnp.inp.cell.Fill_0(_universe)

            assert obj.universe == _universe

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                number = pymcnp.utils.types.Integer(number)
                pymcnp.inp.cell.Fill_0(number)


class Test_Elpt:
    """
    Tests ``Elpt``.
    """

    VALID_EXAMPLES = [(-234.05434, ('n', 'p')), (345034950, ('n',)), (34534.3453, ('n', '#'))]

    INVALID_EXAMPLES = []

    def test_valid(self):
        for cutoff, designator in self.VALID_EXAMPLES:
            _cutoff = pymcnp.utils.types.Real(cutoff)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Elpt(_designator, _cutoff)

            assert obj.cutoff == pymcnp.utils.types.Real(cutoff)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for cutoff, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                cutoff = pymcnp.utils.types.Real(cutoff)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Elpt(designator, cutoff)


class Test_Cosy:
    """
    Tests ``Cosy``.
    """

    VALID_EXAMPLES = [1, 2, 3, 4, 5, 6]

    INVALID_EXAMPLES = [0, 100000000, -1]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.Integer(number)

            obj = pymcnp.inp.cell.Cosy(_number)

            assert obj.number == pymcnp.utils.types.Integer(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                number = pymcnp.utils.types.Integer(number)
                pymcnp.inp.cell.Cosy(number)


class Test_Bflcl:
    """
    Tests ``Bflcl``.
    """

    VALID_EXAMPLES = [0, 4, 10]

    INVALID_EXAMPLES = [-1, -345, -1000]

    def test_valid(self):
        for number in self.VALID_EXAMPLES:
            _number = pymcnp.utils.types.Integer(number)

            obj = pymcnp.inp.cell.Bflcl(_number)

            assert obj.number == pymcnp.utils.types.Integer(number)

    def test_invalid(self):
        for number in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                number = pymcnp.utils.types.Integer(number)
                pymcnp.inp.cell.Bflcl(number)


class Test_Unc:
    """
    Tests ``Unc``.
    """

    VALID_EXAMPLES = [(0, ('#',)), (1, ('e',))]

    INVALID_EXAMPLES = [(-1, ('n', '#')), (345, ('@', '#')), (-1000, ('e',)), (2, ('p', '_'))]

    def test_valid(self):
        for setting, designator in self.VALID_EXAMPLES:
            _setting = pymcnp.utils.types.Integer(setting)
            _designator = pymcnp.utils.types.Designator(designator)

            obj = pymcnp.inp.cell.Unc(_designator, _setting)

            assert obj.setting == pymcnp.utils.types.Integer(setting)
            assert obj.designator == pymcnp.utils.types.Designator(designator)

    def test_invalid(self):
        for setting, designator in self.INVALID_EXAMPLES:
            with pytest.raises(pymcnp.utils.errors.InpError):
                setting = pymcnp.utils.types.Integer(setting)
                designator = pymcnp.utils.types.Designator(designator)
                pymcnp.inp.cell.Unc(designator, setting)
