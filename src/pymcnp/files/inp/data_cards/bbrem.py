"""
Contains the ``Bbrem`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Bbrem(Data):
    """
    Represents INP bbrem data cards.

    ``Bbrem`` implements ``Data``.

    Attributes:
        biases: Bias factors for the bremsstrahlung.
        materials: Material to bias.
    """

    def __init__(self, biases: tuple[types.McnpReal], materials: tuple[types.McnpInteger]):
        """
        Initializes ``Bbrem``.

        Parameters:
            biases: Bias factors for the bremsstrahlung.
            materials: Material to bias.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if biases is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(biases))

        for entry in biases:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(biases))

        if materials is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(materials))

        for entry in materials:
            if entry is None or not (0 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(materials))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.BBREM
        self.parameters: Final[tuple[any]] = tuple(list(biases) + list(materials))
        self.biases: Final[tuple[types.McnpReal]] = biases
        self.materials: Final[tuple[types.McnpInteger]] = materials
        self.ident: Final[str] = 'bbrem'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Bbrem`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for bbrem data cards.

        Returns:
            ``Bbrem`` object.

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
        if mnemonic != 'bbrem':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        biases = [types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]
        materials = [types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]

        data = Bbrem(biases, materials)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Bbrem`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Bbrem``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.biases)} {' '.join(entry.to_mcnp() for entry in self.materials)}"
        )
