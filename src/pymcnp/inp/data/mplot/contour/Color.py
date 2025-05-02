import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Color(ContourOption):
    """
    Represents INP color elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Acolor\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Color``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class ColorBuilder:
    """
    Builds ``Color``.

    Attributes:

    """

    def build(self):
        """
        Builds ``ColorBuilder`` into ``Color``.

        Returns:
            ``Color`` for ``ColorBuilder``.
        """

        return Color()
