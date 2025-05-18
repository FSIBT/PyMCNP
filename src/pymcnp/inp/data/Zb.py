import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


class Zb(DataOption):
    """
    Represents INP zb elements.

    Attributes:
        anything: Any parameters.
    """

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azb( {types.String._REGEX.pattern})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zb``.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                anything,
            ]
        )

        self.anything: typing.Final[types.String] = anything


@dataclasses.dataclass
class ZbBuilder:
    """
    Builds ``Zb``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZbBuilder`` into ``Zb``.

        Returns:
            ``Zb`` for ``ZbBuilder``.
        """

        anything = self.anything
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Zb(
            anything=anything,
        )
