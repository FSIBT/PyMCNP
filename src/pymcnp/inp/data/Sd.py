import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Sd(DataOption):
    """
    Represents INP sd elements.

    Attributes:
        information: Area, volume, or mass by segmented, surface/cell.
    """

    _KEYWORD = 'sd'

    _ATTRS = {
        'information': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Asd((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, information: types.Tuple[types.Real]):
        """
        Initializes ``Sd``.

        Parameters:
            information: Area, volume, or mass by segmented, surface/cell.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if information is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, information)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                information,
            ]
        )

        self.information: typing.Final[types.Tuple[types.Real]] = information


@dataclasses.dataclass
class SdBuilder:
    """
    Builds ``Sd``.

    Attributes:
        information: Area, volume, or mass by segmented, surface/cell.
    """

    information: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``SdBuilder`` into ``Sd``.

        Returns:
            ``Sd`` for ``SdBuilder``.
        """

        if self.information:
            information = []
            for item in self.information:
                if isinstance(item, types.Real):
                    information.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    information.append(types.Real(item))
                elif isinstance(item, str):
                    information.append(types.Real.from_mcnp(item))
            information = types.Tuple(information)
        else:
            information = None

        return Sd(
            information=information,
        )

    @staticmethod
    def unbuild(ast: Sd):
        """
        Unbuilds ``Sd`` into ``SdBuilder``

        Returns:
            ``SdBuilder`` for ``Sd``.
        """

        return Sd(
            information=copy.deepcopy(ast.information),
        )
