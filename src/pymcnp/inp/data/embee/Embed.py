import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Embed(_option.EmbeeOption):
    """
    Represents INP embed elements.

    Attributes:
        number: Embedded mesh universe number.
    """

    _KEYWORD = 'embed'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Aembed( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Embed``.

        Parameters:
            number: Embedded mesh universe number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (0 <= number.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class EmbedBuilder(_option.EmbeeOptionBuilder):
    """
    Builds ``Embed``.

    Attributes:
        number: Embedded mesh universe number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``EmbedBuilder`` into ``Embed``.

        Returns:
            ``Embed`` for ``EmbedBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Embed(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Embed):
        """
        Unbuilds ``Embed`` into ``EmbedBuilder``

        Returns:
            ``EmbedBuilder`` for ``Embed``.
        """

        return EmbedBuilder(
            number=copy.deepcopy(ast.number),
        )
