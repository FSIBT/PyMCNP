import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tr_4(_option.DataOption):
    """
    Represents INP tr variation #4 elements.

    Attributes:
        prefix: Star prefix.
        suffix: Data card option suffix.
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        system: Coordinate system setting.
    """

    _KEYWORD = 'tr'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'system': types.Integer,
    }

    _REGEX = re.compile(rf'\A([*])?tr(\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, suffix: types.Integer, x: types.Real, y: types.Real, z: types.Real, prefix: types.String = None, system: types.Integer = None):
        """
        Initializes ``Tr_4``.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if system is not None and not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, system)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                system,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.suffix: typing.Final[types.Integer] = suffix
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.system: typing.Final[types.Integer] = system


@dataclasses.dataclass
class TrBuilder_4(_option.DataOptionBuilder):
    """
    Builds ``Tr_4``.

    Attributes:
        prefix: Star prefix.
        suffix: Data card option suffix.
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        system: Coordinate system setting.
    """

    suffix: str | int | types.Integer
    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real
    prefix: str | types.String = None
    system: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TrBuilder_4`` into ``Tr_4``.

        Returns:
            ``Tr_4`` for ``TrBuilder_4``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        system = self.system
        if isinstance(self.system, types.Integer):
            system = self.system
        elif isinstance(self.system, int):
            system = types.Integer(self.system)
        elif isinstance(self.system, str):
            system = types.Integer.from_mcnp(self.system)

        return Tr_4(
            prefix=prefix,
            suffix=suffix,
            x=x,
            y=y,
            z=z,
            system=system,
        )

    @staticmethod
    def unbuild(ast: Tr_4):
        """
        Unbuilds ``Tr_4`` into ``TrBuilder_4``

        Returns:
            ``TrBuilder_4`` for ``Tr_4``.
        """

        return TrBuilder_4(
            prefix=copy.deepcopy(ast.prefix),
            suffix=copy.deepcopy(ast.suffix),
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            z=copy.deepcopy(ast.z),
            system=copy.deepcopy(ast.system),
        )
