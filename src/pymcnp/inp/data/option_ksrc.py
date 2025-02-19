import re
import typing

from . import ksrc
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ksrc(_option.DataOption_, keyword='ksrc'):
    """
    Represents INP data card ksrc options.

    Attributes:
        locations: Tuple of inital source points.
    """

    _REGEX = re.compile(r'\Aksrc((( \S+)( \S+)( \S+))+)\Z')

    def __init__(self, locations: tuple[ksrc.KsrcEntry_Location]):
        """
        Initializes ``DataOption_Ksrc``.

        Parameters:
            locations: Tuple of inital source points.

        Returns:
            ``DataOption_Ksrc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, locations)

        self.value: typing.Final[tuple[any]] = types._Tuple([locations])
        self.locations: typing.Final[tuple[ksrc.KsrcEntry_Location]] = locations

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ksrc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ksrc``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ksrc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        locations = types._Tuple(
            [
                ksrc.KsrcEntry_Location.from_mcnp(token[0])
                for token in ksrc.KsrcEntry_Location._REGEX.finditer(tokens[1])
            ]
        )

        return DataOption_Ksrc(locations)
