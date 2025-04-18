import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fip(DataOption_, keyword='fip'):
    """
    Represents INP fip elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'x1': types.RealOrJump,
        'y1': types.RealOrJump,
        'z1': types.RealOrJump,
        'ro': types.RealOrJump,
        'x2': types.RealOrJump,
        'y2': types.RealOrJump,
        'z2': types.RealOrJump,
        'f1': types.RealOrJump,
        'f2': types.RealOrJump,
        'f3': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Afip(\d+):(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        x1: types.RealOrJump,
        y1: types.RealOrJump,
        z1: types.RealOrJump,
        ro: types.RealOrJump,
        x2: types.RealOrJump,
        y2: types.RealOrJump,
        z2: types.RealOrJump,
        f1: types.RealOrJump,
        f2: types.RealOrJump,
        f3: types.RealOrJump,
    ):
        """
        Initializes ``Fip``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            x1: Pinhole center x-coordinate.
            y1: Pinhole center y-coordinate.
            z1: Pinhole center z-coordinate.
            ro: Pinhole exclusion radius.
            x2: Reference direction x-coordinate.
            y2: Reference direction y-coordinate.
            z2: Reference direction z-coordinate.
            f1: Cylindrical collimator radius.
            f2: Pinhole radius in the direction perpendiuclar to the reference direction.
            f3: Distance between pinhole and and detector grid.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x1)
        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y1)
        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z1)
        if ro is None or not (ro == 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ro)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x2)
        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y2)
        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z2)
        if f1 is None or not (f1 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, f1)
        if f2 is None or not (f2 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, f2)
        if f3 is None or not (f3 >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, f3)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x1,
                y1,
                z1,
                ro,
                x2,
                y2,
                z2,
                f1,
                f2,
                f3,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.x1: typing.Final[types.RealOrJump] = x1
        self.y1: typing.Final[types.RealOrJump] = y1
        self.z1: typing.Final[types.RealOrJump] = z1
        self.ro: typing.Final[types.RealOrJump] = ro
        self.x2: typing.Final[types.RealOrJump] = x2
        self.y2: typing.Final[types.RealOrJump] = y2
        self.z2: typing.Final[types.RealOrJump] = z2
        self.f1: typing.Final[types.RealOrJump] = f1
        self.f2: typing.Final[types.RealOrJump] = f2
        self.f3: typing.Final[types.RealOrJump] = f3
