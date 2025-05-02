import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Line(ContourOption):
    """
    Represents INP line elements.

    Attributes:

    """

    _ATTRS = {}

    _REGEX = re.compile(r'\Aline\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Line``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LineBuilder:
    """
    Builds ``Line``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LineBuilder`` into ``Line``.

        Returns:
            ``Line`` for ``LineBuilder``.
        """

        return Line()
