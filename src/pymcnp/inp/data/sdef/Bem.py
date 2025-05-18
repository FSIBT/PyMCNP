import re
import typing
import dataclasses


from ._option import SdefOption
from ....utils import types
from ....utils import errors


class Bem(SdefOption):
    """
    Represents INP bem elements.

    Attributes:
        exn: Normalized beam emittance parameter for x coordinates.
        eyn: Normalized beam emittance parameter for x coordinates.
        bml: Distance from the aperture to the spot.
    """

    _ATTRS = {
        'exn': types.RealOrJump,
        'eyn': types.RealOrJump,
        'bml': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Abem( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, exn: types.RealOrJump, eyn: types.RealOrJump, bml: types.RealOrJump):
        """
        Initializes ``Bem``.

        Parameters:
            exn: Normalized beam emittance parameter for x coordinates.
            eyn: Normalized beam emittance parameter for x coordinates.
            bml: Distance from the aperture to the spot.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if exn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, exn)
        if eyn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, eyn)
        if bml is None or not (bml >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bml)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                exn,
                eyn,
                bml,
            ]
        )

        self.exn: typing.Final[types.RealOrJump] = exn
        self.eyn: typing.Final[types.RealOrJump] = eyn
        self.bml: typing.Final[types.RealOrJump] = bml


@dataclasses.dataclass
class BemBuilder:
    """
    Builds ``Bem``.

    Attributes:
        exn: Normalized beam emittance parameter for x coordinates.
        eyn: Normalized beam emittance parameter for x coordinates.
        bml: Distance from the aperture to the spot.
    """

    exn: str | float | types.RealOrJump
    eyn: str | float | types.RealOrJump
    bml: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``BemBuilder`` into ``Bem``.

        Returns:
            ``Bem`` for ``BemBuilder``.
        """

        exn = self.exn
        if isinstance(self.exn, types.Real):
            exn = self.exn
        elif isinstance(self.exn, float) or isinstance(self.exn, int):
            exn = types.RealOrJump(self.exn)
        elif isinstance(self.exn, str):
            exn = types.RealOrJump.from_mcnp(self.exn)

        eyn = self.eyn
        if isinstance(self.eyn, types.Real):
            eyn = self.eyn
        elif isinstance(self.eyn, float) or isinstance(self.eyn, int):
            eyn = types.RealOrJump(self.eyn)
        elif isinstance(self.eyn, str):
            eyn = types.RealOrJump.from_mcnp(self.eyn)

        bml = self.bml
        if isinstance(self.bml, types.Real):
            bml = self.bml
        elif isinstance(self.bml, float) or isinstance(self.bml, int):
            bml = types.RealOrJump(self.bml)
        elif isinstance(self.bml, str):
            bml = types.RealOrJump.from_mcnp(self.bml)

        return Bem(
            exn=exn,
            eyn=eyn,
            bml=bml,
        )
