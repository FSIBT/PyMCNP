"""
Contains the ``Xs`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataEntry
from ....utils import types, errors, _parser


class XsEntry(DataEntry):
    """
    Represents INP xs data card entry.

    ``XsEntry`` implements ``DataEntry``.

    Attributes:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.
    """

    def __init__(self, zaid: types.Zaid, weight_ratio: types.McnpReal):
        """
        Initializes ``XsEntry``.

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
        Generates ``XsEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``XsEntry``.

        Returns:
            ``XsEntry`` object.

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

        return XsEntry(zaid, weight_ratio)

    def to_mcnp(self):
        """
        Generates INP from ``XsEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``XsEntry``.
        """

        return f'{self.zaid.to_mcnp()} {self.weight_ratio.to_mcnp()}'


class Xs(Data):
    """
    Represents INP xs data cards.

    ``Xs`` implements ``Data``.

    Attributes:
        weight_ratios: Tuple of atomic weight ratios.
        suffix: Data card suffix..
    """

    def __init__(self, weight_ratios: tuple[XsEntry], suffix: types.McnpInteger):
        """
        Initializes ``Xs``.

        Parameters:
            weight_ratios: Tuple of atomic weight ratios.
            suffix: Data card suffix..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if weight_ratios is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weight_ratios))

        for entry in weight_ratios:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weight_ratios))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.XS
        self.parameters: Final[tuple[any]] = tuple(list(weight_ratios) + [suffix])
        self.weight_ratios: Final[tuple[XsEntry]] = weight_ratios
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'xs{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Xs`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for xs data cards.

        Returns:
            ``Xs`` object.

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
        if mnemonic != 'xs':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        weight_ratios = [
            XsEntry.from_mcnp(' '.join([tokens.popl() for __ in range(0, 2)]))
            for _ in range(0, len(tokens), 2)
        ]
        suffix = types.McnpInteger.from_mcnp(tokens.popl())

        data = Xs(weight_ratios, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Xs`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Xs``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.weight_ratios)} {self.suffix.to_mcnp()}"
        )
