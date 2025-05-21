import re
import copy
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Cend(TOption_1):
    """
    Represents INP cend elements.

    Attributes:
        time: Reference ending time.
    """

    _KEYWORD = 'cend'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Acend( {types.Real._REGEX.pattern})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Cend``.

        Parameters:
            time: Reference ending time.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, time)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time,
            ]
        )

        self.time: typing.Final[types.Real] = time


@dataclasses.dataclass
class CendBuilder:
    """
    Builds ``Cend``.

    Attributes:
        time: Reference ending time.
    """

    time: str | float | types.Real

    def build(self):
        """
        Builds ``CendBuilder`` into ``Cend``.

        Returns:
            ``Cend`` for ``CendBuilder``.
        """

        time = self.time
        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.Real(self.time)
        elif isinstance(self.time, str):
            time = types.Real.from_mcnp(self.time)

        return Cend(
            time=time,
        )

    @staticmethod
    def unbuild(ast: Cend):
        """
        Unbuilds ``Cend`` into ``CendBuilder``

        Returns:
            ``CendBuilder`` for ``Cend``.
        """

        return Cend(
            time=copy.deepcopy(ast.time),
        )
