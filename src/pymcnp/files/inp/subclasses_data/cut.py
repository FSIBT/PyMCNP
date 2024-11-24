"""
Contains the ``Cut`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ....utils import types, errors, _parser


class Cut(Data):
    """
    Represents INP cut data cards.

    ``Cut`` implements ``Data``.

    Attributes:
        time_cutoff: Time cutoff in shakes.
        energy_cutoff: Lower energy cutoff.
        weight_cutoff1: Weight cutoff #1.
        weight_cutoff2: Weight cutoff #2.
        source_weight: Minimum source weight.
    """

    def __init__(
        self,
        time_cutoff: types.McnpReal,
        energy_cutoff: types.McnpReal,
        weight_cutoff1: types.McnpReal,
        weight_cutoff2: types.McnpReal,
        source_weight: types.McnpReal,
    ):
        """
        Initializes ``Cut``.

        Parameters:
            time_cutoff: Time cutoff in shakes.
            energy_cutoff: Lower energy cutoff.
            weight_cutoff1: Weight cutoff #1.
            weight_cutoff2: Weight cutoff #2.
            source_weight: Minimum source weight.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if time_cutoff is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(time_cutoff))

        if energy_cutoff is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(energy_cutoff))

        if weight_cutoff1 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weight_cutoff1))

        if weight_cutoff2 is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(weight_cutoff2))

        if source_weight is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(source_weight))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.CUT
        self.parameters: Final[tuple[any]] = tuple(
            [time_cutoff] + [energy_cutoff] + [weight_cutoff1] + [weight_cutoff2] + [source_weight]
        )
        self.time_cutoff: Final[types.McnpReal] = time_cutoff
        self.energy_cutoff: Final[types.McnpReal] = energy_cutoff
        self.weight_cutoff1: Final[types.McnpReal] = weight_cutoff1
        self.weight_cutoff2: Final[types.McnpReal] = weight_cutoff2
        self.source_weight: Final[types.McnpReal] = source_weight
        self.ident: Final[str] = 'cut'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cut`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for cut data cards.

        Returns:
            ``Cut`` object.

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
        if mnemonic != 'cut':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        time_cutoff = types.McnpReal.from_mcnp(tokens.popl())
        energy_cutoff = types.McnpReal.from_mcnp(tokens.popl())
        weight_cutoff1 = types.McnpReal.from_mcnp(tokens.popl())
        weight_cutoff2 = types.McnpReal.from_mcnp(tokens.popl())
        source_weight = types.McnpReal.from_mcnp(tokens.popl())

        data = Cut(time_cutoff, energy_cutoff, weight_cutoff1, weight_cutoff2, source_weight)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Cut`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Cut``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.time_cutoff.to_mcnp()} {self.energy_cutoff.to_mcnp()} {self.weight_cutoff1.to_mcnp()} {self.weight_cutoff2.to_mcnp()} {self.source_weight.to_mcnp()}'
        )
