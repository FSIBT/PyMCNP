import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Lcb(DataOption):
    """
    Represents INP lcb elements.

    Attributes:
        flenb1: Kinetic energy for nucleons CEM/Bertini/INCL.
        flenb2: Kinetic energy for nucleons LAQGSM03.03.
        flenb3: Kinetic energy for pions CEM/Bertini/INCL.
        flenb4: Kinetic energy for pions LAQGSM03.03.
        flenb5: Kinetic energy for nucleons ISABEL.
        flenb6: Kinetic energy for appropriate model.
        cotfe: Cutoff kinetic energy for particle escape.
        film0: Maximum correction allowed for masss-energy balancing.
    """

    _ATTRS = {
        'flenb1': types.RealOrJump,
        'flenb2': types.RealOrJump,
        'flenb3': types.RealOrJump,
        'flenb4': types.RealOrJump,
        'flenb5': types.RealOrJump,
        'flenb6': types.RealOrJump,
        'cotfe': types.RealOrJump,
        'film0': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Alcb( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        flenb1: types.RealOrJump,
        flenb2: types.RealOrJump,
        flenb3: types.RealOrJump,
        flenb4: types.RealOrJump,
        flenb5: types.RealOrJump,
        flenb6: types.RealOrJump,
        cotfe: types.RealOrJump,
        film0: types.RealOrJump,
    ):
        """
        Initializes ``Lcb``.

        Parameters:
            flenb1: Kinetic energy for nucleons CEM/Bertini/INCL.
            flenb2: Kinetic energy for nucleons LAQGSM03.03.
            flenb3: Kinetic energy for pions CEM/Bertini/INCL.
            flenb4: Kinetic energy for pions LAQGSM03.03.
            flenb5: Kinetic energy for nucleons ISABEL.
            flenb6: Kinetic energy for appropriate model.
            cotfe: Cutoff kinetic energy for particle escape.
            film0: Maximum correction allowed for masss-energy balancing.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if flenb1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, flenb1)
        if flenb2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, flenb2)
        if flenb3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, flenb3)
        if flenb4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, flenb4)
        if flenb5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, flenb5)
        if flenb6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, flenb6)
        if cotfe is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cotfe)
        if film0 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, film0)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                flenb1,
                flenb2,
                flenb3,
                flenb4,
                flenb5,
                flenb6,
                cotfe,
                film0,
            ]
        )

        self.flenb1: typing.Final[types.RealOrJump] = flenb1
        self.flenb2: typing.Final[types.RealOrJump] = flenb2
        self.flenb3: typing.Final[types.RealOrJump] = flenb3
        self.flenb4: typing.Final[types.RealOrJump] = flenb4
        self.flenb5: typing.Final[types.RealOrJump] = flenb5
        self.flenb6: typing.Final[types.RealOrJump] = flenb6
        self.cotfe: typing.Final[types.RealOrJump] = cotfe
        self.film0: typing.Final[types.RealOrJump] = film0


@dataclasses.dataclass
class LcbBuilder:
    """
    Builds ``Lcb``.

    Attributes:
        flenb1: Kinetic energy for nucleons CEM/Bertini/INCL.
        flenb2: Kinetic energy for nucleons LAQGSM03.03.
        flenb3: Kinetic energy for pions CEM/Bertini/INCL.
        flenb4: Kinetic energy for pions LAQGSM03.03.
        flenb5: Kinetic energy for nucleons ISABEL.
        flenb6: Kinetic energy for appropriate model.
        cotfe: Cutoff kinetic energy for particle escape.
        film0: Maximum correction allowed for masss-energy balancing.
    """

    flenb1: str | float | types.RealOrJump
    flenb2: str | float | types.RealOrJump
    flenb3: str | float | types.RealOrJump
    flenb4: str | float | types.RealOrJump
    flenb5: str | float | types.RealOrJump
    flenb6: str | float | types.RealOrJump
    cotfe: str | float | types.RealOrJump
    film0: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``LcbBuilder`` into ``Lcb``.

        Returns:
            ``Lcb`` for ``LcbBuilder``.
        """

        if isinstance(self.flenb1, types.Real):
            flenb1 = self.flenb1
        elif isinstance(self.flenb1, float) or isinstance(self.flenb1, int):
            flenb1 = types.RealOrJump(self.flenb1)
        elif isinstance(self.flenb1, str):
            flenb1 = types.RealOrJump.from_mcnp(self.flenb1)

        if isinstance(self.flenb2, types.Real):
            flenb2 = self.flenb2
        elif isinstance(self.flenb2, float) or isinstance(self.flenb2, int):
            flenb2 = types.RealOrJump(self.flenb2)
        elif isinstance(self.flenb2, str):
            flenb2 = types.RealOrJump.from_mcnp(self.flenb2)

        if isinstance(self.flenb3, types.Real):
            flenb3 = self.flenb3
        elif isinstance(self.flenb3, float) or isinstance(self.flenb3, int):
            flenb3 = types.RealOrJump(self.flenb3)
        elif isinstance(self.flenb3, str):
            flenb3 = types.RealOrJump.from_mcnp(self.flenb3)

        if isinstance(self.flenb4, types.Real):
            flenb4 = self.flenb4
        elif isinstance(self.flenb4, float) or isinstance(self.flenb4, int):
            flenb4 = types.RealOrJump(self.flenb4)
        elif isinstance(self.flenb4, str):
            flenb4 = types.RealOrJump.from_mcnp(self.flenb4)

        if isinstance(self.flenb5, types.Real):
            flenb5 = self.flenb5
        elif isinstance(self.flenb5, float) or isinstance(self.flenb5, int):
            flenb5 = types.RealOrJump(self.flenb5)
        elif isinstance(self.flenb5, str):
            flenb5 = types.RealOrJump.from_mcnp(self.flenb5)

        if isinstance(self.flenb6, types.Real):
            flenb6 = self.flenb6
        elif isinstance(self.flenb6, float) or isinstance(self.flenb6, int):
            flenb6 = types.RealOrJump(self.flenb6)
        elif isinstance(self.flenb6, str):
            flenb6 = types.RealOrJump.from_mcnp(self.flenb6)

        if isinstance(self.cotfe, types.Real):
            cotfe = self.cotfe
        elif isinstance(self.cotfe, float) or isinstance(self.cotfe, int):
            cotfe = types.RealOrJump(self.cotfe)
        elif isinstance(self.cotfe, str):
            cotfe = types.RealOrJump.from_mcnp(self.cotfe)

        if isinstance(self.film0, types.Real):
            film0 = self.film0
        elif isinstance(self.film0, float) or isinstance(self.film0, int):
            film0 = types.RealOrJump(self.film0)
        elif isinstance(self.film0, str):
            film0 = types.RealOrJump.from_mcnp(self.film0)

        return Lcb(
            flenb1=flenb1,
            flenb2=flenb2,
            flenb3=flenb3,
            flenb4=flenb4,
            flenb5=flenb5,
            flenb6=flenb6,
            cotfe=cotfe,
            film0=film0,
        )
