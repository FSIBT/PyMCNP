import re
import copy
import typing
import dataclasses


from ._option import KpertOption
from ....utils import types
from ....utils import errors


class Rxn(KpertOption):
    """
    Represents INP rxn elements.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    _KEYWORD = 'rxn'

    _ATTRS = {
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Arxn((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Rxn``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class RxnBuilder:
    """
    Builds ``Rxn``.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``RxnBuilder`` into ``Rxn``.

        Returns:
            ``Rxn`` for ``RxnBuilder``.
        """

        if self.numbers:
            numbers = []
            for item in self.numbers:
                if isinstance(item, types.Integer):
                    numbers.append(item)
                elif isinstance(item, int):
                    numbers.append(types.Integer(item))
                elif isinstance(item, str):
                    numbers.append(types.Integer.from_mcnp(item))
            numbers = types.Tuple(numbers)
        else:
            numbers = None

        return Rxn(
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Rxn):
        """
        Unbuilds ``Rxn`` into ``RxnBuilder``

        Returns:
            ``RxnBuilder`` for ``Rxn``.
        """

        return Rxn(
            numbers=copy.deepcopy(ast.numbers),
        )
