import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class C(_option.DataOption):
    """
    Represents INP c elements.

    Attributes:
        prefix: Star prefix.
        suffix: Data card option suffix.
        bounds: Upper cosine bounds for bin.
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    _KEYWORD = 'c'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(rf'\A([*]?)c(\d+)((?: {types.Real._REGEX.pattern[2:-2]})+?)( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, suffix: types.Integer, bounds: types.Tuple[types.Real], prefix: types.String = None, t: types.String = None, c: types.String = None):
        """
        Initializes ``C``.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            bounds: Upper cosine bounds for bin.
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix.value not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
                t,
                c,
            ]
        )

        self.prefix: typing.Final[types.String] = prefix
        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class CBuilder(_option.DataOptionBuilder):
    """
    Builds ``C``.

    Attributes:
        prefix: Star prefix.
        suffix: Data card option suffix.
        bounds: Upper cosine bounds for bin.
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    bounds: list[str] | list[float] | list[types.Real]
    prefix: str | types.String = None
    t: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``CBuilder`` into ``C``.

        Returns:
            ``C`` for ``CBuilder``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.bounds:
            bounds = []
            for item in self.bounds:
                if isinstance(item, types.Real):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.Real(item))
                elif isinstance(item, str):
                    bounds.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        t = self.t
        if isinstance(self.t, types.String):
            t = self.t
        elif isinstance(self.t, str):
            t = types.String.from_mcnp(self.t)

        c = self.c
        if isinstance(self.c, types.String):
            c = self.c
        elif isinstance(self.c, str):
            c = types.String.from_mcnp(self.c)

        return C(
            prefix=prefix,
            suffix=suffix,
            bounds=bounds,
            t=t,
            c=c,
        )

    @staticmethod
    def unbuild(ast: C):
        """
        Unbuilds ``C`` into ``CBuilder``

        Returns:
            ``CBuilder`` for ``C``.
        """

        return CBuilder(
            prefix=copy.deepcopy(ast.prefix),
            suffix=copy.deepcopy(ast.suffix),
            bounds=copy.deepcopy(ast.bounds),
            t=copy.deepcopy(ast.t),
            c=copy.deepcopy(ast.c),
        )
