"""
Contains the ``Fill`` subclass of ``CellOption``.
"""

import re
from typing import Final, Union

from ..cell_entry import CellEntry
from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class FillEntry(CellEntry):
    """
    ``FillEntry`` implements ``CellEntry``.

    Attributes:
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        xx: Rotation matrix xx' component.
        xy: Rotation matrix xy' component.
        xz: Rotation matrix xz' component.
        yx: Rotation matrix yx' component.
        yy: Rotation matrix yy' component.
        yz: Rotation matrix yz' component.
        zx: Rotation matrix zx' component.
        zy: Rotation matrix zy' component.
        zz: Rotation matrix zz' component.
        m: Coordinate system setting.
    """

    def __init__(
        self,
        x: types.McnpReal,
        y: types.McnpReal,
        z: types.McnpReal,
        xx: types.McnpReal,
        xy: types.McnpReal,
        xz: types.McnpReal,
        yx: types.McnpReal,
        yy: types.McnpReal,
        yz: types.McnpReal,
        zx: types.McnpReal,
        zy: types.McnpReal,
        zz: types.McnpReal,
        m: types.McnpInteger,
    ):
        """
        Initializes ``FillEntry``.

        Parameters:
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
            xx: Rotation matrix xx' component.
            xy: Rotation matrix xy' component.
            xz: Rotation matrix xz' component.
            yx: Rotation matrix yx' component.
            yy: Rotation matrix yy' component.
            yz: Rotation matrix yz' component.
            zx: Rotation matrix zx' component.
            zy: Rotation matrix zy' component.
            zz: Rotation matrix zz' component.
            m: Coordinate system setting.

        Raises:
            McnpError: INVALID_CELL_ENTRY_PARAMETER.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if xx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if xy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if xz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if yx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if yy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if yz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if zx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if zy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if zz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        if m is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_ENTRY_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z
        self.xx: Final[types.McnpReal] = xx
        self.xy: Final[types.McnpReal] = xy
        self.xz: Final[types.McnpReal] = xz
        self.yx: Final[types.McnpReal] = yx
        self.yy: Final[types.McnpReal] = yy
        self.yz: Final[types.McnpReal] = yz
        self.zx: Final[types.McnpReal] = zx
        self.zy: Final[types.McnpReal] = zy
        self.zz: Final[types.McnpReal] = zz
        self.m: Final[types.McnpInteger] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FillEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``FillEntry``.

        Returns:
            ``FillEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        x = types.McnpReal(tokens.popl())
        y = types.McnpReal(tokens.popl())
        z = types.McnpReal(tokens.popl())
        xx = types.McnpReal(tokens.popl())
        xy = types.McnpReal(tokens.popl())
        xz = types.McnpReal(tokens.popl())
        yx = types.McnpReal(tokens.popl())
        yy = types.McnpReal(tokens.popl())
        yz = types.McnpReal(tokens.popl())
        zx = types.McnpReal(tokens.popl())
        zy = types.McnpReal(tokens.popl())
        zz = types.McnpReal(tokens.popl())
        m = types.McnpInteger(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return FillEntry(x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)

    def to_mcnp(self):
        """
        Generates INP from ``FillEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``FillEntry``.
        """

        return f'{self.x} {self.y} {self.z} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.zx} {self.zy} {self.zz} {self.m}'


class Fill(CellOption):
    """
    Represents INP cell card fill options.

    ``Fill`` implements ``_card.CardOption``.
    """

    def __init__(self, number: types.McnpInteger):
        raise NotImplementedError

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError


class Fill_Form1(Fill):
    """
    Represents INP cell card fill form #1 options.

    ``Fill_Form1`` implements ``_card.CardOption``.

    Attributes:
        number: Fill cell option value or value(s) tuple.
        transform: Option transformation number of specification.
    """

    def __init__(
        self, number: types.McnpInteger, transform: Union[FillEntry, types.McnpInteger] = None
    ):
        """
        Initializes ``Fill_Form1``.

        Parameters:
            number: Fill cell option value or value(s) tuple.
            transform: Option transformation number of specification.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(number))

        if transform is not None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(number))

        self.keyword: Final[CellKeyword] = CellKeyword.FILL
        self.value: Final[types.McnpInteger] = (number, transform)
        self.number: Final[types.McnpInteger] = number
        self.transform: Final[types.McnpInteger] = transform

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fill_Form1`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fill_Form1``.

        Returns:
            ``Fill_Form1`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| |:|\(|\)', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        keyword = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        keyword = keyword[0] if keyword else ''
        if keyword != 'fill':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        number = types.McnpInteger.from_mcnp(tokens.popl())
        if tokens:
            if tokens.peekl() == '(' and tokens.peekr() == ')':
                tokens.popl()
                tokens.popr()

            if len(tokens) > 1:
                transform = CellEntry.from_mcnp(
                    ' '.join(tokens.popl() for _ in range(0, len(tokens)))
                )
            else:
                transform = types.McnpInteger.from_mcnp(tokens.popl())
        else:
            transform = None

        return Fill_Form1(number, transform=transform)


