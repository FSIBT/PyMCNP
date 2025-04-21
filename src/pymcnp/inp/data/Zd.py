import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types


class Zd(DataOption, keyword='zd'):
    """
    Represents INP zd elements.

    Attributes:
        anything: Any parameters.
    """

    _ATTRS = {
        'anything': types.String,
    }

    _REGEX = re.compile(rf'\Azd( {types.String._REGEX.pattern})?\Z')

    def __init__(self, anything: types.String = None):
        """
        Initializes ``Zd``.

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
class ZdBuilder:
    """
    Builds ``Zd``.

    Attributes:
        anything: Any parameters.
    """

    anything: str | types.String = None

    def build(self):
        """
        Builds ``ZdBuilder`` into ``Zd``.

        Returns:
            ``Zd`` for ``ZdBuilder``.
        """

        anything = None
        if isinstance(self.anything, types.String):
            anything = self.anything
        elif isinstance(self.anything, str):
            anything = types.String.from_mcnp(self.anything)

        return Zd(
            anything=anything,
        )
