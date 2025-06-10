import re
import typing
import dataclasses


from . import _option
from ....utils import types


class Plot(_option.MplotOption):
    """
    Represents INP plot elements.

    Attributes:

    """

    _KEYWORD = 'plot'

    _ATTRS = {}

    _REGEX = re.compile(r'\Aplot\Z')

    def __init__(
        self,
    ):
        """
        Initializes ``Plot``.

        Parameters:


        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple([])


@dataclasses.dataclass
class PlotBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Plot``.

    Attributes:

    """

    def build(self):
        """
        Builds ``PlotBuilder`` into ``Plot``.

        Returns:
            ``Plot`` for ``PlotBuilder``.
        """

        return Plot()

    @staticmethod
    def unbuild(ast: Plot):
        """
        Unbuilds ``Plot`` into ``PlotBuilder``

        Returns:
            ``PlotBuilder`` for ``Plot``.
        """

        return PlotBuilder()
