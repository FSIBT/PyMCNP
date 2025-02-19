import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Kmesh(_option.FmeshOption_, keyword='kmesh'):
    """
    Represents INP data card data option kmesh options.

    Attributes:
        locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.
    """

    _REGEX = re.compile(r'\Akmesh( \S+)\Z')

    def __init__(self, locations: types.Real):
        """
        Initializes ``FmeshOption_Kmesh``.

        Parameters:
            locations: Locations of mesh points z/theta for rectangular/cylindrical geometry.

        Returns:
            ``FmeshOption_Kmesh``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if locations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, locations)

        self.value: typing.Final[tuple[any]] = types._Tuple([locations])
        self.locations: typing.Final[types.Real] = locations

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Kmesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Kmesh``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Kmesh._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        locations = types.Real.from_mcnp(tokens[1])

        return FmeshOption_Kmesh(locations)
