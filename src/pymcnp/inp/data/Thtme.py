import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Thtme(DataOption, keyword='thtme'):
    """
    Represents INP thtme elements.

    Attributes:
        times: Tuple of times when thermal temperatures are specified.
    """

    _ATTRS = {
        'times': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Athtme((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, times: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Thtme``.

        Parameters:
            times: Tuple of times when thermal temperatures are specified.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if times is None or not (filter(lambda entry: not (entry <= 99), times)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, times)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                times,
            ]
        )

        self.times: typing.Final[types.Tuple[types.RealOrJump]] = times


@dataclasses.dataclass
class ThtmeBuilder:
    """
    Builds ``Thtme``.

    Attributes:
        times: Tuple of times when thermal temperatures are specified.
    """

    times: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``ThtmeBuilder`` into ``Thtme``.

        Returns:
            ``Thtme`` for ``ThtmeBuilder``.
        """

        times = []
        for item in self.times:
            if isinstance(item, types.RealOrJump):
                times.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                times.append(types.RealOrJump(item))
            elif isinstance(item, str):
                times.append(types.RealOrJump.from_mcnp(item))
        times = types.Tuple(times)

        return Thtme(
            times=times,
        )
