import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fill_0(_option.LikeOption):
    """
    Represents INP fill variation #0 elements.

    Attributes:
        prefix: Star prefix.
        i: Lattice parameter #1.
        j: Lattice parameter #2.
        k: Lattice parameter #3.
        universes: Fill universe numbers.
        m: Displacement vector origin.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'i': types.Index,
        'j': types.Index,
        'k': types.Index,
        'universes': types.Tuple[types.Integer],
        'm': types.Integer,
    }

    _REGEX = re.compile(rf'\A([*])?fill (\S+:\S+) (\S+:\S+) (\S+:\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)(?: [(]({types.Integer._REGEX.pattern[2:-2]})[)])?\Z')

    def __init__(self, i: types.Index, j: types.Index, k: types.Index, universes: types.Tuple[types.Integer], prefix: types.String = None, m: types.Integer = None):
        """
        Initializes ``Fill_0``.

        Parameters:
            prefix: Star prefix.
            i: Lattice parameter #1.
            j: Lattice parameter #2.
            k: Lattice parameter #3.
            universes: Fill universe numbers.
            m: Displacement vector origin.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if i is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i)
        if j is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, j)
        if k is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, k)
        if universes is None:
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

        self.prefix: typing.Final[types.String] = prefix
        self.i: typing.Final[types.Index] = i
        self.j: typing.Final[types.Index] = j
        self.k: typing.Final[types.Index] = k
        self.universes: typing.Final[types.Tuple[types.Integer]] = universes
        self.m: typing.Final[types.Integer] = m


@dataclasses.dataclass
class FillBuilder_0(_option.LikeOptionBuilder):
    """
    Builds ``Fill_0``.

    Attributes:
        prefix: Star prefix.
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
    prefix: str | types.String = None
    m: str | int | types.Integer = None

    def build(self):
        """
        Builds ``FillBuilder_0`` into ``Fill_0``.

        Returns:
            ``Fill_0`` for ``FillBuilder_0``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

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

        return Fill_0(
            prefix=prefix,
            i=i,
            j=j,
            k=k,
            universes=universes,
            m=m,
        )

    @staticmethod
    def unbuild(ast: Fill_0):
        """
        Unbuilds ``Fill_0`` into ``FillBuilder_0``

        Returns:
            ``FillBuilder_0`` for ``Fill_0``.
        """

        return FillBuilder_0(
            prefix=copy.deepcopy(ast.prefix),
            i=copy.deepcopy(ast.i),
            j=copy.deepcopy(ast.j),
            k=copy.deepcopy(ast.k),
            universes=copy.deepcopy(ast.universes),
            m=copy.deepcopy(ast.m),
        )
