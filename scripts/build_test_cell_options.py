"""
Contains script for building ``TestCellOption`` subclasses.
"""

from typing import Final

import _data


class CellOptionTestScheme:
    """
    Stores attribute metadata for metaprogramming.

    Attributes:
        name: Cell option name for ``CellOption``.
        valid: List of valid test parameters.
        invalid: List of invalid test parameters.
    """

    def __init__(self, name: str, valid: tuple[any], invalid: tuple[any]):
        """
        Initializies ``CellOptionTestScheme``.

        Attributes:
            name: Cell option name for ``CellOption``.
            valid: List of valid ``CellOption`` test parameters.
            invalid: List of invalid ``CellOption`` test parameters.
        """

        self.valid: Final[tuple[any]] = valid
        self.invalid: Final[tuple[any]] = invalid


CELL_OPTION_TESTS: Final[tuple[CellOptionTestScheme]] = (
    CellOptionTestScheme(
        name='Imp',
        valid=[(0.5, ('n', 'p')), (1.5, ('n')), (-0.5, ('n', '#'))],
        invalid=[],
    ),
    CellOptionTestScheme(
        name='Vol',
        valid=[0.5, 1.5, 0.0],
        invalid=[-1.5, -2.5, -0.1],
    ),
    CellOptionTestScheme(
        name='Pwt',
        valid=[0.5, 1.5, -0.5],
        invalid=[],
    ),
    CellOptionTestScheme(
        name='Ext',
        valid=[('0.5', ('n', 'p')), ('0.9', ('n')), ('-0.5', ('n', '#'))],
        invalid=[],
    ),
    CellOptionTestScheme(
        name='Fcl',
        valid=[(0.5, ('n', 'p')), (0.9, ('n')), (-0.5, ('n', '#'))],
        invalid=[(2.51, ('n', 'p')), (3.94, ('n')), (-1.3, ('n', '#'))],
    ),
    CellOptionTestScheme(
        name='Wwn',
        valid=[(0.5, 3, ('n', 'p')), (0.9, 8, ('n')), (-1.0, 2, ('n', '#'))],
        invalid=[],
    ),
    CellOptionTestScheme(
        name='Dxc',
        valid=[(0.5, 3, ('n', 'p')), (0.9, 8, ('n')), (0.0, 2, ('n', '#'))],
        invalid=[(-1.0, 2, ('n'))],
    ),
    CellOptionTestScheme(
        name='Nonu',
        valid=[0, 1, 2],
        invalid=[-1, 3, 100],
    ),
    CellOptionTestScheme(
        name='Pd',
        valid=[(0, 5), (0.5, 7), (1, 3)],
        invalid=[(-1, 1), (3, 2), (100, 5)],
    ),
    CellOptionTestScheme(
        name='Tmp',
        valid=[(4.26, 1), (3.14, 5), (0.24, 7), (9.43, 3)],
        invalid=[(-0.53, 1), (00.00, 2), (-1.43, 5)],
    ),
    CellOptionTestScheme(
        name='U',
        valid=[-99_999_999, 99_999_999, 0, 1, -1],
        invalid=[-100_000_000, 100_000_000, 100_000_432],
    ),
    CellOptionTestScheme(
        name='Trcl',
        valid=[1, 67, 999],
        invalid=[-1000, 1000, 2343],
    ),
    CellOptionTestScheme(
        name='Lat',
        valid=[1, 2],
        invalid=[0, -1, 100],
    ),
    CellOptionTestScheme(
        name='Fill',
        valid=[0, 234, 99_999_999],
        invalid=[-100, 100_000_000, -1],
    ),
    CellOptionTestScheme(
        name='Elpt',
        valid=[(-234.05434, ('n', 'p')), (345034950, ('n')), (34534.3453, ('n', '#'))],
        invalid=[],
    ),
    CellOptionTestScheme(
        name='Cosy',
        valid=[1, 2, 3, 4, 5, 6],
        invalid=[0, 100_000_000, -1],
    ),
    CellOptionTestScheme(
        name='Bflcl',
        valid=[0, 4, 10],
        invalid=[-1, -345, -1000],
    ),
    CellOptionTestScheme(
        name='Unc',
        valid=[(0, ('#')), (1, ('e'))],
        invalid=[(-1, ('n', '#')), (345, ('@', '#')), (-1000, ('e')), (2, ('p', '_'))],
    ),
)


def build_TestCellOption(cell_option: _data.CellOptionScheme, test: CellOptionTestScheme):
    o = ''

    # TEST_VALID

    o += f'class Test_Cell{cell_option.name}:\n'
    o += '    """\n'
    o += f'    Tests ``Cell{cell_option.name}``.\n'
    o += '    """\n'
    o += '\n'
    o += f'    VALID_EXAMPLES = {str(test.valid)}\n'
    o += '\n'
    o += f'    INVALID_EXAMPLES = {str(test.invalid)}\n'
    o += '\n'
    o += '    def test_valid(self):\n'
    o += f'        for {", ".join(attribute.name for attribute in cell_option.attributes)} in self.VALID_EXAMPLES:\n'

    for attribute in cell_option.attributes:
        if attribute.type.startswith('types'):
            o += (
                f'            _{attribute.name} = pymcnp.utils.{attribute.type}({attribute.name})\n'
            )
        elif attribute.type == 'str':
            o += f'            _{attribute.name} = {attribute.name}\n'
        else:
            o += f'            _{attribute.name} = {attribute.type}({attribute.name})\n'

    o += '\n'
    o += f'            obj = pymcnp.inp.Cell{cell_option.name}(_{", _".join(attribute.name for attribute in cell_option.attributes)})\n'
    o += '\n'
    o += f'            assert obj.keyword == pymcnp.inp.CellKeyword.{cell_option.enum}\n'

    for attribute in cell_option.attributes:
        if attribute.type.startswith('types'):
            o += f'            assert obj.{attribute.name} == pymcnp.utils.{attribute.type}({attribute.name})\n'
        elif attribute.type == 'str':
            o += f'            assert obj.{attribute.name} == {attribute.name}\n'
        else:
            o += f'            assert obj.{attribute.name} == {attribute.type}({attribute.name})\n'

    o += '\n'
    o += '    def test_invalid(self):\n'
    o += f'        for {", ".join(attribute.name for attribute in cell_option.attributes)} in self.INVALID_EXAMPLES:\n'
    o += '            with pytest.raises(pymcnp.utils.errors.McnpError):\n'

    for attribute in cell_option.attributes:
        if attribute.type.startswith('types'):
            o += f'                {attribute.name} = pymcnp.utils.{attribute.type}({attribute.name})\n'
        elif attribute.type == 'str':
            o += f'                {attribute.name} = {attribute.name}\n'
        else:
            o += f'                {attribute.name} = {attribute.type}({attribute.name})\n'

    o += f'                pymcnp.inp.Cell{cell_option.name}({", ".join(attribute.name for attribute in cell_option.attributes)})\n'
    o += '\n'

    return o


for cell_option, test in zip(_data.CELL_OPTIONS, CELL_OPTION_TESTS):
    print(build_TestCellOption(cell_option, test))
