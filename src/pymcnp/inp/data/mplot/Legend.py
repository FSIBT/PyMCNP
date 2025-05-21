import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types


class Legend(MplotOption):
    """
    Represents INP legend elements.

    Attributes:
        x: Label x-location.
        y: Label x-location.
    """

    _KEYWORD = 'legend'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
    }

    _REGEX = re.compile(
        rf'\Alegend( {types.Real._REGEX.pattern})?( {types.Real._REGEX.pattern})?\Z'
    )

    def __init__(self, x: types.Real = None, y: types.Real = None):
        """
        Initializes ``Legend``.

        Parameters:
            x: Label x-location.
            y: Label x-location.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y


@dataclasses.dataclass
class LegendBuilder:
    """
    Builds ``Legend``.

    Attributes:
        x: Label x-location.
        y: Label x-location.
    """

    x: str | float | types.Real = None
    y: str | float | types.Real = None

    def build(self):
        """
        Builds ``LegendBuilder`` into ``Legend``.

        Returns:
            ``Legend`` for ``LegendBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        return Legend(
            x=x,
            y=y,
        )

    @staticmethod
    def unbuild(ast: Legend):
        """
        Unbuilds ``Legend`` into ``LegendBuilder``

        Returns:
            ``LegendBuilder`` for ``Legend``.
        """

        return Legend(
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
        )
