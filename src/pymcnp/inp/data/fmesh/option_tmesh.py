import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Tmesh(_option.FmeshOption_, keyword='tmesh'):
    """
    Represents INP data card data option tmesh options.

    Attributes:
        time: Values of mesh points in time.
    """

    _REGEX = re.compile(r'\Atmesh( \S+)\Z')

    def __init__(self, time: types.Real):
        """
        Initializes ``FmeshOption_Tmesh``.

        Parameters:
            time: Values of mesh points in time.

        Returns:
            ``FmeshOption_Tmesh``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time)

        self.value: typing.Final[tuple[any]] = types._Tuple([time])
        self.time: typing.Final[types.Real] = time

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Tmesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Tmesh``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Tmesh._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        time = types.Real.from_mcnp(tokens[1])

        return FmeshOption_Tmesh(time)
