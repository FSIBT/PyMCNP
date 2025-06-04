import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Lcc(DataOption):
    """
    Represents INP lcc elements.

    Attributes:
        stincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blocking.
        npaulincl: Pauli blocking parameter setting.
        nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
        ecutincl: Bertini model energy below this energy.
        ebankincl: INCL bank particles below this energy.
        ebankabia: ABLA bank particles below this energy.
    """

    _KEYWORD = 'lcc'

    _ATTRS = {
        'stincl': types.Real,
        'v0incl': types.Real,
        'xfoisaincl': types.Real,
        'npaulincl': types.Integer,
        'nosurfincl': types.Integer,
        'ecutincl': types.Real,
        'ebankincl': types.Real,
        'ebankabia': types.Real,
    }

    _REGEX = re.compile(
        rf'\Alcc( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        stincl: types.Real = None,
        v0incl: types.Real = None,
        xfoisaincl: types.Real = None,
        npaulincl: types.Integer = None,
        nosurfincl: types.Integer = None,
        ecutincl: types.Real = None,
        ebankincl: types.Real = None,
        ebankabia: types.Real = None,
    ):
        """
        Initializes ``Lcc``.

        Parameters:
            stincl: Rescaling factor of the cascade duration.
            v0incl: Potential depth.
            xfoisaincl: Maximum impact parameter for Pauli blocking.
            npaulincl: Pauli blocking parameter setting.
            nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
            ecutincl: Bertini model energy below this energy.
            ebankincl: INCL bank particles below this energy.
            ebankabia: ABLA bank particles below this energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if npaulincl is not None and not (
            npaulincl.value == 0 or npaulincl.value == -1 or npaulincl.value == 1
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npaulincl)
        if nosurfincl is not None and nosurfincl.value not in {-2, -1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nosurfincl)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                stincl,
                v0incl,
                xfoisaincl,
                npaulincl,
                nosurfincl,
                ecutincl,
                ebankincl,
                ebankabia,
            ]
        )

        self.stincl: typing.Final[types.Real] = stincl
        self.v0incl: typing.Final[types.Real] = v0incl
        self.xfoisaincl: typing.Final[types.Real] = xfoisaincl
        self.npaulincl: typing.Final[types.Integer] = npaulincl
        self.nosurfincl: typing.Final[types.Integer] = nosurfincl
        self.ecutincl: typing.Final[types.Real] = ecutincl
        self.ebankincl: typing.Final[types.Real] = ebankincl
        self.ebankabia: typing.Final[types.Real] = ebankabia


@dataclasses.dataclass
class LccBuilder:
    """
    Builds ``Lcc``.

    Attributes:
        stincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blocking.
        npaulincl: Pauli blocking parameter setting.
        nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
        ecutincl: Bertini model energy below this energy.
        ebankincl: INCL bank particles below this energy.
        ebankabia: ABLA bank particles below this energy.
    """

    stincl: str | float | types.Real = None
    v0incl: str | float | types.Real = None
    xfoisaincl: str | float | types.Real = None
    npaulincl: str | int | types.Integer = None
    nosurfincl: str | int | types.Integer = None
    ecutincl: str | float | types.Real = None
    ebankincl: str | float | types.Real = None
    ebankabia: str | float | types.Real = None

    def build(self):
        """
        Builds ``LccBuilder`` into ``Lcc``.

        Returns:
            ``Lcc`` for ``LccBuilder``.
        """

        stincl = self.stincl
        if isinstance(self.stincl, types.Real):
            stincl = self.stincl
        elif isinstance(self.stincl, float) or isinstance(self.stincl, int):
            stincl = types.Real(self.stincl)
        elif isinstance(self.stincl, str):
            stincl = types.Real.from_mcnp(self.stincl)

        v0incl = self.v0incl
        if isinstance(self.v0incl, types.Real):
            v0incl = self.v0incl
        elif isinstance(self.v0incl, float) or isinstance(self.v0incl, int):
            v0incl = types.Real(self.v0incl)
        elif isinstance(self.v0incl, str):
            v0incl = types.Real.from_mcnp(self.v0incl)

        xfoisaincl = self.xfoisaincl
        if isinstance(self.xfoisaincl, types.Real):
            xfoisaincl = self.xfoisaincl
        elif isinstance(self.xfoisaincl, float) or isinstance(self.xfoisaincl, int):
            xfoisaincl = types.Real(self.xfoisaincl)
        elif isinstance(self.xfoisaincl, str):
            xfoisaincl = types.Real.from_mcnp(self.xfoisaincl)

        npaulincl = self.npaulincl
        if isinstance(self.npaulincl, types.Integer):
            npaulincl = self.npaulincl
        elif isinstance(self.npaulincl, int):
            npaulincl = types.Integer(self.npaulincl)
        elif isinstance(self.npaulincl, str):
            npaulincl = types.Integer.from_mcnp(self.npaulincl)

        nosurfincl = self.nosurfincl
        if isinstance(self.nosurfincl, types.Integer):
            nosurfincl = self.nosurfincl
        elif isinstance(self.nosurfincl, int):
            nosurfincl = types.Integer(self.nosurfincl)
        elif isinstance(self.nosurfincl, str):
            nosurfincl = types.Integer.from_mcnp(self.nosurfincl)

        ecutincl = self.ecutincl
        if isinstance(self.ecutincl, types.Real):
            ecutincl = self.ecutincl
        elif isinstance(self.ecutincl, float) or isinstance(self.ecutincl, int):
            ecutincl = types.Real(self.ecutincl)
        elif isinstance(self.ecutincl, str):
            ecutincl = types.Real.from_mcnp(self.ecutincl)

        ebankincl = self.ebankincl
        if isinstance(self.ebankincl, types.Real):
            ebankincl = self.ebankincl
        elif isinstance(self.ebankincl, float) or isinstance(self.ebankincl, int):
            ebankincl = types.Real(self.ebankincl)
        elif isinstance(self.ebankincl, str):
            ebankincl = types.Real.from_mcnp(self.ebankincl)

        ebankabia = self.ebankabia
        if isinstance(self.ebankabia, types.Real):
            ebankabia = self.ebankabia
        elif isinstance(self.ebankabia, float) or isinstance(self.ebankabia, int):
            ebankabia = types.Real(self.ebankabia)
        elif isinstance(self.ebankabia, str):
            ebankabia = types.Real.from_mcnp(self.ebankabia)

        return Lcc(
            stincl=stincl,
            v0incl=v0incl,
            xfoisaincl=xfoisaincl,
            npaulincl=npaulincl,
            nosurfincl=nosurfincl,
            ecutincl=ecutincl,
            ebankincl=ebankincl,
            ebankabia=ebankabia,
        )

    @staticmethod
    def unbuild(ast: Lcc):
        """
        Unbuilds ``Lcc`` into ``LccBuilder``

        Returns:
            ``LccBuilder`` for ``Lcc``.
        """

        return Lcc(
            stincl=copy.deepcopy(ast.stincl),
            v0incl=copy.deepcopy(ast.v0incl),
            xfoisaincl=copy.deepcopy(ast.xfoisaincl),
            npaulincl=copy.deepcopy(ast.npaulincl),
            nosurfincl=copy.deepcopy(ast.nosurfincl),
            ecutincl=copy.deepcopy(ast.ecutincl),
            ebankincl=copy.deepcopy(ast.ebankincl),
            ebankabia=copy.deepcopy(ast.ebankabia),
        )
