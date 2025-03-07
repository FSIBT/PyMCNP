import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fic(DataOption_, keyword='fic'):
    """
    Represents INP fic elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'x1': types.Real,
        'y1': types.Real,
        'z1': types.Real,
        'ro': types.Real,
        'x2': types.Real,
        'y2': types.Real,
        'z2': types.Real,
        'f1': types.Real,
        'f2': types.Real,
        'f3': types.Real,
    }

    _REGEX = re.compile(
        rf'fic(\S+):(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        x1: types.Real,
        y1: types.Real,
        z1: types.Real,
        ro: types.Real,
        x2: types.Real,
        y2: types.Real,
        z2: types.Real,
        f1: types.Real,
        f2: types.Real,
        f3: types.Real,
    ):
        """
        Initializes ``Fic``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            x1: Cylindrical grid center x-coordinate.
            y1: Cylindrical grid center y-coordinate.
            z1: Cylindrical grid center z-coordinate.
            ro: Cylindrical grid exclusion radius.
            x2: Reference direction x-coordinate.
            y2: Reference direction y-coordinate.
            z2: Reference direction z-coordinate.
            f1: Source contributions on/off.
            f2: Radial view of field.
            f3: Contribution offset setting.

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
        if f1 is None or f1 not in {0, -1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, f1)
        if f2 is None or not (f2 != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, f2)
        if f3 is None or f2 not in {0, -1}:
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
        self.x1: typing.Final[types.Real] = x1
        self.y1: typing.Final[types.Real] = y1
        self.z1: typing.Final[types.Real] = z1
        self.ro: typing.Final[types.Real] = ro
        self.x2: typing.Final[types.Real] = x2
        self.y2: typing.Final[types.Real] = y2
        self.z2: typing.Final[types.Real] = z2
        self.f1: typing.Final[types.Real] = f1
        self.f2: typing.Final[types.Real] = f2
        self.f3: typing.Final[types.Real] = f3
