import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Loglog(_option.MplotOption):
    """
    Represents INP loglog elements.

    Attributes:

    """

    _KEYWORD = 'loglog'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aloglog\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Loglog``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LoglogBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Loglog``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LoglogBuilder`` into ``Loglog``.

        Returns:
            ``Loglog`` for ``LoglogBuilder``.
        """

        return Loglog()

    @staticmethod
    def unbuild(ast: Loglog):
        """
        Unbuilds ``Loglog`` into ``LoglogBuilder``

        Returns:
            ``LoglogBuilder`` for ``Loglog``.
        """

        return LoglogBuilder()
