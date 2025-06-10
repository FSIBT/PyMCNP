import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Xlims(_option.MplotOption):
    """
    Represents INP xlims elements.

    Attributes:
        lower: x-axis lower limit.
        upper: x-axis upper limit.
        nsteps: x-axis interval.
    """

    _KEYWORD = 'xlims'

    _ATTRS = {
        'lower': types.Real,
        'upper': types.Real,
        'nsteps': types.Real,
    }

    _REGEX = re.compile(rf'\Axlims( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, lower: types.Real, upper: types.Real, nsteps: types.Real = None):
        """
        Initializes ``Xlims``.

        Parameters:
            lower: x-axis lower limit.
            upper: x-axis upper limit.
            nsteps: x-axis interval.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lower)
        if upper is None or not (lower.value < upper.value):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, upper)
        if nsteps is not None and not (nsteps.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nsteps)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lower,
                upper,
                nsteps,
            ]
        )

        self.lower: typing.Final[types.Real] = lower
        self.upper: typing.Final[types.Real] = upper
        self.nsteps: typing.Final[types.Real] = nsteps


@dataclasses.dataclass
class XlimsBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Xlims``.

    Attributes:
        lower: x-axis lower limit.
        upper: x-axis upper limit.
        nsteps: x-axis interval.
    """

    lower: str | float | types.Real
    upper: str | float | types.Real
    nsteps: str | float | types.Real = None

    def build(self):
        """
        Builds ``XlimsBuilder`` into ``Xlims``.

        Returns:
            ``Xlims`` for ``XlimsBuilder``.
        """

        lower = self.lower
        if isinstance(self.lower, types.Real):
            lower = self.lower
        elif isinstance(self.lower, float) or isinstance(self.lower, int):
            lower = types.Real(self.lower)
        elif isinstance(self.lower, str):
            lower = types.Real.from_mcnp(self.lower)

        upper = self.upper
        if isinstance(self.upper, types.Real):
            upper = self.upper
        elif isinstance(self.upper, float) or isinstance(self.upper, int):
            upper = types.Real(self.upper)
        elif isinstance(self.upper, str):
            upper = types.Real.from_mcnp(self.upper)

        nsteps = self.nsteps
        if isinstance(self.nsteps, types.Real):
            nsteps = self.nsteps
        elif isinstance(self.nsteps, float) or isinstance(self.nsteps, int):
            nsteps = types.Real(self.nsteps)
        elif isinstance(self.nsteps, str):
            nsteps = types.Real.from_mcnp(self.nsteps)

        return Xlims(
            lower=lower,
            upper=upper,
            nsteps=nsteps,
        )

    @staticmethod
    def unbuild(ast: Xlims):
        """
        Unbuilds ``Xlims`` into ``XlimsBuilder``

        Returns:
            ``XlimsBuilder`` for ``Xlims``.
        """

        return XlimsBuilder(
            lower=copy.deepcopy(ast.lower),
            upper=copy.deepcopy(ast.upper),
            nsteps=copy.deepcopy(ast.nsteps),
        )
