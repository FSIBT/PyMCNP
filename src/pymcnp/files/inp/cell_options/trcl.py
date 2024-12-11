"""
Contains the ``Trcl`` subclass of ``CellOption``.
"""

import re
from typing import Final

from ..cell_entry import CellEntry
from ..cell_option import CellOption
from ..cell_keyword import CellKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class TrclEntry(CellEntry):
    """
    ``TrclEntry`` implements ``CellEntry``.

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
        Initializes ``TrclEntry``.

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
        Generates ``TrclEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``TrclEntry``.

        Returns:
            ``TrclEntry`` object.

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

        return TrclEntry(x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)


class Trcl(CellOption):
    """
    Represents INP cell card trcl options.

    ``Trcl`` implements ``_card.CardOption``.
    """

    def __init__(self, number: types.McnpInteger):
        raise NotImplementedError

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError


class Trcl_Form1(CellOption):
    """
    Represents INP cell card trcl options.

    ``Trcl_Form1`` implements ``_card.CardOption``.

    Attributes:
        number: Cell coordinate transformation number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Trcl_Form1``.

        Parameters:
            number: Cell coordinate transformation number.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if number is None or not (1 <= number <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str(number))

        self.keyword: Final[CellKeyword] = CellKeyword.TRCL
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Trcl_Form1`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Trcl_Form1``.

        Returns:
            ``Trcl_Form1`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| |:', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        keyword = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        keyword = keyword[0] if keyword else ''
        if keyword != 'trcl':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        number = types.McnpInteger.from_mcnp(tokens.popl())

        return Trcl_Form1(number)


class Trcl_Form2(CellOption):
    """
    Represents INP cell card trcl options.

    ``Trcl_Form2`` implements ``_card.CardOption``.

    Attributes:
        transform: Cell coordinate transformation specifier.
    """

    def __init__(self, transform: TrclEntry):
        """
        Initializes ``Trcl_Form2``.

        Parameters:
            transform: Cell coordinate transformation specifier.

        Raises:
            McnpError: INVALID_CELL_OPTION_VALUE.
        """

        if transform is None or not (1 <= transform <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, transform.to_mcnp())

        self.keyword: Final[CellKeyword] = CellKeyword.TRCL
        self.value: Final[TrclEntry] = transform
        self.transform: Final[TrclEntry] = transform

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Trcl_Form2`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Trcl_Form2``.

        Returns:
            ``Trcl_Form2`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| |:', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        keyword = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        keyword = keyword[0] if keyword else ''
        if keyword != 'trcl':
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))

        tokens.popl()
        transform = TrclEntry.from_mcnp(' '.join(tokens.popl() for _ in range(0, len(tokens))))

        return Trcl_Form2(transform)
