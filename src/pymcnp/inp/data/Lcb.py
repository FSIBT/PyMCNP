import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lcb(DataOption_, keyword='lcb'):
    """
    Represents INP lcb elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if flenb1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, flenb1)
        if flenb2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, flenb2)
        if flenb3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, flenb3)
        if flenb4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, flenb4)
        if flenb5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, flenb5)
        if flenb6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, flenb6)
        if cotfe is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cotfe)
        if film0 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, film0)

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
