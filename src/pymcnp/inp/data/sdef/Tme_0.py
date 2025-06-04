import re
import copy
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Tme_0(SdefOption):
    """
    Represents INP tme variation #0 elements.

    Attributes:
        time: Time in shakes.
    """

    _KEYWORD = 'tme'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Atme( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Tme_0``.

        Parameters:
            time: Time in shakes.

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
class TmeBuilder_0:
    """
    Builds ``Tme_0``.

    Attributes:
        time: Time in shakes.
    """

    time: str | float | types.Real

    def build(self):
        """
        Builds ``TmeBuilder_0`` into ``Tme_0``.

        Returns:
            ``Tme_0`` for ``TmeBuilder_0``.
        """

        time = self.time
        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.Real(self.time)
        elif isinstance(self.time, str):
            time = types.Real.from_mcnp(self.time)

        return Tme_0(
            time=time,
        )

    @staticmethod
    def unbuild(ast: Tme_0):
        """
        Unbuilds ``Tme_0`` into ``TmeBuilder_0``

        Returns:
            ``TmeBuilder_0`` for ``Tme_0``.
        """

        return Tme_0(
            time=copy.deepcopy(ast.time),
        )
