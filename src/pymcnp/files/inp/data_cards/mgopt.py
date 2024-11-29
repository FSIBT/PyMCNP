"""
Contains the ``Mgopt`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types, errors, _parser


class Mgopt(Data):
    """
    Represents INP mgopt data cards.

    ``Mgopt`` implements ``Data``.

    Attributes:
        mcal: Problem type setting.
        igm: Total number of energy groups for all kinds of particle.
        iplt: Weight windows usage indicator.
        iab: Adjoint biasing for adjoint problems contorls.
        icw: Name of the reference cell for generated weight windows.
        fnw: Normalization value for generated weight windows.
        rim: Generated weight windows compression limit.
    """

    def __init__(
        self,
        mcal: str,
        igm: types.McnpInteger,
        iplt: types.McnpInteger,
        iab: types.McnpInteger,
        icw: types.McnpInteger,
        fnw: types.McnpReal,
        rim: types.McnpReal,
    ):
        """
        Initializes ``Mgopt``.

        Parameters:
            mcal: Problem type setting.
            igm: Total number of energy groups for all kinds of particle.
            iplt: Weight windows usage indicator.
            iab: Adjoint biasing for adjoint problems contorls.
            icw: Name of the reference cell for generated weight windows.
            fnw: Normalization value for generated weight windows.
            rim: Generated weight windows compression limit.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if mcal is None or mcal.value not in {'f', 'a'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(mcal))

        if igm is None or not (igm >= 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(igm))

        if iplt is None or not (iplt == 0 or iplt == 1 or iplt == 2):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(iplt))

        if iab is None or not (iab == 0 or iab == 1 or iab == 2):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(iab))

        if icw is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(icw))

        if fnw is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(fnw))

        if rim is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(rim))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.MGOPT
        self.parameters: Final[tuple[any]] = tuple(
            [mcal] + [igm] + [iplt] + [iab] + [icw] + [fnw] + [rim]
        )
        self.mcal: Final[str] = mcal
        self.igm: Final[types.McnpInteger] = igm
        self.iplt: Final[types.McnpInteger] = iplt
        self.iab: Final[types.McnpInteger] = iab
        self.icw: Final[types.McnpInteger] = icw
        self.fnw: Final[types.McnpReal] = fnw
        self.rim: Final[types.McnpReal] = rim
        self.ident: Final[str] = 'mgopt'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mgopt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for mgopt data cards.

        Returns:
            ``Mgopt`` object.

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
        if mnemonic != 'mgopt':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        mcal = tokens.popl()
        igm = types.McnpInteger.from_mcnp(tokens.popl())
        iplt = types.McnpInteger.from_mcnp(tokens.popl())
        iab = types.McnpInteger.from_mcnp(tokens.popl())
        icw = types.McnpInteger.from_mcnp(tokens.popl())
        fnw = types.McnpReal.from_mcnp(tokens.popl())
        rim = types.McnpReal.from_mcnp(tokens.popl())

        data = Mgopt(mcal, igm, iplt, iab, icw, fnw, rim)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Mgopt`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Mgopt``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.mcal.to_mcnp()} {self.igm.to_mcnp()} {self.iplt.to_mcnp()} {self.iab.to_mcnp()} {self.icw.to_mcnp()} {self.fnw.to_mcnp()} {self.rim.to_mcnp()}'
        )
