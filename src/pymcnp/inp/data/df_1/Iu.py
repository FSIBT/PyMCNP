import re
import copy
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

    _KEYWORD = 'iu'

    _ATTRS = {
        'units': types.Integer,
    }

    _REGEX = re.compile(rf'\Aiu( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, units: types.Integer):
        """
        Initializes ``Iu``.

        Parameters:
            units: Control units.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if units is None or not (isinstance(units.value, types.Jump) or units.value in {1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, units)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                units,
            ]
        )

        self.units: typing.Final[types.Integer] = units


@dataclasses.dataclass
class IuBuilder:
    """
    Builds ``Iu``.

    Attributes:
        units: Control units.
    """

    units: str | int | types.Integer

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
            units = types.Integer(self.units)
        elif isinstance(self.units, str):
            units = types.Integer.from_mcnp(self.units)

        return Iu(
            units=units,
        )

    @staticmethod
    def unbuild(ast: Iu):
        """
        Unbuilds ``Iu`` into ``IuBuilder``

        Returns:
            ``IuBuilder`` for ``Iu``.
        """

        return Iu(
            units=copy.deepcopy(ast.units),
        )
