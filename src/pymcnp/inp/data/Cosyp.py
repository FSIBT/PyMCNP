import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Cosyp(DataOption_, keyword='cosyp'):
    """
    Represents INP cosyp elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'prefix': types.IntegerOrJump,
        'axsh': types.IntegerOrJump,
        'axsv': types.IntegerOrJump,
        'emaps': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(
        rf'\Acosyp( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})((?: {types.RealOrJump._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        prefix: types.IntegerOrJump,
        axsh: types.IntegerOrJump,
        axsv: types.IntegerOrJump,
        emaps: types.Tuple[types.RealOrJump],
    ):
        """
        Initializes ``Cosyp``.

        Parameters:
            prefix: Prefix number of the COSY map files.
            axsh: Horiztonal axis orientation.
            axsv: Vertical axis orientation.
            emaps: Tuple of operating beam energies.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if prefix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, prefix)
        if axsh is None or axsh.value not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, axsh)
        if axsv is None or axsv.value not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, axsv)
        if emaps is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emaps)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                prefix,
                axsh,
                axsv,
                emaps,
            ]
        )

        self.prefix: typing.Final[types.IntegerOrJump] = prefix
        self.axsh: typing.Final[types.IntegerOrJump] = axsh
        self.axsv: typing.Final[types.IntegerOrJump] = axsv
        self.emaps: typing.Final[types.Tuple[types.RealOrJump]] = emaps
