import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Coplot(_option.MplotOption):
    """
    Represents INP coplot elements.

    Attributes:

    """

    _KEYWORD = 'coplot'

    _ATTRS = {}

    _REGEX = re.compile(r'\Acoplot\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Coplot``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class CoplotBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Coplot``.

    Attributes:

    """

    def build(self):
        """
        Builds ``CoplotBuilder`` into ``Coplot``.

        Returns:
            ``Coplot`` for ``CoplotBuilder``.
        """

        return Coplot()

    @staticmethod
    def unbuild(ast: Coplot):
        """
        Unbuilds ``Coplot`` into ``CoplotBuilder``

        Returns:
            ``CoplotBuilder`` for ``Coplot``.
        """

        return CoplotBuilder()
