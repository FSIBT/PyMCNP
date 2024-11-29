"""
Contains the ``Ksrc`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_entry import DataEntry
from ...utils import types, errors, _parser


class KsrcEntry(DataEntry):
    """
    Represents INP ksrc data card entry.

    ``KsrcEntry`` implements ``DataEntry``.

    Attributes:
            x: Location x-coordinate.
            y: Location y-coordinate.
            z: Location z-coordinate.
    """

    def __init__(self, x: types.McnpReal, y: types.McnpReal, z: types.McnpReal):
        """
        Initializes ``KsrcEntry``.

        Parameters:
                x: Location x-coordinate.
                y: Location y-coordinate.
                z: Location z-coordinate.

        Raises:
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        self.x: Final[types.McnpReal] = x
        self.y: Final[types.McnpReal] = y
        self.z: Final[types.McnpReal] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsrcEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``KsrcEntry``.

        Returns:
            ``KsrcEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        x = types.McnpReal.from_mcnp(tokens.popl())
        y = types.McnpReal.from_mcnp(tokens.popl())
        z = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return KsrcEntry(x, y, z)

    def to_mcnp(self):
        """
        Generates INP from ``KsrcEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``KsrcEntry``.
        """

        return f'{self.x.to_mcnp()} {self.y.to_mcnp()} {self.z.to_mcnp()}'


class Ksrc(Data):
    """
    Represents INP ksrc data cards.

    ``Ksrc`` implements ``Data``.

    Attributes:
        locations: Tuple of inital source points.
    """

    def __init__(self, locations: tuple[KsrcEntry]):
        """
        Initializes ``Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if locations is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(locations))

        for entry in locations:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(locations))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.KSRC
        self.parameters: Final[tuple[any]] = tuple(list(locations))
        self.locations: Final[tuple[KsrcEntry]] = locations
        self.ident: Final[str] = 'ksrc'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ksrc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ksrc data cards.

        Returns:
            ``Ksrc`` object.

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
        if mnemonic != 'ksrc':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        locations = [
            KsrcEntry.from_mcnp(' '.join([tokens.popl() for __ in range(0, 3)]))
            for _ in range(0, len(tokens), 3)
        ]

        data = Ksrc(locations)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Ksrc`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Ksrc``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.locations)}"
        )
