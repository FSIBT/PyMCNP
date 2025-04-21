import re
import typing
import dataclasses


from ._option import Df_1Option
from ....utils import types
from ....utils import errors


class Iu(Df_1Option, keyword='iu'):
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if units is None or units not in {1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, units)

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

        if isinstance(self.units, types.Integer):
            units = self.units
        elif isinstance(self.units, int):
            units = types.IntegerOrJump(self.units)
        elif isinstance(self.units, str):
            units = types.IntegerOrJump.from_mcnp(self.units)

        return Iu(
            units=units,
        )
