import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Thresh(_option.ActOption):
    """
    Represents INP thresh elements.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    _KEYWORD = 'thresh'

    _ATTRS = {
        'fraction': types.Real,
    }

    _REGEX = re.compile(rf'\Athresh( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, fraction: types.Real):
        """
        Initializes ``Thresh``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if fraction is None or not (0 <= fraction.value <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, fraction)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fraction,
            ]
        )

        self.fraction: typing.Final[types.Real] = fraction


@dataclasses.dataclass
class ThreshBuilder(_option.ActOptionBuilder):
    """
    Builds ``Thresh``.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    fraction: str | float | types.Real

    def build(self):
        """
        Builds ``ThreshBuilder`` into ``Thresh``.

        Returns:
            ``Thresh`` for ``ThreshBuilder``.
        """

        fraction = self.fraction
        if isinstance(self.fraction, types.Real):
            fraction = self.fraction
        elif isinstance(self.fraction, float) or isinstance(self.fraction, int):
            fraction = types.Real(self.fraction)
        elif isinstance(self.fraction, str):
            fraction = types.Real.from_mcnp(self.fraction)

        return Thresh(
            fraction=fraction,
        )

    @staticmethod
    def unbuild(ast: Thresh):
        """
        Unbuilds ``Thresh`` into ``ThreshBuilder``

        Returns:
            ``ThreshBuilder`` for ``Thresh``.
        """

        return ThreshBuilder(
            fraction=copy.deepcopy(ast.fraction),
        )
