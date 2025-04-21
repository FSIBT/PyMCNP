import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Tme_1(SdefOption, keyword='tme'):
    """
    Represents INP tme variation #1 elements.

    Attributes:
        time: Time in shakes.
    """

    _ATTRS = {
        'time': types.EmbeddedDistributionNumber,
    }

    _REGEX = re.compile(rf'\Atme( {types.EmbeddedDistributionNumber._REGEX.pattern})\Z')

    def __init__(self, time: types.EmbeddedDistributionNumber):
        """
        Initializes ``Tme_1``.

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

        self.time: typing.Final[types.EmbeddedDistributionNumber] = time


@dataclasses.dataclass
class TmeBuilder_1:
    """
    Builds ``Tme_1``.

    Attributes:
        time: Time in shakes.
    """

    time: str | types.EmbeddedDistributionNumber

    def build(self):
        """
        Builds ``TmeBuilder_1`` into ``Tme_1``.

        Returns:
            ``Tme_1`` for ``TmeBuilder_1``.
        """

        if isinstance(self.time, types.EmbeddedDistributionNumber):
            time = self.time
        elif isinstance(self.time, str):
            time = types.EmbeddedDistributionNumber.from_mcnp(self.time)

        return Tme_1(
            time=time,
        )
