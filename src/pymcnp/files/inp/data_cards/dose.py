"""
Contains the ``Dose`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Dose(Data):
    """
    Represents INP dose data cards.

    ``Dose`` implements ``Data``.

    Attributes:
        ic: Conversion coefficent.
        int: Interpolation method.
        iu: Units of resuts.
        fac: Normalization of factor for dose.
    """

    def __init__(
        self,
        ic: types.McnpInteger,
        int: types.McnpInteger,
        iu: types.McnpInteger,
        fac: types.McnpReal,
    ):
        """
        Initializes ``Dose``.

        Parameters:
            ic: Conversion coefficent.
            int: Interpolation method.
            iu: Units of resuts.
            fac: Normalization of factor for dose.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if ic is None or ic.value not in {10, 20, 31, 32, 33, 34, 35, 40, 99}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ic))

        if int is None or int.value not in {1, 2, 3}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(int))

        if iu is None or ic.value not in {1, 2}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(iu))

        if fac is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(fac))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.DOSE
        self.parameters: Final[tuple[any]] = tuple([ic] + [int] + [iu] + [fac])
        self.ic: Final[types.McnpInteger] = ic
        self.int: Final[types.McnpInteger] = int
        self.iu: Final[types.McnpInteger] = iu
        self.fac: Final[types.McnpReal] = fac
        self.ident: Final[str] = 'dose'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dose`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for dose data cards.

        Returns:
            ``Dose`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |:|=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        mnemonic = mnemonic[0] if mnemonic else ''
        if mnemonic != 'dose':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        ic = types.McnpInteger.from_mcnp(tokens.popl())
        int = types.McnpInteger.from_mcnp(tokens.popl())
        iu = types.McnpInteger.from_mcnp(tokens.popl())
        fac = types.McnpReal.from_mcnp(tokens.popl())

        data = Dose(ic, int, iu, fac)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Dose`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Dose``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.ic.to_mcnp()} {self.int.to_mcnp()} {self.iu.to_mcnp()} {self.fac.to_mcnp()}'
        )
