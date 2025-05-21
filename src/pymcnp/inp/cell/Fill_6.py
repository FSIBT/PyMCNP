import re
import copy
import typing
import dataclasses


from ._option import CellOption
from ...utils import types
from ...utils import errors


class Fill_6(CellOption):
    """
    Represents INP fill variation #6 elements.

    Attributes:
        i: Lattice parameter #1.
        j: Lattice parameter #2.
        k: Lattice parameter #3.
        universes: Fill universe numbers.
        m: Displacement vector origin.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'i': types.Index,
        'j': types.Index,
        'k': types.Index,
        'universes': types.Tuple[types.Integer],
        'm': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Afill( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})( {types.Index._REGEX.pattern})((?: {types.Integer._REGEX.pattern})+?)( {types.Integer._REGEX.pattern}| [(]{types.Integer._REGEX.pattern}[)])?\Z'
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
            InpError: SEMANTICS_OPTION.
        """

        if i is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i)
        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j)
        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, k)
        if universes is None or not (
            len(universes)
            == (i.upper.value - i.lower.value)
            * (j.upper.value - j.lower.value)
            * (k.upper.value - k.lower.value)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universes)

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

        i = self.i
        if isinstance(self.i, types.Index):
            i = self.i
        elif isinstance(self.i, str):
            i = types.Index.from_mcnp(self.i)

        j = self.j
        if isinstance(self.j, types.Index):
            j = self.j
        elif isinstance(self.j, str):
            j = types.Index.from_mcnp(self.j)

        k = self.k
        if isinstance(self.k, types.Index):
            k = self.k
        elif isinstance(self.k, str):
            k = types.Index.from_mcnp(self.k)

        if self.universes:
            universes = []
            for item in self.universes:
                if isinstance(item, types.Integer):
                    universes.append(item)
                elif isinstance(item, int):
                    universes.append(types.Integer(item))
                elif isinstance(item, str):
                    universes.append(types.Integer.from_mcnp(item))
            universes = types.Tuple(universes)
        else:
            universes = None

        m = self.m
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

    @staticmethod
    def unbuild(ast: Fill_6):
        """
        Unbuilds ``Fill_6`` into ``FillBuilder_6``

        Returns:
            ``FillBuilder_6`` for ``Fill_6``.
        """

        return Fill_6(
            i=copy.deepcopy(ast.i),
            j=copy.deepcopy(ast.j),
            k=copy.deepcopy(ast.k),
            universes=copy.deepcopy(ast.universes),
            m=copy.deepcopy(ast.m),
        )
