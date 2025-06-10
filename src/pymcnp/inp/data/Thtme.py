import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Thtme(_option.DataOption):
    """
    Represents INP thtme elements.

    Attributes:
        times: Tuple of times when thermal temperatures are specified.
    """

    _KEYWORD = 'thtme'

    _ATTRS = {
        'times': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Athtme((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, times: types.Tuple[types.Real]):
        """
        Initializes ``Thtme``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if times is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, times)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                times,
            ]
        )

        self.times: typing.Final[types.Tuple[types.Real]] = times


@dataclasses.dataclass
class ThtmeBuilder(_option.DataOptionBuilder):
    """
    Builds ``Thtme``.

    Attributes:
        times: Tuple of times when thermal temperatures are specified.
    """

    times: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``ThtmeBuilder`` into ``Thtme``.

        Returns:
            ``Thtme`` for ``ThtmeBuilder``.
        """

        if self.times:
            times = []
            for item in self.times:
                if isinstance(item, types.Real):
                    times.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    times.append(types.Real(item))
                elif isinstance(item, str):
                    times.append(types.Real.from_mcnp(item))
            times = types.Tuple(times)
        else:
            times = None

        return Thtme(
            times=times,
        )

    @staticmethod
    def unbuild(ast: Thtme):
        """
        Unbuilds ``Thtme`` into ``ThtmeBuilder``

        Returns:
            ``ThtmeBuilder`` for ``Thtme``.
        """

        return ThtmeBuilder(
            times=copy.deepcopy(ast.times),
        )
