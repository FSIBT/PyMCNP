import re
import typing

from . import block
from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class DawwgOption_Block(_option.DawwgOption_, keyword='block'):
    """
    Represents INP data card data option block options.

    Attributes:
        setting: Destination of key-value pairs.
        options: Dictionary of dawwg block options.
    """

    _REGEX = re.compile(
        r'\Ablock( \S+)(( (((ngroup)( \S+))|((isn)( \S+))|((niso)( \S+))|((mt)( \S+))|((iquad)( \S+))|((fmmix)( \S+))|((nosolv)( \S+))|((noedit)( \S+))|((nogeod)( \S+))|((nomix)( \S+))|((noasg)( \S+))|((nomacr)( \S+))|((noslnp)( \S+))|((noedtt)( \S+))|((noadjm)( \S+))|((lib)( \S+))|((libname)( \S+))|((fissneut)( \S+))|((lng)( \S+))|((balxs)( \S+))|((ntichi)( \S+))|((ievt)( \S+))|((isct)( \S+))|((ith)( \S+))|((trcor)( \S+))|((ibl)( \S+))|((ibr)( \S+))|((ibt)( \S+))|((ibb)( \S+))|((ibfrnt)( \S+))|((ibback)( \S+))|((epsi)( \S+))|((oitm)( \S+))|((nosigf)( \S+))|((srcacc)( \S+))|((diffsol)( \S+))|((tsasn)( \S+))|((tsaepsi)( \S+))|((tsaits)( \S+))|((tsabeta)( \S+))|((ptconv)( \S+))|((norm)( \S+))|((xsectp)( \S+))|((fissrp)( \S+))|((sourcp)( \S+))|((angp)( \S+))|((balp)( \S+))|((raflux)( \S+))|((rmflux)( \S+))|((avatar)( \S+))|((asleft)( \S+))|((asrite)( \S+))|((asbott)( \S+))|((astop)( \S+))|((asfrnt)( \S+))|((asback)( \S+))|((massed)( \S+))|((pted)( \S+))|((zned)( \S+))|((rzflux)( \S+))|((rzmflux)( \S+))|((edoutf)( \S+))|((byvolp)( \S+))|((ajed)( \S+))|((fluxone)( \S+))))+)?\Z'
    )

    def __init__(self, setting: types.Integer, options: tuple[block.BlockOption_] = None):
        """
        Initializes ``DawwgOption_Block``.

        Parameters:
            setting: Destination of key-value pairs.
            options: Dictionary of dawwg block options.

        Returns:
            ``DawwgOption_Block``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {1, 3, 5, 6}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting, options])
        self.setting: typing.Final[types.Integer] = setting
        self.options: typing.Final[dict[str, block.BlockOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DawwgOption_Block`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``DawwgOption_Block``.

        Raises:
            InpError: SYNTAX_DAWWG_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DawwgOption_Block._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        setting = types.Integer.from_mcnp(tokens[1])
        options = (
            types._Tuple(tuple(_parser.process_inp_option(block.BlockOption_, tokens[2])))
            if tokens[2]
            else None
        )

        return DawwgOption_Block(setting, options)
