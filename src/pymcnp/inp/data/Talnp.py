import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Talnp(DataOption, keyword='talnp'):
    """
    Represents INP talnp elements.

    Attributes:
        tallies: Tallies to exclude from output.
    """

    _ATTRS = {
        'tallies': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Atalnp((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z')

    def __init__(self, tallies: types.Tuple[types.IntegerOrJump] = None):
        """
        Initializes ``Talnp``.

        Parameters:
            tallies: Tallies to exclude from output.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tallies is not None and not (
            filter(lambda entry: not (1 <= entry <= 99_999_999), tallies)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tallies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tallies,
            ]
        )

        self.tallies: typing.Final[types.Tuple[types.IntegerOrJump]] = tallies


@dataclasses.dataclass
class TalnpBuilder:
    """
    Builds ``Talnp``.

    Attributes:
        tallies: Tallies to exclude from output.
    """

    tallies: list[str] | list[int] | list[types.IntegerOrJump] = None

    def build(self):
        """
        Builds ``TalnpBuilder`` into ``Talnp``.

        Returns:
            ``Talnp`` for ``TalnpBuilder``.
        """

        tallies = []
        for item in self.tallies:
            if isinstance(item, types.IntegerOrJump):
                tallies.append(item)
            elif isinstance(item, int):
                tallies.append(types.IntegerOrJump(item))
            elif isinstance(item, str):
                tallies.append(types.IntegerOrJump.from_mcnp(item))
        tallies = types.Tuple(tallies)

        return Talnp(
            tallies=tallies,
        )
