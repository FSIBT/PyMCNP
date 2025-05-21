import re
import copy
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Cbeg(TOption_1):
    """
    Represents INP cbeg elements.

    Attributes:
        time: Reference starting time.
    """

    _KEYWORD = 'cbeg'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Acbeg( {types.Real._REGEX.pattern})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Cbeg``.

        Parameters:
            time: Reference starting time.

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
class CbegBuilder:
    """
    Builds ``Cbeg``.

    Attributes:
        time: Reference starting time.
    """

    time: str | float | types.Real

    def build(self):
        """
        Builds ``CbegBuilder`` into ``Cbeg``.

        Returns:
            ``Cbeg`` for ``CbegBuilder``.
        """

        time = self.time
        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.Real(self.time)
        elif isinstance(self.time, str):
            time = types.Real.from_mcnp(self.time)

        return Cbeg(
            time=time,
        )

    @staticmethod
    def unbuild(ast: Cbeg):
        """
        Unbuilds ``Cbeg`` into ``CbegBuilder``

        Returns:
            ``CbegBuilder`` for ``Cbeg``.
        """

        return Cbeg(
            time=copy.deepcopy(ast.time),
        )
