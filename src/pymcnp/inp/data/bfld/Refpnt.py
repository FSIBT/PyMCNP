import re
import copy
import typing
import dataclasses


from ._option import BfldOption
from ....utils import types
from ....utils import errors


class Refpnt(BfldOption):
    """
    Represents INP refpnt elements.

    Attributes:
        point: Point anywhere on the quadrapole beam.
    """

    _KEYWORD = 'refpnt'

    _ATTRS = {
        'point': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Arefpnt((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, point: types.Tuple[types.Real]):
        """
        Initializes ``Refpnt``.

        Parameters:
            point: Point anywhere on the quadrapole beam.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, point)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                point,
            ]
        )

        self.point: typing.Final[types.Tuple[types.Real]] = point


@dataclasses.dataclass
class RefpntBuilder:
    """
    Builds ``Refpnt``.

    Attributes:
        point: Point anywhere on the quadrapole beam.
    """

    point: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``RefpntBuilder`` into ``Refpnt``.

        Returns:
            ``Refpnt`` for ``RefpntBuilder``.
        """

        if self.point:
            point = []
            for item in self.point:
                if isinstance(item, types.Real):
                    point.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    point.append(types.Real(item))
                elif isinstance(item, str):
                    point.append(types.Real.from_mcnp(item))
            point = types.Tuple(point)
        else:
            point = None

        return Refpnt(
            point=point,
        )

    @staticmethod
    def unbuild(ast: Refpnt):
        """
        Unbuilds ``Refpnt`` into ``RefpntBuilder``

        Returns:
            ``RefpntBuilder`` for ``Refpnt``.
        """

        return Refpnt(
            point=copy.deepcopy(ast.point),
        )
