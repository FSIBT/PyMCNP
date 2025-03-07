import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Fill_2(CellOption_, keyword='fill'):
    """
    Represents INP fill_2 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'i': types.Index,
        'j': types.Index,
        'k': types.Index,
        'universes': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(
        rf'fill( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})(( {types.Integer._REGEX.pattern})+)'
    )

    def __init__(
        self, i: types.Index, j: types.Index, k: types.Index, universes: types.Tuple[types.Integer]
    ):
        """
        Initializes ``Fill_2``.

        Parameters:
            i: Lattice parameter #1.
            j: Lattice parameter #2.
            k: Lattice parameter #3.
            universes: Fill universe numbers.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if i is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i)
        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, j)
        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, k)
        if universes is None or not (
            len(universes) == (i.upper - i.lower) * (j.upper - j.lower) * (k.upper - k.lower)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, universes)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                i,
                j,
                k,
                universes,
            ]
        )

        self.i: typing.Final[types.Index] = i
        self.j: typing.Final[types.Index] = j
        self.k: typing.Final[types.Index] = k
        self.universes: typing.Final[types.Tuple[types.Integer]] = universes
