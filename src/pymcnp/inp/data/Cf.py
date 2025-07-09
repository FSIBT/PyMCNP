import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Cf(_option.DataOption):
    """
    Represents INP cf elements.

    Attributes:
        suffix: Data card option suffix.
        numbers: Tallies for problem cell numbers to flag.
    """

    _KEYWORD = 'cf'

    _ATTRS = {
        'suffix': types.Integer,
        'numbers': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Acf(\d+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, numbers: types.Tuple[types.Integer]):
        """
        Initializes ``Cf``.

        Parameters:
            suffix: Data card option suffix.
            numbers: Tallies for problem cell numbers to flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if numbers is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, numbers)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                numbers,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.numbers: typing.Final[types.Tuple[types.Integer]] = numbers


@dataclasses.dataclass
class CfBuilder(_option.DataOptionBuilder):
    """
    Builds ``Cf``.

    Attributes:
        suffix: Data card option suffix.
        numbers: Tallies for problem cell numbers to flag.
    """

    suffix: str | int | types.Integer
    numbers: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``CfBuilder`` into ``Cf``.

        Returns:
            ``Cf`` for ``CfBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

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

        return Cf(
            suffix=suffix,
            numbers=numbers,
        )

    @staticmethod
    def unbuild(ast: Cf):
        """
        Unbuilds ``Cf`` into ``CfBuilder``

        Returns:
            ``CfBuilder`` for ``Cf``.
        """

        return CfBuilder(
            suffix=copy.deepcopy(ast.suffix),
            numbers=copy.deepcopy(ast.numbers),
        )
