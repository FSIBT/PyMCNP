import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Sur(_option.SdefOption):
    """
    Represents INP sur elements.

    Attributes:
        number: Surface number.
    """

    _KEYWORD = 'sur'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Asur( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Sur``.

        Parameters:
            number: Surface number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if number is None or not (isinstance(number.value, types.Jump) or 0 <= number.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, number)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                number,
            ]
        )

        self.number: typing.Final[types.Integer] = number


@dataclasses.dataclass
class SurBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Sur``.

    Attributes:
        number: Surface number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``SurBuilder`` into ``Sur``.

        Returns:
            ``Sur`` for ``SurBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Sur(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Sur):
        """
        Unbuilds ``Sur`` into ``SurBuilder``

        Returns:
            ``SurBuilder`` for ``Sur``.
        """

        return SurBuilder(
            number=copy.deepcopy(ast.number),
        )
