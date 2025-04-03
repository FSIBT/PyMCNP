import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_1(DataOption_, keyword='phys:p'):
    """
    Represents INP phys_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'emcpf': types.RealOrJump,
        'ides': types.IntegerOrJump,
        'nocoh': types.IntegerOrJump,
        'ispn': types.IntegerOrJump,
        'nodop': types.IntegerOrJump,
        'fism': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:p( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        emcpf: types.RealOrJump,
        ides: types.IntegerOrJump,
        nocoh: types.IntegerOrJump,
        ispn: types.IntegerOrJump,
        nodop: types.IntegerOrJump,
        fism: types.IntegerOrJump,
    ):
        """
        Initializes ``Phys_1``.

        Parameters:
            emcpf: Upper energy limit for photon treatment.
            ides: Generation of elections by photon controls.
            nocoh: Coherent Thomson scattering controls.
            ispn: Photonuclear particle production controls.
            nodop: Photon Doppler energy broadening controls.
            fism: Selection of photofission method controls.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if emcpf is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emcpf)
        if ides is None or ides not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ides)
        if nocoh is None or nocoh not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nocoh)
        if ispn is None or ispn not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ispn)
        if nodop is None or nodop not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nodop)
        if fism is None or fism not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fism)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                emcpf,
                ides,
                nocoh,
                ispn,
                nodop,
                fism,
            ]
        )

        self.emcpf: typing.Final[types.RealOrJump] = emcpf
        self.ides: typing.Final[types.IntegerOrJump] = ides
        self.nocoh: typing.Final[types.IntegerOrJump] = nocoh
        self.ispn: typing.Final[types.IntegerOrJump] = ispn
        self.nodop: typing.Final[types.IntegerOrJump] = nodop
        self.fism: typing.Final[types.IntegerOrJump] = fism
