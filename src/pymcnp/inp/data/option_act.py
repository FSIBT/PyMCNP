import re
import typing

from . import act
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Act(_option.DataOption_, keyword='act'):
    """
    Represents INP data card act options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Aact(( (((fission)( \S+))|((nonfiss)( \S+))|((dn)( \S+))|((dg)( \S+))|((thresh)( \S+))|((dnbais)( \S+))|((nap)( \S+))|((dneb)((( \S+)( \S+))+))|((dgeb)((( \S+)( \S+))+))|((pecut)( \S+))|((hlcut)( \S+))|((sample)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[act.ActOption_] = None):
        """
        Initializes ``DataOption_Act``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Act``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, act.ActOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Act`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Act``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Act._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(act.ActOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Act(options)
