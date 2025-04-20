import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_1(DataOption_, keyword='phys:p'):
    """
    Represents INP phys variation #1 elements.

    Attributes:
        emcpf: Upper energy limit for photon treatment.
        ides: Generation of elections by photon controls.
        nocoh: Coherent Thomson scattering controls.
        ispn: Photonuclear particle production controls.
        nodop: Photon Doppler energy broadening controls.
        fism: Selection of photofission method controls.
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
        rf'\Aphys:p( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?\Z'
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

        if ides is not None and not (isinstance(ides.value, types.Jump) or ides.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ides)
        if nocoh is not None and not (isinstance(nocoh.value, types.Jump) or nocoh.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nocoh)
        if ispn is not None and not (isinstance(ispn.value, types.Jump) or ispn.value in {-1, 0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ispn)
        if nodop is not None and not (isinstance(nodop.value, types.Jump) or nodop.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nodop)
        if fism is not None and not (isinstance(fism.value, types.Jump) or fism.value in {0, 1}):
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


@dataclasses.dataclass
class PhysBuilder_1:
    """
    Builds ``Phys_1``.

    Attributes:
        emcpf: Upper energy limit for photon treatment.
        ides: Generation of elections by photon controls.
        nocoh: Coherent Thomson scattering controls.
        ispn: Photonuclear particle production controls.
        nodop: Photon Doppler energy broadening controls.
        fism: Selection of photofission method controls.
    """

    emcpf: str | float | types.RealOrJump
    ides: str | int | types.IntegerOrJump
    nocoh: str | int | types.IntegerOrJump
    ispn: str | int | types.IntegerOrJump
    nodop: str | int | types.IntegerOrJump
    fism: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``PhysBuilder_1`` into ``Phys_1``.

        Returns:
            ``Phys_1`` for ``PhysBuilder_1``.
        """

        if isinstance(self.emcpf, types.Real):
            emcpf = self.emcpf
        elif isinstance(self.emcpf, float) or isinstance(self.emcpf, int):
            emcpf = types.RealOrJump(self.emcpf)
        elif isinstance(self.emcpf, str):
            emcpf = types.RealOrJump.from_mcnp(self.emcpf)

        if isinstance(self.ides, types.Integer):
            ides = self.ides
        elif isinstance(self.ides, int):
            ides = types.IntegerOrJump(self.ides)
        elif isinstance(self.ides, str):
            ides = types.IntegerOrJump.from_mcnp(self.ides)

        if isinstance(self.nocoh, types.Integer):
            nocoh = self.nocoh
        elif isinstance(self.nocoh, int):
            nocoh = types.IntegerOrJump(self.nocoh)
        elif isinstance(self.nocoh, str):
            nocoh = types.IntegerOrJump.from_mcnp(self.nocoh)

        if isinstance(self.ispn, types.Integer):
            ispn = self.ispn
        elif isinstance(self.ispn, int):
            ispn = types.IntegerOrJump(self.ispn)
        elif isinstance(self.ispn, str):
            ispn = types.IntegerOrJump.from_mcnp(self.ispn)

        if isinstance(self.nodop, types.Integer):
            nodop = self.nodop
        elif isinstance(self.nodop, int):
            nodop = types.IntegerOrJump(self.nodop)
        elif isinstance(self.nodop, str):
            nodop = types.IntegerOrJump.from_mcnp(self.nodop)

        if isinstance(self.fism, types.Integer):
            fism = self.fism
        elif isinstance(self.fism, int):
            fism = types.IntegerOrJump(self.fism)
        elif isinstance(self.fism, str):
            fism = types.IntegerOrJump.from_mcnp(self.fism)

        return Phys_1(
            emcpf=emcpf,
            ides=ides,
            nocoh=nocoh,
            ispn=ispn,
            nodop=nodop,
            fism=fism,
        )
