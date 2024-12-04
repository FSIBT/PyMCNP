"""
Contains the ``Awtab`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_entry import DataEntry
from ...utils import types, errors, _parser


class AwtabEntry(DataEntry):
    """
    Represents INP awtab data card entry.

    ``AwtabEntry`` implements ``DataEntry``.

    Attributes:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.
    """

    def __init__(self, zaid: types.Zaid, weight_ratio: types.McnpReal):
        """
        Initializes ``AwtabEntry``.

        Parameters:
                zaid: Zaid alias for nuclide.
                weight_ratio: Atomic weight ratios.

        Raises:
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if weight_ratio is None or not (weight_ratio > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        self.zaid: Final[types.Zaid] = zaid
        self.weight_ratio: Final[types.McnpReal] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``AwtabEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``AwtabEntry``.

        Returns:
            ``AwtabEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        zaid = types.Zaid.from_mcnp(tokens.popl())
        weight_ratio = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return AwtabEntry(zaid, weight_ratio)

    def to_mcnp(self):
        """
        Generates INP from ``AwtabEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``AwtabEntry``.
        """

        return f'{self.zaid.to_mcnp()} {self.weight_ratio.to_mcnp()}'


class Awtab(Data):
    """
    Represents INP awtab data cards.

    ``Awtab`` implements ``Data``.

    Attributes:
        weight_ratios: Tuple of atomic weight ratios.
    """

    def __init__(self, weight_ratios: tuple[AwtabEntry]):
        """
        Initializes ``Awtab``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if weight_ratios is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weight_ratios))

        for entry in weight_ratios:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weight_ratios))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.AWTAB
        self.parameters: Final[tuple[any]] = tuple(list(weight_ratios))
        self.weight_ratios: Final[tuple[AwtabEntry]] = weight_ratios
        self.ident: Final[str] = 'awtab'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Awtab`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for awtab data cards.

        Returns:
            ``Awtab`` object.

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
        if mnemonic != 'awtab':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        weight_ratios = [
            AwtabEntry.from_mcnp(' '.join([tokens.popl() for __ in range(0, 2)]))
            for _ in range(0, len(tokens), 2)
        ]

        data = Awtab(weight_ratios)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Awtab`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Awtab``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.weight_ratios)}"
        )
