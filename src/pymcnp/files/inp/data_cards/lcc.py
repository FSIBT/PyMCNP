"""
Contains the ``Lcc`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Lcc(Data):
    """
    Represents INP lcc data cards.

    ``Lcc`` implements ``Data``.

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

    def __init__(
        self,
        stincl: types.McnpReal,
        v0incl: types.McnpReal,
        xfoisaincl: types.McnpReal,
        npaulincl: types.McnpInteger,
        nosurfincl: types.McnpInteger,
        ecutincl: types.McnpReal,
        ebankincl: types.McnpReal,
        ebankabia: types.McnpReal,
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
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if stincl is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(stincl))

        if v0incl is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(v0incl))

        if xfoisaincl is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(xfoisaincl))

        if npaulincl is None or not (npaulincl == 0 or npaulincl == -1 or npaulincl == 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(npaulincl))

        if nosurfincl is None or not (
            xfoisaincl == -2 or xfoisaincl == -1 or xfoisaincl == 0 or xfoisaincl == 1
        ):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nosurfincl))

        if ecutincl is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ecutincl))

        if ebankincl is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ebankincl))

        if ebankabia is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ebankabia))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LCC
        self.parameters: Final[tuple[any]] = tuple(
            [stincl]
            + [v0incl]
            + [xfoisaincl]
            + [npaulincl]
            + [nosurfincl]
            + [ecutincl]
            + [ebankincl]
            + [ebankabia]
        )
        self.stincl: Final[types.McnpReal] = stincl
        self.v0incl: Final[types.McnpReal] = v0incl
        self.xfoisaincl: Final[types.McnpReal] = xfoisaincl
        self.npaulincl: Final[types.McnpInteger] = npaulincl
        self.nosurfincl: Final[types.McnpInteger] = nosurfincl
        self.ecutincl: Final[types.McnpReal] = ecutincl
        self.ebankincl: Final[types.McnpReal] = ebankincl
        self.ebankabia: Final[types.McnpReal] = ebankabia
        self.ident: Final[str] = 'lcc'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lcc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for lcc data cards.

        Returns:
            ``Lcc`` object.

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
        if mnemonic != 'lcc':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        stincl = types.McnpReal.from_mcnp(tokens.popl())
        v0incl = types.McnpReal.from_mcnp(tokens.popl())
        xfoisaincl = types.McnpReal.from_mcnp(tokens.popl())
        npaulincl = types.McnpInteger.from_mcnp(tokens.popl())
        nosurfincl = types.McnpInteger.from_mcnp(tokens.popl())
        ecutincl = types.McnpReal.from_mcnp(tokens.popl())
        ebankincl = types.McnpReal.from_mcnp(tokens.popl())
        ebankabia = types.McnpReal.from_mcnp(tokens.popl())

        data = Lcc(
            stincl, v0incl, xfoisaincl, npaulincl, nosurfincl, ecutincl, ebankincl, ebankabia
        )
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Lcc`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Lcc``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.stincl.to_mcnp()} {self.v0incl.to_mcnp()} {self.xfoisaincl.to_mcnp()} {self.npaulincl.to_mcnp()} {self.nosurfincl.to_mcnp()} {self.ecutincl.to_mcnp()} {self.ebankincl.to_mcnp()} {self.ebankabia.to_mcnp()}'
        )
