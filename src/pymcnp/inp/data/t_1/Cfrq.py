import re
import copy
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Cfrq(TOption_1):
    """
    Represents INP cfrq elements.

    Attributes:
        frequency: Frequency of cycling.
    """

    _KEYWORD = 'cfrq'

    _ATTRS = {
        'frequency': types.Real,
    }

    _REGEX = re.compile(rf'\Acfrq( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, frequency: types.Real):
        """
        Initializes ``Cfrq``.

        Parameters:
            frequency: Frequency of cycling.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if frequency is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, frequency)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                frequency,
            ]
        )

        self.frequency: typing.Final[types.Real] = frequency


@dataclasses.dataclass
class CfrqBuilder:
    """
    Builds ``Cfrq``.

    Attributes:
        frequency: Frequency of cycling.
    """

    frequency: str | float | types.Real

    def build(self):
        """
        Builds ``CfrqBuilder`` into ``Cfrq``.

        Returns:
            ``Cfrq`` for ``CfrqBuilder``.
        """

        frequency = self.frequency
        if isinstance(self.frequency, types.Real):
            frequency = self.frequency
        elif isinstance(self.frequency, float) or isinstance(self.frequency, int):
            frequency = types.Real(self.frequency)
        elif isinstance(self.frequency, str):
            frequency = types.Real.from_mcnp(self.frequency)

        return Cfrq(
            frequency=frequency,
        )

    @staticmethod
    def unbuild(ast: Cfrq):
        """
        Unbuilds ``Cfrq`` into ``CfrqBuilder``

        Returns:
            ``CfrqBuilder`` for ``Cfrq``.
        """

        return Cfrq(
            frequency=copy.deepcopy(ast.frequency),
        )
