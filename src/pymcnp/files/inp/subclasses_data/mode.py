"""
Contains the ``Mode`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Mode(Data):
    """
    Represents INP mode data cards.

    ``Mode`` implements ``Data``.

    Attributes:
        particles: Tuple of particle designators.
    """

    def __init__(self, particles: tuple[types.Designator]):
        """
        Initializes ``Mode``.

        Parameters:
            particles: Tuple of particle designators.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(particles))

        for entry in particles:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(particles))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.MODE
        self.parameters: Final[tuple[any]] = tuple(list(particles))
        self.particles: Final[tuple[types.Designator]] = particles
        self.ident: Final[str] = 'mode'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mode`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for mode data cards.

        Returns:
            ``Mode`` object.

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
        if mnemonic != 'mode':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        particles = [types.Designator.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Mode(particles)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Mode`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Mode``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.particles)}"
        )
