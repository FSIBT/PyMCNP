import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Printal(_option.MplotOption):
    """
    Represents INP printal elements.

    Attributes:

    """

    _KEYWORD = 'printal'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aprintal\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Printal``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PrintalBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Printal``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PrintalBuilder`` into ``Printal``.

        Returns:
            ``Printal`` for ``PrintalBuilder``.
        """

        return Printal()

    @staticmethod
    def unbuild(ast: Printal):
        """
        Unbuilds ``Printal`` into ``PrintalBuilder``

        Returns:
            ``PrintalBuilder`` for ``Printal``.
        """

        return PrintalBuilder()
