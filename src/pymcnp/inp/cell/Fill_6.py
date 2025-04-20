import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Fill_6(CellOption_, keyword='fill'):
    """
    Represents INP fill variation #6 elements.

    Attributes:
        i: Lattice parameter #1.
        j: Lattice parameter #2.
        k: Lattice parameter #3.
        universes: Fill universe numbers.
        m: Displacement vector origin.
    """

    _ATTRS = {
        'i': types.Index,
        'j': types.Index,
        'k': types.Index,
        'universes': types.Tuple[types.Integer],
        'm': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})((?: {types.Integer._REGEX.pattern})+?)( [(]{types.Integer._REGEX.pattern}[)])?\Z'
    )

    def __init__(
        self,
        i: types.Index,
        j: types.Index,
        k: types.Index,
        universes: types.Tuple[types.Integer],
        m: types.Integer = None,
    ):
        """
        Initializes ``Fill_6``.

        Parameters:
            i: Lattice parameter #1.
            j: Lattice parameter #2.
            k: Lattice parameter #3.
            universes: Fill universe numbers.
            m: Displacement vector origin.

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
                m,
            ]
        )

        self.i: typing.Final[types.Index] = i
        self.j: typing.Final[types.Index] = j
        self.k: typing.Final[types.Index] = k
        self.universes: typing.Final[types.Tuple[types.Integer]] = universes
        self.m: typing.Final[types.Integer] = m


@dataclasses.dataclass
class FillBuilder_6:
    """
    Builds ``Fill_6``.

    Attributes:
        i: Lattice parameter #1.
        j: Lattice parameter #2.
        k: Lattice parameter #3.
        universes: Fill universe numbers.
        m: Displacement vector origin.
    """

    i: str | types.Index
    j: str | types.Index
    k: str | types.Index
    universes: list[str] | list[int] | list[types.Integer]
    m: str | int | types.Integer = None

    def build(self):
        """
        Builds ``FillBuilder_6`` into ``Fill_6``.

        Returns:
            ``Fill_6`` for ``FillBuilder_6``.
        """

        if isinstance(self.i, types.Index):
            i = self.i
        elif isinstance(self.i, str):
            i = types.Index.from_mcnp(self.i)

        if isinstance(self.j, types.Index):
            j = self.j
        elif isinstance(self.j, str):
            j = types.Index.from_mcnp(self.j)

        if isinstance(self.k, types.Index):
            k = self.k
        elif isinstance(self.k, str):
            k = types.Index.from_mcnp(self.k)

        universes = []
        for item in self.universes:
            if isinstance(item, types.Integer):
                universes.append(item)
            elif isinstance(item, int):
                universes.append(types.Integer(item))
            elif isinstance(item, str):
                universes.append(types.Integer.from_mcnp(item))
        universes = types.Tuple(universes)

        m = None
        if isinstance(self.m, types.Integer):
            m = self.m
        elif isinstance(self.m, int):
            m = types.Integer(self.m)
        elif isinstance(self.m, str):
            m = types.Integer.from_mcnp(self.m)

        return Fill_6(
            i=i,
            j=j,
            k=k,
            universes=universes,
            m=m,
        )
