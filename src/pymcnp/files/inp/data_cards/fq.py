"""
Contains the ``Fq`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Fq(Data):
    """
    Represents INP fq data cards.

    ``Fq`` implements ``Data``.

    Attributes:
        a1: Letters representing tally bin types.
        a2: Letters representing tally bin types.
        a3: Letters representing tally bin types.
        a4: Letters representing tally bin types.
        a5: Letters representing tally bin types.
        a6: Letters representing tally bin types.
        a7: Letters representing tally bin types.
        a8: Letters representing tally bin types.
        suffix: Data card suffix.
    """

    def __init__(
        self,
        a1: str,
        a2: str,
        a3: str,
        a4: str,
        a5: str,
        a6: str,
        a7: str,
        a8: str,
        suffix: types.McnpInteger,
    ):
        """
        Initializes ``Fq``.

        Parameters:
            a1: Letters representing tally bin types.
            a2: Letters representing tally bin types.
            a3: Letters representing tally bin types.
            a4: Letters representing tally bin types.
            a5: Letters representing tally bin types.
            a6: Letters representing tally bin types.
            a7: Letters representing tally bin types.
            a8: Letters representing tally bin types.
            suffix: Data card suffix.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if a1 is None or a1 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a1))

        if a2 is None or a2 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a2))

        if a3 is None or a3 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a3))

        if a4 is None or a4 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a4))

        if a5 is None or a5 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a5))

        if a6 is None or a6 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a6))

        if a7 is None or a7 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a7))

        if a8 is None or a8 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(a8))

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.FQ
        self.parameters: Final[tuple[any]] = tuple(
            [a1] + [a2] + [a3] + [a4] + [a5] + [a6] + [a7] + [a8] + [suffix]
        )
        self.a1: Final[str] = a1
        self.a2: Final[str] = a2
        self.a3: Final[str] = a3
        self.a4: Final[str] = a4
        self.a5: Final[str] = a5
        self.a6: Final[str] = a6
        self.a7: Final[str] = a7
        self.a8: Final[str] = a8
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'fq{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fq`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for fq data cards.

        Returns:
            ``Fq`` object.

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
        if mnemonic != 'fq':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[2:])

        a1 = tokens.popl()
        a2 = tokens.popl()
        a3 = tokens.popl()
        a4 = tokens.popl()
        a5 = tokens.popl()
        a6 = tokens.popl()
        a7 = tokens.popl()
        a8 = tokens.popl()

        data = Fq(a1, a2, a3, a4, a5, a6, a7, a8, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Fq`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Fq``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {self.a1.to_mcnp()} {self.a2.to_mcnp()} {self.a3.to_mcnp()} {self.a4.to_mcnp()} {self.a5.to_mcnp()} {self.a6.to_mcnp()} {self.a7.to_mcnp()} {self.a8.to_mcnp()}'
        )
