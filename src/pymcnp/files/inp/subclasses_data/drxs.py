"""
Contains the ``Drxs`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Drxs(Data):
    """
    Represents INP drxs data cards.

    ``Drxs`` implements ``Data``.

    Attributes:
        zaids: Tuple of ZAID aliases.
    """

    def __init__(self, zaids: tuple[types.Zaid]):
        """
        Initializes ``Drxs``.

        Parameters:
            zaids: Tuple of ZAID aliases.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if zaids is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(zaids))

        for entry in zaids:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(zaids))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.DRXS
        self.parameters: Final[tuple[any]] = tuple(list(zaids))
        self.zaids: Final[tuple[types.Zaid]] = zaids
        self.ident: Final[str] = 'drxs'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Drxs`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for drxs data cards.

        Returns:
            ``Drxs`` object.

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
        if mnemonic != 'drxs':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        zaids = [types.Zaid.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Drxs(zaids)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Drxs`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Drxs``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.zaids)}"
        )
