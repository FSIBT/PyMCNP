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
        'prefix': types.Integer,
        'axsh': types.Integer,
        'axsv': types.Integer,
        'emaps': types.Tuple[types.Real],
    }

    _REGEX = re.compile(
        rf'\Acosyp( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})((?: {types.Real._REGEX.pattern})+?)\Z'
    )

    def __init__(
        self,
        prefix: types.Integer,
        axsh: types.Integer,
        axsv: types.Integer,
        emaps: types.Tuple[types.Real],
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

        self.prefix: typing.Final[types.Integer] = prefix
        self.axsh: typing.Final[types.Integer] = axsh
        self.axsv: typing.Final[types.Integer] = axsv
        self.emaps: typing.Final[types.Tuple[types.Real]] = emaps
