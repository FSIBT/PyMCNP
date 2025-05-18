import re
import typing
import dataclasses


from ._option import DfOption_1
from ....utils import types
from ....utils import errors


class Iu(DfOption_1):
    """
    Represents INP iu elements.

    Attributes:
        units: Control units.
    """

    _ATTRS = {
        'units': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aiu( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, units: types.IntegerOrJump):
        """
        Initializes ``Iu``.

        Parameters:
            units: Control units.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if units is None or not (isinstance(units, types.Jump) or units.value in {1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, units)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                units,
            ]
        )

        self.units: typing.Final[types.IntegerOrJump] = units


@dataclasses.dataclass
class IuBuilder:
    """
    Builds ``Iu``.

    Attributes:
        units: Control units.
    """

    units: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IuBuilder`` into ``Iu``.

        Returns:
            ``Iu`` for ``IuBuilder``.
        """

        units = self.units
        if isinstance(self.units, types.Integer):
            units = self.units
        elif isinstance(self.units, int):
            units = types.IntegerOrJump(self.units)
        elif isinstance(self.units, str):
            units = types.IntegerOrJump.from_mcnp(self.units)

        return Iu(
            units=units,
        )
