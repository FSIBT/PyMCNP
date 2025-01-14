"""
Contains the ``Wwp`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Wwp(Data):
    """
    Represents INP wwp data cards.

    ``Wwp`` implements ``Data``.

    Attributes:
        wupn: Multiplier to define the weight window upper limit.
        wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.
        mxspln: Maximum number of integer splits.
        mwhere: Controls where to check a particle’s weight.
        switchn: Controls where to get the lower weight-window bounds.
        mtime: Energy/time-dependent window setting.
        wnrom: Weight-window normalization factor.
        etsplt: ESLPT & TSPLT split/roulette on/off.
        wu: Limits the maximum lower weight-window bound for any particle, energy, or time.
        nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.
        designator: Data card particle designator.
    """

    def __init__(
        self,
        wupn: types.McnpReal,
        wsurvn: types.McnpReal,
        mxspln: types.McnpReal,
        mwhere: types.McnpInteger,
        switchn: types.McnpReal,
        mtime: types.McnpInteger,
        wnrom: types.McnpReal,
        etsplt: types.McnpInteger,
        wu: types.McnpReal,
        nmfp: types.McnpReal,
        designator: types.Designator,
    ):
        """
        Initializes ``Wwp``.

        Parameters:
            wupn: Multiplier to define the weight window upper limit.
            wsurvn: Multiplier to define the maximum Russian roulette survival weight within the window.
            mxspln: Maximum number of integer splits.
            mwhere: Controls where to check a particle’s weight.
            switchn: Controls where to get the lower weight-window bounds.
            mtime: Energy/time-dependent window setting.
            wnrom: Weight-window normalization factor.
            etsplt: ESLPT & TSPLT split/roulette on/off.
            wu: Limits the maximum lower weight-window bound for any particle, energy, or time.
            nmfp: Limits the maximum lower weight-window bound for any particle, energy, or time.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if wupn is None or not (wupn >= 2):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(wupn))

        if wsurvn is None or not (1 < wsurvn):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(wsurvn))

        if mxspln is None or not (1 < mxspln):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(mxspln))

        if mwhere is None or mwhere.value not in {-1, 0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(mwhere))

        if switchn is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(switchn))

        if mtime is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(mtime))

        if wnrom is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(wnrom))

        if etsplt is None or etsplt.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(etsplt))

        if wu is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(wu))

        if nmfp is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(nmfp))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.WWP
        self.parameters: Final[tuple[any]] = tuple(
            [wupn]
            + [wsurvn]
            + [mxspln]
            + [mwhere]
            + [switchn]
            + [mtime]
            + [wnrom]
            + [etsplt]
            + [wu]
            + [nmfp]
            + [designator]
        )
        self.wupn: Final[types.McnpReal] = wupn
        self.wsurvn: Final[types.McnpReal] = wsurvn
        self.mxspln: Final[types.McnpReal] = mxspln
        self.mwhere: Final[types.McnpInteger] = mwhere
        self.switchn: Final[types.McnpReal] = switchn
        self.mtime: Final[types.McnpInteger] = mtime
        self.wnrom: Final[types.McnpReal] = wnrom
        self.etsplt: Final[types.McnpInteger] = etsplt
        self.wu: Final[types.McnpReal] = wu
        self.nmfp: Final[types.McnpReal] = nmfp
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'wwp:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Wwp`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for wwp data cards.

        Returns:
            ``Wwp`` object.

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
        if mnemonic != 'wwp':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        tokens.popl()

        wupn = types.McnpReal.from_mcnp(tokens.popl())
        wsurvn = types.McnpReal.from_mcnp(tokens.popl())
        mxspln = types.McnpReal.from_mcnp(tokens.popl())
        mwhere = types.McnpInteger.from_mcnp(tokens.popl())
        switchn = types.McnpReal.from_mcnp(tokens.popl())
        mtime = types.McnpInteger.from_mcnp(tokens.popl())
        wnrom = types.McnpReal.from_mcnp(tokens.popl())
        etsplt = types.McnpInteger.from_mcnp(tokens.popl())
        wu = types.McnpReal.from_mcnp(tokens.popl())
        nmfp = types.McnpReal.from_mcnp(tokens.popl())

        data = Wwp(
            wupn, wsurvn, mxspln, mwhere, switchn, mtime, wnrom, etsplt, wu, nmfp, designator
        )
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Wwp`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Wwp``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()} {self.wupn.to_mcnp()} {self.wsurvn.to_mcnp()} {self.mxspln.to_mcnp()} {self.mwhere.to_mcnp()} {self.switchn.to_mcnp()} {self.mtime.to_mcnp()} {self.wnrom.to_mcnp()} {self.etsplt.to_mcnp()} {self.wu.to_mcnp()} {self.nmfp.to_mcnp()}'
        )
