import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Printpts(_option.MplotOption):
    """
    Represents INP printpts elements.

    Attributes:

    """

    _KEYWORD = 'printpts'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aprintpts\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Printpts``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PrintptsBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Printpts``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PrintptsBuilder`` into ``Printpts``.

        Returns:
            ``Printpts`` for ``PrintptsBuilder``.
        """

        return Printpts()

    @staticmethod
    def unbuild(ast: Printpts):
        """
        Unbuilds ``Printpts`` into ``PrintptsBuilder``

        Returns:
            ``PrintptsBuilder`` for ``Printpts``.
        """

        return PrintptsBuilder()
