import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Fir(DataOption_, keyword='fir'):
    """
    Represents INP fir elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        x1: Rectangular grid center x-coordinate.
        y1: Rectangular grid center y-coordinate.
        z1: Rectangular grid center z-coordinate.
        ro: Rectangular grid exclusion radius.
        x2: Reference direction x-coordinate.
        y2: Reference direction y-coordinate.
        z2: Reference direction z-coordinate.
        f1: Source contributions on/off.
        f2: Radial view of field.
        f3: Contribution offset setting.
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
        rf'\Afir(\d+):(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
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
        Initializes ``Fir``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            x1: Rectangular grid center x-coordinate.
            y1: Rectangular grid center y-coordinate.
            z1: Rectangular grid center z-coordinate.
            ro: Rectangular grid exclusion radius.
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
        if f2 is None:
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


@dataclasses.dataclass
class FirBuilder:
    """
    Builds ``Fir``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        x1: Rectangular grid center x-coordinate.
        y1: Rectangular grid center y-coordinate.
        z1: Rectangular grid center z-coordinate.
        ro: Rectangular grid exclusion radius.
        x2: Reference direction x-coordinate.
        y2: Reference direction y-coordinate.
        z2: Reference direction z-coordinate.
        f1: Source contributions on/off.
        f2: Radial view of field.
        f3: Contribution offset setting.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    x1: str | float | types.RealOrJump
    y1: str | float | types.RealOrJump
    z1: str | float | types.RealOrJump
    ro: str | float | types.RealOrJump
    x2: str | float | types.RealOrJump
    y2: str | float | types.RealOrJump
    z2: str | float | types.RealOrJump
    f1: str | float | types.RealOrJump
    f2: str | float | types.RealOrJump
    f3: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``FirBuilder`` into ``Fir``.

        Returns:
            ``Fir`` for ``FirBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if isinstance(self.x1, types.Real):
            x1 = self.x1
        elif isinstance(self.x1, float) or isinstance(self.x1, int):
            x1 = types.RealOrJump(self.x1)
        elif isinstance(self.x1, str):
            x1 = types.RealOrJump.from_mcnp(self.x1)

        if isinstance(self.y1, types.Real):
            y1 = self.y1
        elif isinstance(self.y1, float) or isinstance(self.y1, int):
            y1 = types.RealOrJump(self.y1)
        elif isinstance(self.y1, str):
            y1 = types.RealOrJump.from_mcnp(self.y1)

        if isinstance(self.z1, types.Real):
            z1 = self.z1
        elif isinstance(self.z1, float) or isinstance(self.z1, int):
            z1 = types.RealOrJump(self.z1)
        elif isinstance(self.z1, str):
            z1 = types.RealOrJump.from_mcnp(self.z1)

        if isinstance(self.ro, types.Real):
            ro = self.ro
        elif isinstance(self.ro, float) or isinstance(self.ro, int):
            ro = types.RealOrJump(self.ro)
        elif isinstance(self.ro, str):
            ro = types.RealOrJump.from_mcnp(self.ro)

        if isinstance(self.x2, types.Real):
            x2 = self.x2
        elif isinstance(self.x2, float) or isinstance(self.x2, int):
            x2 = types.RealOrJump(self.x2)
        elif isinstance(self.x2, str):
            x2 = types.RealOrJump.from_mcnp(self.x2)

        if isinstance(self.y2, types.Real):
            y2 = self.y2
        elif isinstance(self.y2, float) or isinstance(self.y2, int):
            y2 = types.RealOrJump(self.y2)
        elif isinstance(self.y2, str):
            y2 = types.RealOrJump.from_mcnp(self.y2)

        if isinstance(self.z2, types.Real):
            z2 = self.z2
        elif isinstance(self.z2, float) or isinstance(self.z2, int):
            z2 = types.RealOrJump(self.z2)
        elif isinstance(self.z2, str):
            z2 = types.RealOrJump.from_mcnp(self.z2)

        if isinstance(self.f1, types.Real):
            f1 = self.f1
        elif isinstance(self.f1, float) or isinstance(self.f1, int):
            f1 = types.RealOrJump(self.f1)
        elif isinstance(self.f1, str):
            f1 = types.RealOrJump.from_mcnp(self.f1)

        if isinstance(self.f2, types.Real):
            f2 = self.f2
        elif isinstance(self.f2, float) or isinstance(self.f2, int):
            f2 = types.RealOrJump(self.f2)
        elif isinstance(self.f2, str):
            f2 = types.RealOrJump.from_mcnp(self.f2)

        if isinstance(self.f3, types.Real):
            f3 = self.f3
        elif isinstance(self.f3, float) or isinstance(self.f3, int):
            f3 = types.RealOrJump(self.f3)
        elif isinstance(self.f3, str):
            f3 = types.RealOrJump.from_mcnp(self.f3)

        return Fir(
            suffix=suffix,
            designator=designator,
            x1=x1,
            y1=y1,
            z1=z1,
            ro=ro,
            x2=x2,
            y2=y2,
            z2=z2,
            f1=f1,
            f2=f2,
            f3=f3,
        )
