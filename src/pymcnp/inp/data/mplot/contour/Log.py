import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Log(ContourOption):
    """
    Represents INP log elements.

    Attributes:

    """

    _KEYWORD = 'log'

    _ATTRS = {}

    _REGEX = re.compile(r'\Alog\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Log``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class LogBuilder:
    """
    Builds ``Log``.

    Attributes:

    """

    def build(self):
        """
        Builds ``LogBuilder`` into ``Log``.

        Returns:
            ``Log`` for ``LogBuilder``.
        """

        return Log()

    @staticmethod
    def unbuild(ast: Log):
        """
        Unbuilds ``Log`` into ``LogBuilder``

        Returns:
            ``LogBuilder`` for ``Log``.
        """

        return Log()
