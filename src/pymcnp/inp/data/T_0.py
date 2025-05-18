import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class T_0(DataOption):
    """
    Represents INP t variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper time bounds for bin.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.RealOrJump],
        'nt': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'\At(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.RealOrJump],
        nt: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``T_0``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper time bounds for bin.
            nt: Notation to inhibit automatic totaling.
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
                nt,
                c,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds
        self.nt: typing.Final[types.String] = nt
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class TBuilder_0:
    """
    Builds ``T_0``.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper time bounds for bin.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    bounds: list[str] | list[float] | list[types.RealOrJump]
    nt: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``TBuilder_0`` into ``T_0``.

        Returns:
            ``T_0`` for ``TBuilder_0``.
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
                if isinstance(item, types.RealOrJump):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.RealOrJump(item))
                elif isinstance(item, str):
                    bounds.append(types.RealOrJump.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        nt = self.nt
        if isinstance(self.nt, types.String):
            nt = self.nt
        elif isinstance(self.nt, str):
            nt = types.String.from_mcnp(self.nt)

        c = self.c
        if isinstance(self.c, types.String):
            c = self.c
        elif isinstance(self.c, str):
            c = types.String.from_mcnp(self.c)

        return T_0(
            suffix=suffix,
            bounds=bounds,
            nt=nt,
            c=c,
        )
