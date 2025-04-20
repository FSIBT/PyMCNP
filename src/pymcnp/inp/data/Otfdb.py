import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Otfdb(DataOption_, keyword='otfdb'):
    """
    Represents INP otfdb elements.

    Attributes:
        zaids: Identifiers for the broadening tables.
    """

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Aotfdb((?: {types.Zaid._REGEX.pattern})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.Zaid]):
        """
        Initializes ``Otfdb``.

        Parameters:
            zaids: Identifiers for the broadening tables.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class OtfdbBuilder:
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

        zaids = []
        for item in self.zaids:
            if isinstance(item, types.Zaid):
                zaids.append(item)
            elif isinstance(item, str):
                zaids.append(types.Zaid.from_mcnp(item))
            else:
                zaids.append(item.build())
        zaids = types.Tuple(zaids)

        return Otfdb(
            zaids=zaids,
        )
