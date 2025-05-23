import re
import copy
import typing
import dataclasses


from ._option import KsenOption
from ....utils import types
from ....utils import errors


class Iso(KsenOption):
    """
    Represents INP iso elements.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    _KEYWORD = 'iso'

    _ATTRS = {
        'zaids': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.Real]):
        """
        Initializes ``Iso``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Real]] = zaids


@dataclasses.dataclass
class IsoBuilder:
    """
    Builds ``Iso``.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    zaids: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``IsoBuilder`` into ``Iso``.

        Returns:
            ``Iso`` for ``IsoBuilder``.
        """

        if self.zaids:
            zaids = []
            for item in self.zaids:
                if isinstance(item, types.Real):
                    zaids.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    zaids.append(types.Real(item))
                elif isinstance(item, str):
                    zaids.append(types.Real.from_mcnp(item))
            zaids = types.Tuple(zaids)
        else:
            zaids = None

        return Iso(
            zaids=zaids,
        )

    @staticmethod
    def unbuild(ast: Iso):
        """
        Unbuilds ``Iso`` into ``IsoBuilder``

        Returns:
            ``IsoBuilder`` for ``Iso``.
        """

        return Iso(
            zaids=copy.deepcopy(ast.zaids),
        )
