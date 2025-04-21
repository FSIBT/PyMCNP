import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Tr_4(DataOption, keyword='tr'):
    """
    Represents INP tr variation #4 elements.

    Attributes:
        suffix: Data card option suffix.
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        system: Coordinate system setting.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'x': types.RealOrJump,
        'y': types.RealOrJump,
        'z': types.RealOrJump,
        'system': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Atr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        x: types.RealOrJump,
        y: types.RealOrJump,
        z: types.RealOrJump,
        system: types.IntegerOrJump = None,
    ):
        """
        Initializes ``Tr_4``.

        Parameters:
            suffix: Data card option suffix.
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if system is not None and not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, system)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                system,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.x: typing.Final[types.RealOrJump] = x
        self.y: typing.Final[types.RealOrJump] = y
        self.z: typing.Final[types.RealOrJump] = z
        self.system: typing.Final[types.IntegerOrJump] = system


@dataclasses.dataclass
class TrBuilder_4:
    """
    Builds ``Tr_4``.

    Attributes:
        suffix: Data card option suffix.
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        system: Coordinate system setting.
    """

    suffix: str | int | types.Integer
    x: str | float | types.RealOrJump
    y: str | float | types.RealOrJump
    z: str | float | types.RealOrJump
    system: str | int | types.IntegerOrJump = None

    def build(self):
        """
        Builds ``TrBuilder_4`` into ``Tr_4``.

        Returns:
            ``Tr_4`` for ``TrBuilder_4``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.RealOrJump(self.x)
        elif isinstance(self.x, str):
            x = types.RealOrJump.from_mcnp(self.x)

        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.RealOrJump(self.y)
        elif isinstance(self.y, str):
            y = types.RealOrJump.from_mcnp(self.y)

        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.RealOrJump(self.z)
        elif isinstance(self.z, str):
            z = types.RealOrJump.from_mcnp(self.z)

        system = None
        if isinstance(self.system, types.Integer):
            system = self.system
        elif isinstance(self.system, int):
            system = types.IntegerOrJump(self.system)
        elif isinstance(self.system, str):
            system = types.IntegerOrJump.from_mcnp(self.system)

        return Tr_4(
            suffix=suffix,
            x=x,
            y=y,
            z=z,
            system=system,
        )
