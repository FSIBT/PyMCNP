import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Otfdb(_option.DataOption):
    """
    Represents INP otfdb elements.

    Attributes:
        zaids: Identifiers for the broadening tables.
    """

    _KEYWORD = 'otfdb'

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Aotfdb((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.Zaid]):
        """
        Initializes ``Otfdb``.

        Parameters:
            zaids: Identifiers for the broadening tables.

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
class OtfdbBuilder(_option.DataOptionBuilder):
    """
    Builds ``Otfdb``.

    Attributes:
        zaids: Identifiers for the broadening tables.
    """

    zaids: list[str] | list[types.Zaid]

    def build(self):
        """
        Builds ``OtfdbBuilder`` into ``Otfdb``.

        Returns:
            ``Otfdb`` for ``OtfdbBuilder``.
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

        return Otfdb(
            zaids=zaids,
        )

    @staticmethod
    def unbuild(ast: Otfdb):
        """
        Unbuilds ``Otfdb`` into ``OtfdbBuilder``

        Returns:
            ``OtfdbBuilder`` for ``Otfdb``.
        """

        return OtfdbBuilder(
            zaids=copy.deepcopy(ast.zaids),
        )
