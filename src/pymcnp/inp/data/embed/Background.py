import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Background(_option.EmbedOption):
    """
    Represents INP background elements.

    Attributes:
        number: Background pseudo-cell number.
    """

    _KEYWORD = 'background'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Abackground( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Background``.

        Parameters:
            number: Background pseudo-cell number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (number >= 1 and number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class BackgroundBuilder(_option.EmbedOptionBuilder):
    """
    Builds ``Background``.

    Attributes:
        number: Background pseudo-cell number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``BackgroundBuilder`` into ``Background``.

        Returns:
            ``Background`` for ``BackgroundBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Background(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Background):
        """
        Unbuilds ``Background`` into ``BackgroundBuilder``

        Returns:
            ``BackgroundBuilder`` for ``Background``.
        """

        return BackgroundBuilder(
            number=copy.deepcopy(ast.number),
        )
