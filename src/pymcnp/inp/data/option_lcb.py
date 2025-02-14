import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Lcb(_option.DataOption_, keyword='lcb'):
    """
    Represents INP data card lcb options.

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

    _REGEX = re.compile(r'\Alcb( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        flenb1: types.Real,
        flenb2: types.Real,
        flenb3: types.Real,
        flenb4: types.Real,
        flenb5: types.Real,
        flenb6: types.Real,
        cotfe: types.Real,
        film0: types.Real,
    ):
        """
        Initializes ``DataOption_Lcb``.

        Parameters:
            flenb1: Kinetic energy for nucleons CEM/Bertini/INCL.
            flenb2: Kinetic energy for nucleons LAQGSM03.03.
            flenb3: Kinetic energy for pions CEM/Bertini/INCL.
            flenb4: Kinetic energy for pions LAQGSM03.03.
            flenb5: Kinetic energy for nucleons ISABEL.
            flenb6: Kinetic energy for appropriate model.
            cotfe: Cutoff kinetic energy for particle escape.
            film0: Maximum correction allowed for masss-energy balancing.

        Returns:
            ``DataOption_Lcb``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if flenb1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, flenb1)
        if flenb2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, flenb2)
        if flenb3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, flenb3)
        if flenb4 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, flenb4)
        if flenb5 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, flenb5)
        if flenb6 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, flenb6)
        if cotfe is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, cotfe)
        if film0 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, film0)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [flenb1, flenb2, flenb3, flenb4, flenb5, flenb6, cotfe, film0]
        )
        self.flenb1: typing.Final[types.Real] = flenb1
        self.flenb2: typing.Final[types.Real] = flenb2
        self.flenb3: typing.Final[types.Real] = flenb3
        self.flenb4: typing.Final[types.Real] = flenb4
        self.flenb5: typing.Final[types.Real] = flenb5
        self.flenb6: typing.Final[types.Real] = flenb6
        self.cotfe: typing.Final[types.Real] = cotfe
        self.film0: typing.Final[types.Real] = film0

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Lcb`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Lcb``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Lcb._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        flenb1 = types.Real.from_mcnp(tokens[1])
        flenb2 = types.Real.from_mcnp(tokens[2])
        flenb3 = types.Real.from_mcnp(tokens[3])
        flenb4 = types.Real.from_mcnp(tokens[4])
        flenb5 = types.Real.from_mcnp(tokens[5])
        flenb6 = types.Real.from_mcnp(tokens[6])
        cotfe = types.Real.from_mcnp(tokens[7])
        film0 = types.Real.from_mcnp(tokens[8])

        return DataOption_Lcb(flenb1, flenb2, flenb3, flenb4, flenb5, flenb6, cotfe, film0)
