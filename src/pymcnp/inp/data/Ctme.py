import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ctme(DataOption, keyword='ctme'):
    """
    Represents INP ctme elements.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    _ATTRS = {
        'tme': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Actme( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, tme: types.IntegerOrJump):
        """
        Initializes ``Ctme``.

        Parameters:
            tme: maximum amount of minutes for Monte Carlo calculation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if tme is None or not (tme >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tme)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tme,
            ]
        )

        self.tme: typing.Final[types.IntegerOrJump] = tme


@dataclasses.dataclass
class CtmeBuilder:
    """
    Builds ``Ctme``.

    Attributes:
        tme: maximum amount of minutes for Monte Carlo calculation.
    """

    tme: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``CtmeBuilder`` into ``Ctme``.

        Returns:
            ``Ctme`` for ``CtmeBuilder``.
        """

        if isinstance(self.tme, types.Integer):
            tme = self.tme
        elif isinstance(self.tme, int):
            tme = types.IntegerOrJump(self.tme)
        elif isinstance(self.tme, str):
            tme = types.IntegerOrJump.from_mcnp(self.tme)

        return Ctme(
            tme=tme,
        )
