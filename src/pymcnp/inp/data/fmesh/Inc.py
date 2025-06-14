import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Inc(_option.FmeshOption):
    """
    Represents INP inc elements.

    Attributes:
        lower: Collision for FMESH tally lower bound.
        upper: Collision for FMESH tally upper bound.
    """

    _KEYWORD = 'inc'

    _ATTRS = {
        'lower': types.Real,
        'upper': types.Real,
    }

    _REGEX = re.compile(rf'\Ainc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, lower: types.Real, upper: types.Real = None):
        """
        Initializes ``Inc``.

        Parameters:
            lower: Collision for FMESH tally lower bound.
            upper: Collision for FMESH tally upper bound.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, lower)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lower,
                upper,
            ]
        )

        self.lower: typing.Final[types.Real] = lower
        self.upper: typing.Final[types.Real] = upper


@dataclasses.dataclass
class IncBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Inc``.

    Attributes:
        lower: Collision for FMESH tally lower bound.
        upper: Collision for FMESH tally upper bound.
    """

    lower: str | float | types.Real
    upper: str | float | types.Real = None

    def build(self):
        """
        Builds ``IncBuilder`` into ``Inc``.

        Returns:
            ``Inc`` for ``IncBuilder``.
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

        return Inc(
            lower=lower,
            upper=upper,
        )

    @staticmethod
    def unbuild(ast: Inc):
        """
        Unbuilds ``Inc`` into ``IncBuilder``

        Returns:
            ``IncBuilder`` for ``Inc``.
        """

        return IncBuilder(
            lower=copy.deepcopy(ast.lower),
            upper=copy.deepcopy(ast.upper),
        )
