import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Dm(DataOption):
    """
    Represents INP dm elements.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Adm((?: {types.Zaid._REGEX.pattern})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.Zaid]):
        """
        Initializes ``Dm``.

        Parameters:
            zaids: Tuple of ZAID aliases.

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

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class DmBuilder:
    """
    Builds ``Dm``.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    zaids: list[str] | list[types.Zaid]

    def build(self):
        """
        Builds ``DmBuilder`` into ``Dm``.

        Returns:
            ``Dm`` for ``DmBuilder``.
        """

        if self.zaids:
            zaids = []
            for item in self.zaids:
                if isinstance(item, types.Zaid):
                    zaids.append(item)
                elif isinstance(item, str):
                    zaids.append(types.Zaid.from_mcnp(item))
                else:
                    zaids.append(item.build())
            zaids = types.Tuple(zaids)
        else:
            zaids = None

        return Dm(
            zaids=zaids,
        )
