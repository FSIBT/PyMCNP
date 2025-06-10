import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Rxn(_option.PertOption):
    """
    Represents INP rxn elements.

    Attributes:
        numbers: ENDF/B reaction number.
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
            numbers: ENDF/B reaction number.

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
class RxnBuilder(_option.PertOptionBuilder):
    """
    Builds ``Rxn``.

    Attributes:
        numbers: ENDF/B reaction number.
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

        return RxnBuilder(
            numbers=copy.deepcopy(ast.numbers),
        )
