"""
Contains the ``Lcb`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types, errors, _parser


class Lcb(Data):
    """
    Represents INP lcb data cards.

    ``Lcb`` implements ``Data``.

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

    def __init__(
        self,
        flenb1: types.McnpReal,
        flenb2: types.McnpReal,
        flenb3: types.McnpReal,
        flenb4: types.McnpReal,
        flenb5: types.McnpReal,
        flenb6: types.McnpReal,
        cotfe: types.McnpReal,
        film0: types.McnpReal,
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
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if flenb1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(flenb1))

        if flenb2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(flenb2))

        if flenb3 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(flenb3))

        if flenb4 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(flenb4))

        if flenb5 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(flenb5))

        if flenb6 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(flenb6))

        if cotfe is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(cotfe))

        if film0 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(film0))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LCB
        self.parameters: Final[tuple[any]] = tuple(
            [flenb1] + [flenb2] + [flenb3] + [flenb4] + [flenb5] + [flenb6] + [cotfe] + [film0]
        )
        self.flenb1: Final[types.McnpReal] = flenb1
        self.flenb2: Final[types.McnpReal] = flenb2
        self.flenb3: Final[types.McnpReal] = flenb3
        self.flenb4: Final[types.McnpReal] = flenb4
        self.flenb5: Final[types.McnpReal] = flenb5
        self.flenb6: Final[types.McnpReal] = flenb6
        self.cotfe: Final[types.McnpReal] = cotfe
        self.film0: Final[types.McnpReal] = film0
        self.ident: Final[str] = 'lcb'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lcb`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for lcb data cards.

        Returns:
            ``Lcb`` object.

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
        if mnemonic != 'lcb':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        flenb1 = types.McnpReal.from_mcnp(tokens.popl())
        flenb2 = types.McnpReal.from_mcnp(tokens.popl())
        flenb3 = types.McnpReal.from_mcnp(tokens.popl())
        flenb4 = types.McnpReal.from_mcnp(tokens.popl())
        flenb5 = types.McnpReal.from_mcnp(tokens.popl())
        flenb6 = types.McnpReal.from_mcnp(tokens.popl())
        cotfe = types.McnpReal.from_mcnp(tokens.popl())
        film0 = types.McnpReal.from_mcnp(tokens.popl())

        data = Lcb(flenb1, flenb2, flenb3, flenb4, flenb5, flenb6, cotfe, film0)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Lcb`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Lcb``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.flenb1.to_mcnp()} {self.flenb2.to_mcnp()} {self.flenb3.to_mcnp()} {self.flenb4.to_mcnp()} {self.flenb5.to_mcnp()} {self.flenb6.to_mcnp()} {self.cotfe.to_mcnp()} {self.film0.to_mcnp()}'
        )
