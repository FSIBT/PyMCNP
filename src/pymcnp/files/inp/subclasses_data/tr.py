"""
Contains the ``Tr`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataEntry
from ....utils import types, errors, _parser


class TrDisplacementEntry(DataEntry):
    """
    Represents INP TrDisplacement data card entry.

    ``TrDisplacementEntry`` implements ``DataEntry``.

    Attributes:
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
    """

    def __init__(self, x: types.McnpReal, y: types.McnpReal, z: types.McnpReal):
        """
        Initializes ``TrDisplacementEntry``.

        Parameters:
                x: Displacement vector x component.
                y: Displacement vector y component.
                z: Displacement vector z component.

        Raises:
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TrDisplacementEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``TrDisplacementEntry``.

        Returns:
            ``TrDisplacementEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        x = types.McnpReal.from_mcnp(tokens.popl())
        y = types.McnpReal.from_mcnp(tokens.popl())
        z = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return TrDisplacementEntry(x, y, z)

    def to_mcnp(self):
        """
        Generates INP from ``TrDisplacementEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``TrDisplacementEntry``.
        """

        return f'{self.x.to_mcnp()} {self.y.to_mcnp()} {self.z.to_mcnp()}'


class TrRotationEntry(DataEntry):
    """
    Represents INP TrRotation data card entry.

    ``TrRotationEntry`` implements ``DataEntry``.

    Attributes:
            xx: Rotation matrix xx' component.
            xy: Rotation matrix xy' component.
            xz: Rotation matrix xz' component.
            yx: Rotation matrix yx' component.
            yy: Rotation matrix yy' component.
            yz: Rotation matrix yz' component.
            zx: Rotation matrix zx' component.
            zy: Rotation matrix zy' component.
            zz: Rotation matrix zz' component.
    """

    def __init__(
        self,
        xx: types.McnpReal,
        xy: types.McnpReal,
        xz: types.McnpReal,
        yx: types.McnpReal,
        yy: types.McnpReal,
        yz: types.McnpReal,
        zx: types.McnpReal,
        zy: types.McnpReal,
        zz: types.McnpReal,
    ):
        """
        Initializes ``TrRotationEntry``.

        Parameters:
                xx: Rotation matrix xx' component.
                xy: Rotation matrix xy' component.
                xz: Rotation matrix xz' component.
                yx: Rotation matrix yx' component.
                yy: Rotation matrix yy' component.
                yz: Rotation matrix yz' component.
                zx: Rotation matrix zx' component.
                zy: Rotation matrix zy' component.
                zz: Rotation matrix zz' component.

        Raises:
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
        """

        if xx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if xy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if xz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if yx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if yy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if yz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if zx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if zy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if zz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        self.xx: Final[types.McnpReal] = xx
        self.xy: Final[types.McnpReal] = xy
        self.xz: Final[types.McnpReal] = xz
        self.yx: Final[types.McnpReal] = yx
        self.yy: Final[types.McnpReal] = yy
        self.yz: Final[types.McnpReal] = yz
        self.zx: Final[types.McnpReal] = zx
        self.zy: Final[types.McnpReal] = zy
        self.zz: Final[types.McnpReal] = zz

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TrRotationEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``TrRotationEntry``.

        Returns:
            ``TrRotationEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        xx = types.McnpReal.from_mcnp(tokens.popl())
        xy = types.McnpReal.from_mcnp(tokens.popl())
        xz = types.McnpReal.from_mcnp(tokens.popl())
        yx = types.McnpReal.from_mcnp(tokens.popl())
        yy = types.McnpReal.from_mcnp(tokens.popl())
        yz = types.McnpReal.from_mcnp(tokens.popl())
        zx = types.McnpReal.from_mcnp(tokens.popl())
        zy = types.McnpReal.from_mcnp(tokens.popl())
        zz = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return TrRotationEntry(xx, xy, xz, yx, yy, yz, zx, zy, zz)

    def to_mcnp(self):
        """
        Generates INP from ``TrRotationEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``TrRotationEntry``.
        """

        return f'{self.xx.to_mcnp()} {self.xy.to_mcnp()} {self.xz.to_mcnp()} {self.yx.to_mcnp()} {self.yy.to_mcnp()} {self.yz.to_mcnp()} {self.zx.to_mcnp()} {self.zy.to_mcnp()} {self.zz.to_mcnp()}'


class Tr(Data):
    """
    Represents INP tr data cards.

    ``Tr`` implements ``Data``.

    Attributes:
        displacement: Tuple for displacement vector.
        rotation: Tuple for rotation matrix.
        system: Coordinate system setting.
        suffix: Data card suffix..
    """

    def __init__(
        self,
        displacement: TrDisplacementEntry,
        rotation: TrRotationEntry,
        system: types.McnpInteger,
        suffix: types.McnpInteger,
    ):
        """
        Initializes ``Tr``.

        Parameters:
            displacement: Tuple for displacement vector.
            rotation: Tuple for rotation matrix.
            system: Coordinate system setting.
            suffix: Data card suffix..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if displacement is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(displacement))

        if rotation is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(rotation))

        if system is None or not (system == -1 or system == 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(system))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.TR
        self.parameters: Final[tuple[any]] = tuple(
            [displacement] + [rotation] + [system] + [suffix]
        )
        self.displacement: Final[TrDisplacementEntry] = displacement
        self.rotation: Final[TrRotationEntry] = rotation
        self.system: Final[types.McnpInteger] = system
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'tr{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tr`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for tr data cards.

        Returns:
            ``Tr`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |:|=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        mnemonic = mnemonic[0] if mnemonic else ''
        if mnemonic != 'tr':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        displacement = TrDisplacementEntry.from_mcnp(' '.join([tokens.popl() for _ in range(0, 3)]))
        rotation = TrRotationEntry.from_mcnp(' '.join([tokens.popl() for _ in range(0, 9)]))
        system = types.McnpInteger.from_mcnp(tokens.popl())
        suffix = types.McnpInteger.from_mcnp(tokens.popl())

        data = Tr(displacement, rotation, system, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Tr`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Tr``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {self.displacement.to_mcnp()} {self.rotation.to_mcnp()} {self.system.to_mcnp()} {self.suffix.to_mcnp()}'
        )
