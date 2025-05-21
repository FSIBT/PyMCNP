import re
import copy
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Cofi(TOption_1):
    """
    Represents INP cofi elements.

    Attributes:
        time: Dead time interval.
    """

    _KEYWORD = 'cofi'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Acofi( {types.Real._REGEX.pattern})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Cofi``.

        Parameters:
            time: Dead time interval.

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
class CofiBuilder:
    """
    Builds ``Cofi``.

    Attributes:
        time: Dead time interval.
    """

    time: str | float | types.Real

    def build(self):
        """
        Builds ``CofiBuilder`` into ``Cofi``.

        Returns:
            ``Cofi`` for ``CofiBuilder``.
        """

        time = self.time
        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.Real(self.time)
        elif isinstance(self.time, str):
            time = types.Real.from_mcnp(self.time)

        return Cofi(
            time=time,
        )

    @staticmethod
    def unbuild(ast: Cofi):
        """
        Unbuilds ``Cofi`` into ``CofiBuilder``

        Returns:
            ``CofiBuilder`` for ``Cofi``.
        """

        return Cofi(
            time=copy.deepcopy(ast.time),
        )
