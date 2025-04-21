import re
import typing
import dataclasses


from ._option import StopOption
from ....utils import types
from ....utils import errors


class Ctme(StopOption, keyword='ctme'):
    """
    Represents INP ctme elements.

    Attributes:
        tme: Computer time before stop.
    """

    _ATTRS = {
        'tme': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Actme( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, tme: types.RealOrJump):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: Computer time before stop.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if tme is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tme)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tme,
            ]
        )

        self.tme: typing.Final[types.RealOrJump] = tme


@dataclasses.dataclass
class CtmeBuilder:
    """
    Builds ``Ctme``.

    Attributes:
        tme: Computer time before stop.
    """

    tme: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``CtmeBuilder`` into ``Ctme``.

        Returns:
            ``Ctme`` for ``CtmeBuilder``.
        """

        if isinstance(self.tme, types.Real):
            tme = self.tme
        elif isinstance(self.tme, float) or isinstance(self.tme, int):
            tme = types.RealOrJump(self.tme)
        elif isinstance(self.tme, str):
            tme = types.RealOrJump.from_mcnp(self.tme)

        return Ctme(
            tme=tme,
        )
