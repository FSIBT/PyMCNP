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
        'emcpf': types.Real,
        'ides': types.Integer,
        'nocoh': types.Integer,
        'ispn': types.Integer,
        'nodop': types.Integer,
        'fism': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aphys:p( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        emcpf: types.Real,
        ides: types.Integer,
        nocoh: types.Integer,
        ispn: types.Integer,
        nodop: types.Integer,
        fism: types.Integer,
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

        self.emcpf: typing.Final[types.Real] = emcpf
        self.ides: typing.Final[types.Integer] = ides
        self.nocoh: typing.Final[types.Integer] = nocoh
        self.ispn: typing.Final[types.Integer] = ispn
        self.nodop: typing.Final[types.Integer] = nodop
        self.fism: typing.Final[types.Integer] = fism
