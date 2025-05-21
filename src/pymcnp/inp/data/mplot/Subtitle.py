import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Subtitle(MplotOption):
    """
    Represents INP subtitle elements.

    Attributes:
        x: x-coordinate of location.
        y: y-coordinate of location.
        aa: Line to substitute.
    """

    _KEYWORD = 'subtitle'

    _ATTRS = {
        'x': types.Integer,
        'y': types.Integer,
        'aa': types.String,
    }

    _REGEX = re.compile(
        rf'\Asubtitle( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( \"{types.String._REGEX.pattern}\")\Z'
    )

    def __init__(self, x: types.Integer, y: types.Integer, aa: types.String):
        """
        Initializes ``Subtitle``.

        Parameters:
            x: x-coordinate of location.
            y: y-coordinate of location.
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                aa,
            ]
        )

        self.x: typing.Final[types.Integer] = x
        self.y: typing.Final[types.Integer] = y
        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class SubtitleBuilder:
    """
    Builds ``Subtitle``.

    Attributes:
        x: x-coordinate of location.
        y: y-coordinate of location.
        aa: Line to substitute.
    """

    x: str | int | types.Integer
    y: str | int | types.Integer
    aa: str | types.String

    def build(self):
        """
        Builds ``SubtitleBuilder`` into ``Subtitle``.

        Returns:
            ``Subtitle`` for ``SubtitleBuilder``.
        """

        x = self.x
        if isinstance(self.x, types.Integer):
            x = self.x
        elif isinstance(self.x, int):
            x = types.Integer(self.x)
        elif isinstance(self.x, str):
            x = types.Integer.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Integer):
            y = self.y
        elif isinstance(self.y, int):
            y = types.Integer(self.y)
        elif isinstance(self.y, str):
            y = types.Integer.from_mcnp(self.y)

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Subtitle(
            x=x,
            y=y,
            aa=aa,
        )

    @staticmethod
    def unbuild(ast: Subtitle):
        """
        Unbuilds ``Subtitle`` into ``SubtitleBuilder``

        Returns:
            ``SubtitleBuilder`` for ``Subtitle``.
        """

        return Subtitle(
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            aa=copy.deepcopy(ast.aa),
        )
