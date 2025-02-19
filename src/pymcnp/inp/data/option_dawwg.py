import re
import typing

from . import dawwg
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Dawwg(_option.DataOption_, keyword='dawwg'):
    """
    Represents INP data card dawwg options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Adawwg(( (((points)( \S+))|((xsec)( \S+))|((block)( \S+)(( (((ngroup)( \S+))|((isn)( \S+))|((niso)( \S+))|((mt)( \S+))|((iquad)( \S+))|((fmmix)( \S+))|((nosolv)( \S+))|((noedit)( \S+))|((nogeod)( \S+))|((nomix)( \S+))|((noasg)( \S+))|((nomacr)( \S+))|((noslnp)( \S+))|((noedtt)( \S+))|((noadjm)( \S+))|((lib)( \S+))|((libname)( \S+))|((fissneut)( \S+))|((lng)( \S+))|((balxs)( \S+))|((ntichi)( \S+))|((ievt)( \S+))|((isct)( \S+))|((ith)( \S+))|((trcor)( \S+))|((ibl)( \S+))|((ibr)( \S+))|((ibt)( \S+))|((ibb)( \S+))|((ibfrnt)( \S+))|((ibback)( \S+))|((epsi)( \S+))|((oitm)( \S+))|((nosigf)( \S+))|((srcacc)( \S+))|((diffsol)( \S+))|((tsasn)( \S+))|((tsaepsi)( \S+))|((tsaits)( \S+))|((tsabeta)( \S+))|((ptconv)( \S+))|((norm)( \S+))|((xsectp)( \S+))|((fissrp)( \S+))|((sourcp)( \S+))|((angp)( \S+))|((balp)( \S+))|((raflux)( \S+))|((rmflux)( \S+))|((avatar)( \S+))|((asleft)( \S+))|((asrite)( \S+))|((asbott)( \S+))|((astop)( \S+))|((asfrnt)( \S+))|((asback)( \S+))|((massed)( \S+))|((pted)( \S+))|((zned)( \S+))|((rzflux)( \S+))|((rzmflux)( \S+))|((edoutf)( \S+))|((byvolp)( \S+))|((ajed)( \S+))|((fluxone)( \S+))))+)?)))+)?\Z'
    )

    def __init__(self, options: tuple[dawwg.DawwgOption_] = None):
        """
        Initializes ``DataOption_Dawwg``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Dawwg``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, dawwg.DawwgOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Dawwg`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Dawwg``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Dawwg._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(dawwg.DawwgOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Dawwg(options)
