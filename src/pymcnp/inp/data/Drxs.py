import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Drxs(_option.DataOption):
    """
    Represents INP drxs elements.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    _KEYWORD = 'drxs'

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Adrxs((?: {types.Zaid._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, zaids: types.Tuple[types.Zaid] = None):
        """
        Initializes ``Drxs``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class DrxsBuilder(_option.DataOptionBuilder):
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

        if self.zaids:
            zaids = []
            for item in self.zaids:
                if isinstance(item, types.Zaid):
                    zaids.append(item)
                elif isinstance(item, str):
                    zaids.append(types.Zaid.from_mcnp(item))
            zaids = types.Tuple(zaids)
        else:
            zaids = None

        return Drxs(
            zaids=zaids,
        )

    @staticmethod
    def unbuild(ast: Drxs):
        """
        Unbuilds ``Drxs`` into ``DrxsBuilder``

        Returns:
            ``DrxsBuilder`` for ``Drxs``.
        """

        return DrxsBuilder(
            zaids=copy.deepcopy(ast.zaids),
        )
