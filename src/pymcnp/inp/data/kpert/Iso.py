import re
import typing
import dataclasses


from ._option import KpertOption
from ....utils import types
from ....utils import errors


class Iso(KpertOption):
    """
    Represents INP iso elements.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.RealOrJump]):
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

        self.zaids: typing.Final[types.Tuple[types.RealOrJump]] = zaids


@dataclasses.dataclass
class IsoBuilder:
    """
    Builds ``Iso``.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    zaids: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``IsoBuilder`` into ``Iso``.

        Returns:
            ``Iso`` for ``IsoBuilder``.
        """

        if self.zaids:
            zaids = []
            for item in self.zaids:
                if isinstance(item, types.RealOrJump):
                    zaids.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    zaids.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    zaids.append(types.RealOrJump.from_mcnp(item))
            zaids = types.Tuple(zaids)
        else:
            zaids = None

        return Iso(
            zaids=zaids,
        )
