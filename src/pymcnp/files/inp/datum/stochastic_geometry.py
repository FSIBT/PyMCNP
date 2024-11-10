from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class StochasticGeometryValue:
    """
    ``StochasticGeometryValue`` represents INP stochastic geometry data
    card entries.

    ``StochasticGeometryValue`` implements INP stochastic geometry
    specifications as a Python inner class. Its attributes store different
    stochastic geometry entries, and its methods provide entry points
    and endpoints for working with stochastic geometry entries.
    ``StochasticGeometry`` depends on ``StochasticGeometryValue`` as a data
    type.

    Attributes:
        number: Stochastic geometry universe number.
        maximum_x: Stochastic geometry maximum translation in x direction.
        maximum_y: Stochastic geometry maximum translation in y direction.
        maximum_z: Stochastic geometry maximum translation in z direction.
    """

    def __init__(
        self,
        number: types.McnpInteger,
        maximum_x: types.McnpReal,
        maximum_y: types.McnpReal,
        maximum_z: types.McnpReal,
    ):
        """
        ``__init__`` initializes ``StochasticGeometryValue``.

        Parameters:
            number: Stochastic geometry universe number.
            maximum_x: Stochastic geometry maximum translation in x direction.
            maximum_y: Stochastic geometry maximum translation in y direction.
            maximum_z: Stochastic geometry maximum translation in z direction.

        Raises:
            MCNPSemanticCodes: INVALID_DATUM_PARAMETERS.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if maximum_x is None:
            raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if maximum_y is None:
            raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if maximum_z is None:
            raise errors.MCNPSemanticErrors(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        self.number: Final[int] = number
        self.maximum_x: Final[float] = maximum_x
        self.maximum_y: Final[float] = maximum_y
        self.maximum_z: Final[float] = maximum_z

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``StochasticGeometryValue`` objects from
        INP.

        ``from_mcnp`` constructs instances of ``StochasticGeometryValue``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function.

        Parameters:
            source: INP for stochastic geometry values.

        Returns:
            ``StochasticGeometryValue`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM_URAN, TOOLONG_DATUM_URAN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_URAN),
        )

        number = tokens.popl()
        maximum_x = tokens.popl()
        maximum_y = tokens.popl()
        maximum_z = tokens.popl()

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_URAN)

        return StochasticGeometryValue(number, maximum_x, maximum_y, maximum_z)


class StochasticGeometry(Datum):
    """
    ``StochasticGeometry`` represents INP stochastic geometry data cards.

    ``StochasticGeometry`` inherits attributes from ``Datum``. It represents
    the INP universe data card syntax element.

    Attributes:
        transformations: Tuple of stochastric geometry transformations.
    """

    def __init__(self, transformations: tuple[StochasticGeometryValue]):
        """
        ``__init__`` initializes ``StochasticGeometry``.

         Parameters:
            *transformations: Tuple of stochastric geometry transformations.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in transformations:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'uran')
        self.mnemonic = DatumMnemonic.STOCHASTIC_GEOMETRY
        self.parameters = transformations

        self.transformations = transformations
