import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class E(DataOption):
    """
    Represents INP e elements.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper energy bounds for bin.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
        'nt': types.String,
        'c': types.String,
    }

    _REGEX = re.compile(
        rf'\Ae(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        bounds: types.Tuple[types.Real],
        nt: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``E``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Upper energy bounds for bin.
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
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
        self.nt: typing.Final[types.String] = nt
        self.c: typing.Final[types.String] = c


@dataclasses.dataclass
class EBuilder:
    """
    Builds ``E``.

    Attributes:
        suffix: Data card option suffix.
        bounds: Upper energy bounds for bin.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
    """

    suffix: str | int | types.Integer
    bounds: list[str] | list[float] | list[types.Real]
    nt: str | types.String = None
    c: str | types.String = None

    def build(self):
        """
        Builds ``EBuilder`` into ``E``.

        Returns:
            ``E`` for ``EBuilder``.
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

        return E(
            suffix=suffix,
            bounds=bounds,
            nt=nt,
            c=c,
        )
