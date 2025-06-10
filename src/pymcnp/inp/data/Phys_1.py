import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Phys_1(_option.DataOption):
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

    _KEYWORD = 'phys:p'

    _ATTRS = {
        'emcpf': types.Real,
        'ides': types.Integer,
        'nocoh': types.Integer,
        'ispn': types.Integer,
        'nodop': types.Integer,
        'fism': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aphys:p( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(self, emcpf: types.Real = None, ides: types.Integer = None, nocoh: types.Integer = None, ispn: types.Integer = None, nodop: types.Integer = None, fism: types.Integer = None):
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
            InpError: SEMANTICS_OPTION.
        """

        if ides is not None and not (isinstance(ides.value, types.Jump) or ides.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ides)
        if nocoh is not None and not (isinstance(nocoh.value, types.Jump) or nocoh.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nocoh)
        if ispn is not None and not (isinstance(ispn.value, types.Jump) or ispn.value in {-1, 0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ispn)
        if nodop is not None and not (isinstance(nodop.value, types.Jump) or nodop.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nodop)

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


@dataclasses.dataclass
class PhysBuilder_1(_option.DataOptionBuilder):
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

    emcpf: str | float | types.Real = None
    ides: str | int | types.Integer = None
    nocoh: str | int | types.Integer = None
    ispn: str | int | types.Integer = None
    nodop: str | int | types.Integer = None
    fism: str | int | types.Integer = None

    def build(self):
        """
        Builds ``PhysBuilder_1`` into ``Phys_1``.

        Returns:
            ``Phys_1`` for ``PhysBuilder_1``.
        """

        emcpf = self.emcpf
        if isinstance(self.emcpf, types.Real):
            emcpf = self.emcpf
        elif isinstance(self.emcpf, float) or isinstance(self.emcpf, int):
            emcpf = types.Real(self.emcpf)
        elif isinstance(self.emcpf, str):
            emcpf = types.Real.from_mcnp(self.emcpf)

        ides = self.ides
        if isinstance(self.ides, types.Integer):
            ides = self.ides
        elif isinstance(self.ides, int):
            ides = types.Integer(self.ides)
        elif isinstance(self.ides, str):
            ides = types.Integer.from_mcnp(self.ides)

        nocoh = self.nocoh
        if isinstance(self.nocoh, types.Integer):
            nocoh = self.nocoh
        elif isinstance(self.nocoh, int):
            nocoh = types.Integer(self.nocoh)
        elif isinstance(self.nocoh, str):
            nocoh = types.Integer.from_mcnp(self.nocoh)

        ispn = self.ispn
        if isinstance(self.ispn, types.Integer):
            ispn = self.ispn
        elif isinstance(self.ispn, int):
            ispn = types.Integer(self.ispn)
        elif isinstance(self.ispn, str):
            ispn = types.Integer.from_mcnp(self.ispn)

        nodop = self.nodop
        if isinstance(self.nodop, types.Integer):
            nodop = self.nodop
        elif isinstance(self.nodop, int):
            nodop = types.Integer(self.nodop)
        elif isinstance(self.nodop, str):
            nodop = types.Integer.from_mcnp(self.nodop)

        fism = self.fism
        if isinstance(self.fism, types.Integer):
            fism = self.fism
        elif isinstance(self.fism, int):
            fism = types.Integer(self.fism)
        elif isinstance(self.fism, str):
            fism = types.Integer.from_mcnp(self.fism)

        return Phys_1(
            emcpf=emcpf,
            ides=ides,
            nocoh=nocoh,
            ispn=ispn,
            nodop=nodop,
            fism=fism,
        )

    @staticmethod
    def unbuild(ast: Phys_1):
        """
        Unbuilds ``Phys_1`` into ``PhysBuilder_1``

        Returns:
            ``PhysBuilder_1`` for ``Phys_1``.
        """

        return PhysBuilder_1(
            emcpf=copy.deepcopy(ast.emcpf),
            ides=copy.deepcopy(ast.ides),
            nocoh=copy.deepcopy(ast.nocoh),
            ispn=copy.deepcopy(ast.ispn),
            nodop=copy.deepcopy(ast.nodop),
            fism=copy.deepcopy(ast.fism),
        )
