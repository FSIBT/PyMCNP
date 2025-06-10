import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Loglin(_option.MplotOption):
    """
    Represents INP loglin elements.

    Attributes:

    """

    _KEYWORD = 'loglin'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglin\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Loglin``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LoglinBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Loglin``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LoglinBuilder`` into ``Loglin``.

        Returns:
            ``Loglin`` for ``LoglinBuilder``.
        """

        return Loglin()

    @staticmethod
    def unbuild(ast: Loglin):
        """
        Unbuilds ``Loglin`` into ``LoglinBuilder``

        Returns:
            ``LoglinBuilder`` for ``Loglin``.
        """

        return LoglinBuilder()
