import re
import copy
import typing
import dataclasses


from ._option import TOption_1
from ....utils import types
from ....utils import errors


class Coni(TOption_1):
    """
    Represents INP coni elements.

    Attributes:
        time: Alive time interval.
    """

    _KEYWORD = 'coni'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Aconi( {types.Real._REGEX.pattern})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Coni``.

        Parameters:
            time: Alive time interval.

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
class ConiBuilder:
    """
    Builds ``Coni``.

    Attributes:
        time: Alive time interval.
    """

    time: str | float | types.Real

    def build(self):
        """
        Builds ``ConiBuilder`` into ``Coni``.

        Returns:
            ``Coni`` for ``ConiBuilder``.
        """

        time = self.time
        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.Real(self.time)
        elif isinstance(self.time, str):
            time = types.Real.from_mcnp(self.time)

        return Coni(
            time=time,
        )

    @staticmethod
    def unbuild(ast: Coni):
        """
        Unbuilds ``Coni`` into ``ConiBuilder``

        Returns:
            ``ConiBuilder`` for ``Coni``.
        """

        return Coni(
            time=copy.deepcopy(ast.time),
        )
