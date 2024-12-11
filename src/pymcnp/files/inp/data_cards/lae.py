"""
Contains the ``Lae`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Lae(Data):
    """
    Represents INP lae data cards.

    ``Lae`` implements ``Data``.

    Attributes:
        ipht: Generation of de-excitation photons setting.
        icc: Level of physics for PHT physics setting.
        nobalc: Mass-energy balancing in cascade setting.
        nobale: Mass-energy balancing in evaporation setting.
        ifbrk: Mass-energy balancing in Fermi-breakup setting.
        ilvden: Level-density model setting.
        ievap: Evaporation and fission model setting.
        nofis: Fission setting.
    """

    def __init__(
        self,
        ipht: types.McnpInteger,
        icc: types.McnpInteger,
        nobalc: types.McnpInteger,
        nobale: types.McnpInteger,
        ifbrk: types.McnpInteger,
        ilvden: types.McnpInteger,
        ievap: types.McnpInteger,
        nofis: types.McnpInteger,
    ):
        """
        Initializes ``Lae``.

        Parameters:
            ipht: Generation of de-excitation photons setting.
            icc: Level of physics for PHT physics setting.
            nobalc: Mass-energy balancing in cascade setting.
            nobale: Mass-energy balancing in evaporation setting.
            ifbrk: Mass-energy balancing in Fermi-breakup setting.
            ilvden: Level-density model setting.
            ievap: Evaporation and fission model setting.
            nofis: Fission setting.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if ipht is None or ipht.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ipht))

        if icc is None or icc.value not in {0, 1, 2, 3, 4}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(icc))

        if nobalc is None or nobalc.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nobalc))

        if nobale is None or nobale.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nobale))

        if ifbrk is None or ifbrk.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ifbrk))

        if ilvden is None or ilvden.value not in {0, 1, -1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ilvden))

        if ievap is None or ievap.value not in {0, 1, -1, 2}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(ievap))

        if nofis is None or nofis.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nofis))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.LAE
        self.parameters: Final[tuple[any]] = tuple(
            [ipht] + [icc] + [nobalc] + [nobale] + [ifbrk] + [ilvden] + [ievap] + [nofis]
        )
        self.ipht: Final[types.McnpInteger] = ipht
        self.icc: Final[types.McnpInteger] = icc
        self.nobalc: Final[types.McnpInteger] = nobalc
        self.nobale: Final[types.McnpInteger] = nobale
        self.ifbrk: Final[types.McnpInteger] = ifbrk
        self.ilvden: Final[types.McnpInteger] = ilvden
        self.ievap: Final[types.McnpInteger] = ievap
        self.nofis: Final[types.McnpInteger] = nofis
        self.ident: Final[str] = 'lae'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Lae`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for lae data cards.

        Returns:
            ``Lae`` object.

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
        if mnemonic != 'lae':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        ipht = types.McnpInteger.from_mcnp(tokens.popl())
        icc = types.McnpInteger.from_mcnp(tokens.popl())
        nobalc = types.McnpInteger.from_mcnp(tokens.popl())
        nobale = types.McnpInteger.from_mcnp(tokens.popl())
        ifbrk = types.McnpInteger.from_mcnp(tokens.popl())
        ilvden = types.McnpInteger.from_mcnp(tokens.popl())
        ievap = types.McnpInteger.from_mcnp(tokens.popl())
        nofis = types.McnpInteger.from_mcnp(tokens.popl())

        data = Lae(ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Lae`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Lae``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.ipht.to_mcnp()} {self.icc.to_mcnp()} {self.nobalc.to_mcnp()} {self.nobale.to_mcnp()} {self.ifbrk.to_mcnp()} {self.ilvden.to_mcnp()} {self.ievap.to_mcnp()} {self.nofis.to_mcnp()}'
        )
