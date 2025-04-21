import re
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Refpnt(BfldOption, keyword='refpnt'):
    """
    Represents INP refpnt elements.

    Attributes:
        point: Point anywhere on the quadrapole beam.
    """

    _ATTRS = {
        'point': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Arefpnt((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Refpnt``.

        Parameters:
            point: Point anywhere on the quadrapole beam.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, point)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                point,
            ]
        )

        self.point: typing.Final[types.Tuple[types.RealOrJump]] = point


@dataclasses.dataclass
class RefpntBuilder:
    """
    Builds ``Refpnt``.

    Attributes:
        point: Point anywhere on the quadrapole beam.
    """

    point: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``RefpntBuilder`` into ``Refpnt``.

        Returns:
            ``Refpnt`` for ``RefpntBuilder``.
        """

        point = []
        for item in self.point:
            if isinstance(item, types.RealOrJump):
                point.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                point.append(types.RealOrJump(item))
            elif isinstance(item, str):
                point.append(types.RealOrJump.from_mcnp(item))
        point = types.Tuple(point)

        return Refpnt(
            point=point,
        )
