import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SdefOption_Bem(_option.SdefOption_, keyword='bem'):
    """
    Represents INP data card data option bem options.

    Attributes:
        exn: Normalized beam emittance parameter for x coordinates.
        eyn: Normalized beam emittance parameter for x coordinates.
        bml: Distance from the aperture to the spot.
    """

    _REGEX = re.compile(r'\Abem( \S+)( \S+)( \S+)\Z')

    def __init__(self, exn: types.Real, eyn: types.Real, bml: types.Real):
        """
        Initializes ``SdefOption_Bem``.

        Parameters:
            exn: Normalized beam emittance parameter for x coordinates.
            eyn: Normalized beam emittance parameter for x coordinates.
            bml: Distance from the aperture to the spot.

        Returns:
            ``SdefOption_Bem``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if exn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, exn)
        if eyn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, eyn)
        if bml is None or not (bml >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bml)

        self.value: typing.Final[tuple[any]] = types._Tuple([exn, eyn, bml])
        self.exn: typing.Final[types.Real] = exn
        self.eyn: typing.Final[types.Real] = eyn
        self.bml: typing.Final[types.Real] = bml

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefOption_Bem`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SdefOption_Bem``.

        Raises:
            InpError: SYNTAX_SDEF_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SdefOption_Bem._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        exn = types.Real.from_mcnp(tokens[1])
        eyn = types.Real.from_mcnp(tokens[2])
        bml = types.Real.from_mcnp(tokens[3])

        return SdefOption_Bem(exn, eyn, bml)
