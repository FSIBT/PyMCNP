import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class BfldOption_Refpnt(_option.BfldOption_, keyword='refpnt'):
    """
    Represents INP data card data option refpnt options.

    Attributes:
        point: Point anywhere on the quadrapole beam.
    """

    _REGEX = re.compile(r'\Arefpnt(( \S+)+)\Z')

    def __init__(self, point: tuple[types.Real]):
        """
        Initializes ``BfldOption_Refpnt``.

        Parameters:
            point: Point anywhere on the quadrapole beam.

        Returns:
            ``BfldOption_Refpnt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if point is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, point)

        self.value: typing.Final[tuple[any]] = types._Tuple([point])
        self.point: typing.Final[tuple[types.Real]] = point

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BfldOption_Refpnt`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``BfldOption_Refpnt``.

        Raises:
            McnpError: SYNTAX_BFLD_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = BfldOption_Refpnt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_BFLD_OPTION, source)

        point = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return BfldOption_Refpnt(point)
