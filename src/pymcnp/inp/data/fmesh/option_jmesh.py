import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Jmesh(_option.FmeshOption_, keyword='jmesh'):
    """
    Represents INP data card data option jmesh options.

    Attributes:
        locations: Locations of mesh points y/z for rectangular/cylindrical geometry.
    """

    _REGEX = re.compile(r'\Ajmesh( \S+)\Z')

    def __init__(self, locations: types.Real):
        """
        Initializes ``FmeshOption_Jmesh``.

        Parameters:
            locations: Locations of mesh points y/z for rectangular/cylindrical geometry.

        Returns:
            ``FmeshOption_Jmesh``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if locations is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, locations)

        self.value: typing.Final[tuple[any]] = types._Tuple([locations])
        self.locations: typing.Final[types.Real] = locations

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Jmesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Jmesh``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Jmesh._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        locations = types.Real.from_mcnp(tokens[1])

        return FmeshOption_Jmesh(locations)
