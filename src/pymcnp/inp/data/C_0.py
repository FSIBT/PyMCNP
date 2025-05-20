import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class C_0(DataOption):
    """
    Represents INP c variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper cosine bounds for bin.
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        't': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'\Ac(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.Real],
        t: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``C_0``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper cosine bounds for bin.
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

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

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class CBuilder_0:
    """
    Builds ``C_0``.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper cosine bounds for bin.
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    bounds: list[str] | list[float] | list[types.Real]
    t: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``CBuilder_0`` into ``C_0``.

        Returns:
            ``C_0`` for ``CBuilder_0``.
        """

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

        return C_0(
            suffix=suffix,
            bounds=bounds,
            t=t,
            c=c,
        )
