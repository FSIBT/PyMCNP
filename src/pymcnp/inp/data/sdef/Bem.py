import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Bem(_option.SdefOption):
    """
    Represents INP bem elements.

    Attributes:
        exn: Normalized beam emittance parameter for x coordinates.
        eyn: Normalized beam emittance parameter for x coordinates.
        bml: Distance from the aperture to the spot.
    """

    _KEYWORD = 'bem'

    _ATTRS = {
        'exn': types.Real,
        'eyn': types.Real,
        'bml': types.Real,
    }

    _REGEX = re.compile(rf'\Abem( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, exn: types.Real, eyn: types.Real, bml: types.Real):
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
        if bml is None or not (bml.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bml)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                exn,
                eyn,
                bml,
            ]
        )

        self.exn: typing.Final[types.Real] = exn
        self.eyn: typing.Final[types.Real] = eyn
        self.bml: typing.Final[types.Real] = bml


@dataclasses.dataclass
class BemBuilder(_option.SdefOptionBuilder):
    """
    Builds ``Bem``.

    Attributes:
        exn: Normalized beam emittance parameter for x coordinates.
        eyn: Normalized beam emittance parameter for x coordinates.
        bml: Distance from the aperture to the spot.
    """

    exn: str | float | types.Real
    eyn: str | float | types.Real
    bml: str | float | types.Real

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
            exn = types.Real(self.exn)
        elif isinstance(self.exn, str):
            exn = types.Real.from_mcnp(self.exn)

        eyn = self.eyn
        if isinstance(self.eyn, types.Real):
            eyn = self.eyn
        elif isinstance(self.eyn, float) or isinstance(self.eyn, int):
            eyn = types.Real(self.eyn)
        elif isinstance(self.eyn, str):
            eyn = types.Real.from_mcnp(self.eyn)

        bml = self.bml
        if isinstance(self.bml, types.Real):
            bml = self.bml
        elif isinstance(self.bml, float) or isinstance(self.bml, int):
            bml = types.Real(self.bml)
        elif isinstance(self.bml, str):
            bml = types.Real.from_mcnp(self.bml)

        return Bem(
            exn=exn,
            eyn=eyn,
            bml=bml,
        )

    @staticmethod
    def unbuild(ast: Bem):
        """
        Unbuilds ``Bem`` into ``BemBuilder``

        Returns:
            ``BemBuilder`` for ``Bem``.
        """

        return BemBuilder(
            exn=copy.deepcopy(ast.exn),
            eyn=copy.deepcopy(ast.eyn),
            bml=copy.deepcopy(ast.bml),
        )
