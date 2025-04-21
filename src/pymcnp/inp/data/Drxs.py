import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


class Drxs(DataOption, keyword='drxs'):
    """
    Represents INP drxs elements.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Adrxs((?: {types.Zaid._REGEX.pattern})+?)?\Z')

    def __init__(self, zaids: types.Tuple[types.Zaid] = None):
        """
        Initializes ``Drxs``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class DrxsBuilder:
    """
    Builds ``Drxs``.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    zaids: list[str] | list[types.Zaid] = None

    def build(self):
        """
        Builds ``DrxsBuilder`` into ``Drxs``.

        Returns:
            ``Drxs`` for ``DrxsBuilder``.
        """

        zaids = []
        for item in self.zaids:
            if isinstance(item, types.Zaid):
                zaids.append(item)
            elif isinstance(item, str):
                zaids.append(types.Zaid.from_mcnp(item))
            else:
                zaids.append(item.build())
        zaids = types.Tuple(zaids)

        return Drxs(
            zaids=zaids,
        )
