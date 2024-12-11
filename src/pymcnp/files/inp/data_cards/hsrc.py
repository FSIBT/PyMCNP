"""
Contains the ``Hsrc`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ...utils import types
from ...utils import errors
from ...utils import _parser


class Hsrc(Data):
    """
    Represents INP hsrc data cards.

    ``Hsrc`` implements ``Data``.

    Attributes:
        x_number: Number of mesh intervals in x direction.
        x_minimum: Minimum x-value for mesh..
        x_maximum: Maximum x-value for mesh..
        y_number: Number of mesh intervals in y direction.
        y_minimum: Minimum y-value for mesh..
        y_maximum: Maximum y-value for mesh..
        z_number: Number of mesh intervals in z direction.
        z_minimum: Minimum z-value for mesh..
        z_maximum: Maximum z-value for mesh..
    """

    def __init__(
        self,
        x_number: types.McnpInteger,
        x_minimum: types.McnpReal,
        x_maximum: types.McnpReal,
        y_number: types.McnpInteger,
        y_minimum: types.McnpReal,
        y_maximum: types.McnpReal,
        z_number: types.McnpInteger,
        z_minimum: types.McnpReal,
        z_maximum: types.McnpReal,
    ):
        """
        Initializes ``Hsrc``.

        Parameters:
            x_number: Number of mesh intervals in x direction.
            x_minimum: Minimum x-value for mesh..
            x_maximum: Maximum x-value for mesh..
            y_number: Number of mesh intervals in y direction.
            y_minimum: Minimum y-value for mesh..
            y_maximum: Maximum y-value for mesh..
            z_number: Number of mesh intervals in z direction.
            z_minimum: Minimum z-value for mesh..
            z_maximum: Maximum z-value for mesh..

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if x_number is None or not (x_number > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(x_number))

        if x_minimum is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(x_minimum))

        if x_maximum is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(x_maximum))

        if y_number is None or not (y_number > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(y_number))

        if y_minimum is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(y_minimum))

        if y_maximum is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(y_maximum))

        if z_number is None or not (z_number > 0):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(z_number))

        if z_minimum is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(z_minimum))

        if z_maximum is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(z_maximum))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.HSRC
        self.parameters: Final[tuple[any]] = tuple(
            [x_number]
            + [x_minimum]
            + [x_maximum]
            + [y_number]
            + [y_minimum]
            + [y_maximum]
            + [z_number]
            + [z_minimum]
            + [z_maximum]
        )
        self.x_number: Final[types.McnpInteger] = x_number
        self.x_minimum: Final[types.McnpReal] = x_minimum
        self.x_maximum: Final[types.McnpReal] = x_maximum
        self.y_number: Final[types.McnpInteger] = y_number
        self.y_minimum: Final[types.McnpReal] = y_minimum
        self.y_maximum: Final[types.McnpReal] = y_maximum
        self.z_number: Final[types.McnpInteger] = z_number
        self.z_minimum: Final[types.McnpReal] = z_minimum
        self.z_maximum: Final[types.McnpReal] = z_maximum
        self.ident: Final[str] = 'hsrc'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Hsrc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for hsrc data cards.

        Returns:
            ``Hsrc`` object.

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
        if mnemonic != 'hsrc':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        x_number = types.McnpInteger.from_mcnp(tokens.popl())
        x_minimum = types.McnpReal.from_mcnp(tokens.popl())
        x_maximum = types.McnpReal.from_mcnp(tokens.popl())
        y_number = types.McnpInteger.from_mcnp(tokens.popl())
        y_minimum = types.McnpReal.from_mcnp(tokens.popl())
        y_maximum = types.McnpReal.from_mcnp(tokens.popl())
        z_number = types.McnpInteger.from_mcnp(tokens.popl())
        z_minimum = types.McnpReal.from_mcnp(tokens.popl())
        z_maximum = types.McnpReal.from_mcnp(tokens.popl())

        data = Hsrc(
            x_number,
            x_minimum,
            x_maximum,
            y_number,
            y_minimum,
            y_maximum,
            z_number,
            z_minimum,
            z_maximum,
        )
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Hsrc`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Hsrc``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f'{self.mnemonic.to_mcnp()} {self.x_number.to_mcnp()} {self.x_minimum.to_mcnp()} {self.x_maximum.to_mcnp()} {self.y_number.to_mcnp()} {self.y_minimum.to_mcnp()} {self.y_maximum.to_mcnp()} {self.z_number.to_mcnp()} {self.z_minimum.to_mcnp()} {self.z_maximum.to_mcnp()}'
        )
