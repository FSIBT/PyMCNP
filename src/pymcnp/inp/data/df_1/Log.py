import re
import typing
import dataclasses


from ._option import Df_1Option
from ....utils import types


class Log(Df_1Option, keyword='log'):
    """
    Represents INP log elements.

    Attributes:

    """

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
