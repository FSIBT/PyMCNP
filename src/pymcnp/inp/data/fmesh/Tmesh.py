import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tmesh(_option.FmeshOption):
    """
    Represents INP tmesh elements.

    Attributes:
        time: Values of mesh points in time.
    """

    _KEYWORD = 'tmesh'

    _ATTRS = {
        'time': types.Real,
    }

    _REGEX = re.compile(rf'\Atmesh( {types.Real._REGEX.pattern[2:-2]})\Z')

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
class TmeshBuilder(_option.FmeshOptionBuilder):
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

    @staticmethod
    def unbuild(ast: Tmesh):
        """
        Unbuilds ``Tmesh`` into ``TmeshBuilder``

        Returns:
            ``TmeshBuilder`` for ``Tmesh``.
        """

        return TmeshBuilder(
            time=copy.deepcopy(ast.time),
        )
