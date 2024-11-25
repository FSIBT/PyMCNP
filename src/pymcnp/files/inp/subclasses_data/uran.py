"""
Contains the ``Uran`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataEntry
from ...utils import types, errors, _parser


class UranEntry(DataEntry):
    """
    Represents INP uran data card entry.

    ``UranEntry`` implements ``DataEntry``.

    Attributes:
            number: Universe number for transformation.
            maximum_x: Maximum displacement in the x direction.
            maximum_y: Maximum displacement in the y direction.
            maximum_z: Maximum displacement in the z direction.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        maximum_x: types.McnpReal,
        maximum_y: types.McnpReal,
        maximum_z: types.McnpReal,
    ):
        """
        Initializes ``UranEntry``.

        Parameters:
                number: Universe number for transformation.
                maximum_x: Maximum displacement in the x direction.
                maximum_y: Maximum displacement in the y direction.
                maximum_z: Maximum displacement in the z direction.

        Raises:
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if maximum_x is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if maximum_y is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if maximum_z is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        self.number: Final[types.McnpInteger] = number
        self.maximum_x: Final[types.McnpReal] = maximum_x
        self.maximum_y: Final[types.McnpReal] = maximum_y
        self.maximum_z: Final[types.McnpReal] = maximum_z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``UranEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``UranEntry``.

        Returns:
            ``UranEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        number = types.McnpInteger.from_mcnp(tokens.popl())
        maximum_x = types.McnpReal.from_mcnp(tokens.popl())
        maximum_y = types.McnpReal.from_mcnp(tokens.popl())
        maximum_z = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return UranEntry(number, maximum_x, maximum_y, maximum_z)

    def to_mcnp(self):
        """
        Generates INP from ``UranEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``UranEntry``.
        """

        return f'{self.number.to_mcnp()} {self.maximum_x.to_mcnp()} {self.maximum_y.to_mcnp()} {self.maximum_z.to_mcnp()}'


class Uran(Data):
    """
    Represents INP uran data cards.

    ``Uran`` implements ``Data``.

    Attributes:
        transformations: Tuple of stochastic transformations.
    """

    def __init__(self, transformations: tuple[UranEntry]):
        """
        Initializes ``Uran``.

        Parameters:
            transformations: Tuple of stochastic transformations.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if transformations is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(transformations))

        for entry in transformations:
            if entry is None:
                raise errors.McnpError(
                    errors.McnpCode.INVALID_DATUM_PARAMETERS, str(transformations)
                )

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.URAN
        self.parameters: Final[tuple[any]] = tuple(list(transformations))
        self.transformations: Final[tuple[UranEntry]] = transformations
        self.ident: Final[str] = 'uran'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Uran`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for uran data cards.

        Returns:
            ``Uran`` object.

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
        if mnemonic != 'uran':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        transformations = [
            UranEntry.from_mcnp(' '.join([tokens.popl() for __ in range(0, 4)]))
            for _ in range(0, len(tokens), 4)
        ]

        data = Uran(transformations)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Uran`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Uran``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.transformations)}"
        )
