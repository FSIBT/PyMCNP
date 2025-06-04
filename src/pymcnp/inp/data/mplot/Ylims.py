import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Ylims(MplotOption):
    """
    Represents INP ylims elements.

    Attributes:
        min: y-axis lower limit.
        max: y-axis upper limit.
        nsteps: y-axis interval.
    """

    _KEYWORD = 'ylims'

    _ATTRS = {
        'min': types.Real,
        'max': types.Real,
        'nsteps': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aylims( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(self, min: types.Real, max: types.Real, nsteps: types.Real = None):
        """
        Initializes ``Ylims``.

        Parameters:
            min: y-axis lower limit.
            max: y-axis upper limit.
            nsteps: y-axis interval.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if min is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, min)
        if max is None or not (min.value < max.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, max)
        if nsteps is not None and not (nsteps.value >= 0):
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
class YlimsBuilder:
    """
    Builds ``Ylims``.

    Attributes:
        min: y-axis lower limit.
        max: y-axis upper limit.
        nsteps: y-axis interval.
    """

    min: str | float | types.Real
    max: str | float | types.Real
    nsteps: str | float | types.Real = None

    def build(self):
        """
        Builds ``YlimsBuilder`` into ``Ylims``.

        Returns:
            ``Ylims`` for ``YlimsBuilder``.
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

        return Ylims(
            min=min,
            max=max,
            nsteps=nsteps,
        )

    @staticmethod
    def unbuild(ast: Ylims):
        """
        Unbuilds ``Ylims`` into ``YlimsBuilder``

        Returns:
            ``YlimsBuilder`` for ``Ylims``.
        """

        return Ylims(
            min=copy.deepcopy(ast.min),
            max=copy.deepcopy(ast.max),
            nsteps=copy.deepcopy(ast.nsteps),
        )