class Fill_Form2(Fill):
    """
    Represents INP cell card fill form #2 options.

    ``Fill_Form2`` implements ``_card.CardOption``.

    Attributes:
        i1: Lattice element parameter #1 in the i direction.
        i2: Lattice element parameter #2 in the i direction.
        j1: Lattice element parameter #1 in the j direction.
        j2: Lattice element parameter #2 in the j direction.
        k1: Lattice element parameter #1 in the k direction.
        k2: Lattice element parameter #2 in the k direction.
        numbers: Tuple of unvierse numbers for fill.
    """

    def __init__(
        self,
        i1: types.McnpInteger,
        i2: types.McnpInteger,
        j1: types.McnpInteger,
        j2: types.McnpInteger,
        k1: types.McnpInteger,
        k2: types.McnpInteger,
        numbers: tuple[types.McnpInteger],
    ):
        """
        Initializes ``Fill_Form1``.

        Parameters:
            i1: Lattice element parameter #1 in the i direction.
            i2: Lattice element parameter #2 in the i direction.
            j1: Lattice element parameter #1 in the j direction.
            j2: Lattice element parameter #2 in the j direction.
            k1: Lattice element parameter #1 in the k direction.
            k2: Lattice element parameter #2 in the k direction.
            numbers: Tuple of unvierse numbers for fill.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if i1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(i1))

        if i2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(i2))

        if j1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(j1))

        if j2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(j2))

        if k1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(k1))

        if k2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(k2))

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(numbers))

        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(entry))

        self.keyword: Final[CellKeyword] = CellKeyword.FILL
        self.value: Final[types.McnpInteger] = (i1, i2, j1, j2, k1, k2, numbers)
        self.i1: Final[types.McnpInteger] = i1
        self.i2: Final[types.McnpInteger] = i2
        self.j1: Final[types.McnpInteger] = j1
        self.j2: Final[types.McnpInteger] = j2
        self.k1: Final[types.McnpInteger] = k1
        self.k2: Final[types.McnpInteger] = k2
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fill_Form2`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fill_Form2``.

        Returns:
            ``Fill_Form2`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        keyword = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        keyword = keyword[0] if keyword else ''
        if keyword != 'fill':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        token = tokens.popl().split(':')
        if len(token) != 2:
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)

        i1 = types.McnpInteger.from_mcnp(token[0])
        i2 = types.McnpInteger.from_mcnp(token[1])

        token = tokens.popl().split(':')
        if len(token) != 2:
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)

        j1 = types.McnpInteger.from_mcnp(token[0])
        j2 = types.McnpInteger.from_mcnp(token[1])

        token = tokens.popl().split(':')
        if len(token) != 2:
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)

        k1 = types.McnpInteger.from_mcnp(token[0])
        k2 = types.McnpInteger.from_mcnp(token[1])

        numbers = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        return Fill_Form2(i1, i2, j1, j2, k1, k2, numbers)
