import re
import copy
import typing
import dataclasses


from ._option import EmbeeOption
from ....utils import types
from ....utils import errors


class Mat(EmbeeOption):
    """
    Represents INP mat elements.

    Attributes:
        number: Material number.
    """

    _KEYWORD = 'mat'

    _ATTRS = {
        'number': types.Integer,
    }

    _REGEX = re.compile(rf'\Amat( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``Mat``.

        Parameters:
            number: Material number.

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
class MatBuilder:
    """
    Builds ``Mat``.

    Attributes:
        number: Material number.
    """

    number: str | int | types.Integer

    def build(self):
        """
        Builds ``MatBuilder`` into ``Mat``.

        Returns:
            ``Mat`` for ``MatBuilder``.
        """

        number = self.number
        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        return Mat(
            number=number,
        )

    @staticmethod
    def unbuild(ast: Mat):
        """
        Unbuilds ``Mat`` into ``MatBuilder``

        Returns:
            ``MatBuilder`` for ``Mat``.
        """

        return Mat(
            number=copy.deepcopy(ast.number),
        )
