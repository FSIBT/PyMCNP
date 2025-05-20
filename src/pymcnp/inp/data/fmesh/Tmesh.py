import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Tmesh(FmeshOption):
    """
    Represents INP tmesh elements.

    Attributes:
        time: Values of mesh points in time.
    """

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Atmesh( {types.Real._REGEX.pattern})\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``Tmesh``.

        Parameters:
            time: Values of mesh points in time.

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
class TmeshBuilder:
    """
    Builds ``Tmesh``.

    Attributes:
        time: Values of mesh points in time.
    """

    time: str | float | types.Real

    def build(self):
        """
        Builds ``TmeshBuilder`` into ``Tmesh``.

        Returns:
            ``Tmesh`` for ``TmeshBuilder``.
        """

        time = self.time
        if isinstance(self.time, types.Real):
            time = self.time
        elif isinstance(self.time, float) or isinstance(self.time, int):
            time = types.Real(self.time)
        elif isinstance(self.time, str):
            time = types.Real.from_mcnp(self.time)

        return Tmesh(
            time=time,
        )
