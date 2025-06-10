import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Options(_option.MplotOption):
    """
    Represents INP options elements.

    Attributes:

    """

    _KEYWORD = 'options'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aoptions\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Options``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class OptionsBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Options``.

    Attributes:

    """

    def build(self):
        """
        Builds ``OptionsBuilder`` into ``Options``.

        Returns:
            ``Options`` for ``OptionsBuilder``.
        """

        return Options()

    @staticmethod
    def unbuild(ast: Options):
        """
        Unbuilds ``Options`` into ``OptionsBuilder``

        Returns:
            ``OptionsBuilder`` for ``Options``.
        """

        return OptionsBuilder()
