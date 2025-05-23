import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Talnp(DataOption):
    """
    Represents INP talnp elements.

    Attributes:
        tallies: Tallies to exclude from output.
    """

    _KEYWORD = 'talnp'

    _ATTRS = {
        'tallies': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Atalnp((?: {types.Integer._REGEX.pattern})+?)?\Z')

    def __init__(self, tallies: types.Tuple[types.Integer] = None):
        """
        Initializes ``Talnp``.

        Parameters:
            tallies: Tallies to exclude from output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if tallies is not None and not (
            filter(lambda entry: not (1 <= entry.value <= 99_999_999), tallies)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tallies)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tallies,
            ]
        )

        self.tallies: typing.Final[types.Tuple[types.Integer]] = tallies


@dataclasses.dataclass
class TalnpBuilder:
    """
    Builds ``Talnp``.

    Attributes:
        tallies: Tallies to exclude from output.
    """

    tallies: list[str] | list[int] | list[types.Integer] = None

    def build(self):
        """
        Builds ``TalnpBuilder`` into ``Talnp``.

        Returns:
            ``Talnp`` for ``TalnpBuilder``.
        """

        if self.tallies:
            tallies = []
            for item in self.tallies:
                if isinstance(item, types.Integer):
                    tallies.append(item)
                elif isinstance(item, int):
                    tallies.append(types.Integer(item))
                elif isinstance(item, str):
                    tallies.append(types.Integer.from_mcnp(item))
            tallies = types.Tuple(tallies)
        else:
            tallies = None

        return Talnp(
            tallies=tallies,
        )

    @staticmethod
    def unbuild(ast: Talnp):
        """
        Unbuilds ``Talnp`` into ``TalnpBuilder``

        Returns:
            ``TalnpBuilder`` for ``Talnp``.
        """

        return Talnp(
            tallies=copy.deepcopy(ast.tallies),
        )
