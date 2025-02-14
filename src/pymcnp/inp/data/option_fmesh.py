import re
import typing

from . import fmesh
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fmesh(_option.DataOption_, keyword='fmesh'):
    """
    Represents INP data card fmesh options.

    Attributes:
        options: Dictionary of options.
        suffix: Data card option suffix.
        designator: Data card particle designator.
    """

    _REGEX = re.compile(
        r'\Afmesh(\d+?):(\S+?)(( (((geom)( \S+))|((origin)( \S+)( \S+)( \S+))|((axs)( \S+)( \S+)( \S+))|((vec)( \S+)( \S+)( \S+))|((imesh)( \S+))|((iints)( \S+))|((jmesh)( \S+))|((jints)( \S+))|((kmesh)( \S+))|((kints)( \S+))|((emesh)( \S+))|((eints)( \S+))|((enorm)( \S+))|((tmesh)( \S+))|((tints)( \S+))|((tnorm)( \S+))|((factor)( \S+))|((out)( \S+))|((tr)( \S+))|((inc)( \S+)( \S+)?)|((type)( \S+))|((kclear)( \S+))))+)?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        options: tuple[fmesh.FmeshOption_] = None,
    ):
        """
        Initializes ``DataOption_Fmesh``.

        Parameters:
            options: Dictionary of options.
            suffix: Data card option suffix.
            designator: Data card particle designator.

        Returns:
            ``DataOption_Fmesh``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
        """

        if suffix is None or not (0 < suffix <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, fmesh.FmeshOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )
        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fmesh`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fmesh``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fmesh._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(fmesh.FmeshOption_, tokens[3])))
            if tokens[3]
            else None
        )

        return DataOption_Fmesh(suffix, designator, options)
