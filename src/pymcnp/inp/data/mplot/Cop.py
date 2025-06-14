import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Cop(_option.MplotOption):
    """
    Represents INP cop elements.

    Attributes:

    """

    _KEYWORD = 'cop'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acop\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Cop``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class CopBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Cop``.

    Attributes:

    """

    def build(self):
        """
        Builds ``CopBuilder`` into ``Cop``.

        Returns:
            ``Cop`` for ``CopBuilder``.
        """

        return Cop()

    @staticmethod
    def unbuild(ast: Cop):
        """
        Unbuilds ``Cop`` into ``CopBuilder``

        Returns:
            ``CopBuilder`` for ``Cop``.
        """

        return CopBuilder()
