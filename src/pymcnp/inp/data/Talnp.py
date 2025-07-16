import re

from . import _option
from ... import types


class Talnp(_option.DataOption):
    """
    Represents INP talnp elements.
    """

    _KEYWORD = 'talnp'

    _ATTRS = {
        'tallies': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Atalnp((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, tallies: list[str] | list[int] | list[types.Integer] = None):
        """
        Initializes ``Talnp``.

        Parameters:
            tallies: Tallies to exclude from output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.tallies: types.Tuple[types.Integer] = tallies

    @property
    def tallies(self) -> types.Tuple[types.Integer]:
        """
        Tallies to exclude from output

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._tallies

    @tallies.setter
    def tallies(self, tallies: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``tallies``.

        Parameters:
            tallies: Tallies to exclude from output.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if tallies is not None:
            array = []
            for item in tallies:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            tallies = types.Tuple(array)

        self._tallies: types.Tuple[types.Integer] = tallies
