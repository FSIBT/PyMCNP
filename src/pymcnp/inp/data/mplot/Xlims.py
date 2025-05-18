import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Xlims(MplotOption):
    """
    Represents INP xlims elements.

    Attributes:
        min: x-axis lower limit.
        max: x-axis upper limit.
        nsteps: x-axis interval.
    """

    _ATTRS = {
        'min': types.Real,
        'max': types.Real,
        'nsteps': types.Real,
    }

    _REGEX = re.compile(
        rf'\Axlims( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?\Z'
    )

    def __init__(self, min: types.Real, max: types.Real, nsteps: types.Real = None):
        """
        Initializes ``Xlims``.

        Parameters:
            min: x-axis lower limit.
            max: x-axis upper limit.
            nsteps: x-axis interval.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if min is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, min)
        if max is None or not (min < max):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, max)
        if nsteps is not None and not (nsteps >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nsteps)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                min,
                max,
                nsteps,
            ]
        )

        self.min: typing.Final[types.Real] = min
        self.max: typing.Final[types.Real] = max
        self.nsteps: typing.Final[types.Real] = nsteps


@dataclasses.dataclass
class XlimsBuilder:
    """
    Builds ``Xlims``.

    Attributes:
        min: x-axis lower limit.
        max: x-axis upper limit.
        nsteps: x-axis interval.
    """

    min: str | float | types.Real
    max: str | float | types.Real
    nsteps: str | float | types.Real = None

    def build(self):
        """
        Builds ``XlimsBuilder`` into ``Xlims``.

        Returns:
            ``Xlims`` for ``XlimsBuilder``.
        """

        min = self.min
        if isinstance(self.min, types.Real):
            min = self.min
        elif isinstance(self.min, float) or isinstance(self.min, int):
            min = types.Real(self.min)
        elif isinstance(self.min, str):
            min = types.Real.from_mcnp(self.min)

        max = self.max
        if isinstance(self.max, types.Real):
            max = self.max
        elif isinstance(self.max, float) or isinstance(self.max, int):
            max = types.Real(self.max)
        elif isinstance(self.max, str):
            max = types.Real.from_mcnp(self.max)

        nsteps = self.nsteps
        if isinstance(self.nsteps, types.Real):
            nsteps = self.nsteps
        elif isinstance(self.nsteps, float) or isinstance(self.nsteps, int):
            nsteps = types.Real(self.nsteps)
        elif isinstance(self.nsteps, str):
            nsteps = types.Real.from_mcnp(self.nsteps)

        return Xlims(
            min=min,
            max=max,
            nsteps=nsteps,
        )
