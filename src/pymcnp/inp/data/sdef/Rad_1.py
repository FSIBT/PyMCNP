import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Rad_1(SdefOption):
    """
    Represents INP rad variation #1 elements.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    _KEYWORD = 'rad'

    _ATTRS = {
        'radial_distance': types.DistributionNumber,
    }

    _REGEX = re.compile(rf'\Arad( {types.DistributionNumber._REGEX.pattern})\Z')

    def __init__(self, radial_distance: types.DistributionNumber):
        """
        Initializes ``Rad_1``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if radial_distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radial_distance)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                radial_distance,
            ]
        )

        self.radial_distance: typing.Final[types.DistributionNumber] = radial_distance


@dataclasses.dataclass
class RadBuilder_1:
    """
    Builds ``Rad_1``.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    radial_distance: str | types.DistributionNumber

    def build(self):
        """
        Builds ``RadBuilder_1`` into ``Rad_1``.

        Returns:
            ``Rad_1`` for ``RadBuilder_1``.
        """

        radial_distance = self.radial_distance
        if isinstance(self.radial_distance, types.DistributionNumber):
            radial_distance = self.radial_distance
        elif isinstance(self.radial_distance, str):
            radial_distance = types.DistributionNumber.from_mcnp(self.radial_distance)

        return Rad_1(
            radial_distance=radial_distance,
        )

    @staticmethod
    def unbuild(ast: Rad_1):
        """
        Unbuilds ``Rad_1`` into ``RadBuilder_1``

        Returns:
            ``RadBuilder_1`` for ``Rad_1``.
        """

        return Rad_1(
            radial_distance=copy.deepcopy(ast.radial_distance),
        )
