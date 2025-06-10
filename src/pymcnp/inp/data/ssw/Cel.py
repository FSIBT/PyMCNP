import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Cel(_option.SswOption):
    """
    Represents INP cel elements.

    Attributes:
        cfs: Cells from which KCODE neutrons are written.
    """

    _KEYWORD = 'cel'

    _ATTRS = {
        'cfs': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Acel((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, cfs: types.Tuple[types.Integer]):
        """
        Initializes ``Cel``.

        Parameters:
            cfs: Cells from which KCODE neutrons are written.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if cfs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cfs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                cfs,
            ]
        )

        self.cfs: typing.Final[types.Tuple[types.Integer]] = cfs


@dataclasses.dataclass
class CelBuilder(_option.SswOptionBuilder):
    """
    Builds ``Cel``.

    Attributes:
        cfs: Cells from which KCODE neutrons are written.
    """

    cfs: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``CelBuilder`` into ``Cel``.

        Returns:
            ``Cel`` for ``CelBuilder``.
        """

        if self.cfs:
            cfs = []
            for item in self.cfs:
                if isinstance(item, types.Integer):
                    cfs.append(item)
                elif isinstance(item, int):
                    cfs.append(types.Integer(item))
                elif isinstance(item, str):
                    cfs.append(types.Integer.from_mcnp(item))
            cfs = types.Tuple(cfs)
        else:
            cfs = None

        return Cel(
            cfs=cfs,
        )

    @staticmethod
    def unbuild(ast: Cel):
        """
        Unbuilds ``Cel`` into ``CelBuilder``

        Returns:
            ``CelBuilder`` for ``Cel``.
        """

        return CelBuilder(
            cfs=copy.deepcopy(ast.cfs),
        )
