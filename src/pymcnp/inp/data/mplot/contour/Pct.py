import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Pct(ContourOption):
    """
    Represents INP pct elements.

    Attributes:

    """

    _KEYWORD = 'pct'

    _ATTRS = {}

    _REGEX = re.compile(r'\Apct\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Pct``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PctBuilder:
    """
    Builds ``Pct``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PctBuilder`` into ``Pct``.

        Returns:
            ``Pct`` for ``PctBuilder``.
        """

        return Pct()

    @staticmethod
    def unbuild(ast: Pct):
        """
        Unbuilds ``Pct`` into ``PctBuilder``

        Returns:
            ``PctBuilder`` for ``Pct``.
        """

        return Pct()
