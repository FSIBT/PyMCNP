import re
import typing
import dataclasses


from . import _option
from .....utils import types


class Nocolor(_option.ContourOption):
    """
    Represents INP nocolor elements.

    Attributes:

    """

    _KEYWORD = 'nocolor'

    _ATTRS = {}

    _REGEX = re.compile(r'\Anocolor\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Nocolor``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class NocolorBuilder(_option.ContourOptionBuilder):
    """
    Builds ``Nocolor``.

    Attributes:

    """

    def build(self):
        """
        Builds ``NocolorBuilder`` into ``Nocolor``.

        Returns:
            ``Nocolor`` for ``NocolorBuilder``.
        """

        return Nocolor()

    @staticmethod
    def unbuild(ast: Nocolor):
        """
        Unbuilds ``Nocolor`` into ``NocolorBuilder``

        Returns:
            ``NocolorBuilder`` for ``Nocolor``.
        """

        return NocolorBuilder()
