import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


class Zc(DataOption, keyword='zc'):
    """
    Represents INP zc elements.

    Attributes:
        anything: Any parameters.
    """

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azc( {types.String._REGEX.pattern})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zc``.

        Parameters:
            anything: Any parameters.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                anything,
            ]
        )

        self.anything: typing.Final[types.String] = anything


@dataclasses.dataclass
class ZcBuilder:
    """
    Builds ``Zc``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZcBuilder`` into ``Zc``.

        Returns:
            ``Zc`` for ``ZcBuilder``.
        """

        anything = None
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Zc(
            anything=anything,
        )
