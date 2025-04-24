import re
import typing
import dataclasses


from ._option import ContourOption
from .....utils import types


class Nocolor(ContourOption, keyword='nocolor'):
    """
    Represents INP nocolor elements.

    Attributes:

    """

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
class NocolorBuilder:
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
