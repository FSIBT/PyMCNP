import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Time(_option.EmbeeOption):
    """
    Represents INP time elements.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    _KEYWORD = 'time'

    _ATTRS = {
        'factor': types.Real,
    }

    _REGEX = re.compile(rf'\Atime( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, factor: types.Real):
        """
        Initializes ``Time``.

        Parameters:
            factor: Multiplicative conversion factor for time-related output.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if factor is None or not (factor > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, factor)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                factor,
            ]
        )

        self.factor: typing.Final[types.Real] = factor


@dataclasses.dataclass
class TimeBuilder(_option.EmbeeOptionBuilder):
    """
    Builds ``Time``.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    factor: str | float | types.Real

    def build(self):
        """
        Builds ``TimeBuilder`` into ``Time``.

        Returns:
            ``Time`` for ``TimeBuilder``.
        """

        factor = self.factor
        if isinstance(self.factor, types.Real):
            factor = self.factor
        elif isinstance(self.factor, float) or isinstance(self.factor, int):
            factor = types.Real(self.factor)
        elif isinstance(self.factor, str):
            factor = types.Real.from_mcnp(self.factor)

        return Time(
            factor=factor,
        )

    @staticmethod
    def unbuild(ast: Time):
        """
        Unbuilds ``Time`` into ``TimeBuilder``

        Returns:
            ``TimeBuilder`` for ``Time``.
        """

        return TimeBuilder(
            factor=copy.deepcopy(ast.factor),
        )
