import re
import typing

from . import ds_2
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ds2(_option.DataOption_, keyword='ds'):
    """
    Represents INP data card ds_2 options.

    Attributes:
        q: Dependent source Q option.
        vss: Dependent source independent & dependent variables.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Ads(\d+?)( \S+)(((( \S+)+))+)\Z')

    def __init__(self, q: types.String, vss: tuple[ds_2.Ds2Entry_Qpair], suffix: types.Integer):
        """
        Initializes ``DataOption_Ds2``.

        Parameters:
            q: Dependent source Q option.
            vss: Dependent source independent & dependent variables.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Ds2``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if q is None or q not in {'q'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, q)
        if vss is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vss)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([q, vss])
        self.q: typing.Final[types.String] = q
        self.vss: typing.Final[tuple[ds_2.Ds2Entry_Qpair]] = vss
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ds2`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ds2``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ds2._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        q = types.String.from_mcnp(tokens[2])
        vss = types._Tuple(
            [
                ds_2.Ds2Entry_Qpair.from_mcnp(token[0])
                for token in ds_2.Ds2Entry_Qpair._REGEX.finditer(tokens[3])
            ]
        )

        return DataOption_Ds2(q, vss, suffix)
