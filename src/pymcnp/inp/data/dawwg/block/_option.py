import re
import typing

from .... import _option


class BlockOption_(_option.InpOption_):
    """
    Represents generic INP data card data option dawwg option options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {}

    _REGEX = re.compile(
        r'(((ngroup)( \S+))|((isn)( \S+))|((niso)( \S+))|((mt)( \S+))|((iquad)( \S+))|((fmmix)( \S+))|((nosolv)( \S+))|((noedit)( \S+))|((nogeod)( \S+))|((nomix)( \S+))|((noasg)( \S+))|((nomacr)( \S+))|((noslnp)( \S+))|((noedtt)( \S+))|((noadjm)( \S+))|((lib)( \S+))|((libname)( \S+))|((fissneut)( \S+))|((lng)( \S+))|((balxs)( \S+))|((ntichi)( \S+))|((ievt)( \S+))|((isct)( \S+))|((ith)( \S+))|((trcor)( \S+))|((ibl)( \S+))|((ibr)( \S+))|((ibt)( \S+))|((ibb)( \S+))|((ibfrnt)( \S+))|((ibback)( \S+))|((epsi)( \S+))|((oitm)( \S+))|((nosigf)( \S+))|((srcacc)( \S+))|((diffsol)( \S+))|((tsasn)( \S+))|((tsaepsi)( \S+))|((tsaits)( \S+))|((tsabeta)( \S+))|((ptconv)( \S+))|((norm)( \S+))|((xsectp)( \S+))|((fissrp)( \S+))|((sourcp)( \S+))|((angp)( \S+))|((balp)( \S+))|((raflux)( \S+))|((rmflux)( \S+))|((avatar)( \S+))|((asleft)( \S+))|((asrite)( \S+))|((asbott)( \S+))|((astop)( \S+))|((asfrnt)( \S+))|((asback)( \S+))|((massed)( \S+))|((pted)( \S+))|((zned)( \S+))|((rzflux)( \S+))|((rzmflux)( \S+))|((edoutf)( \S+))|((byvolp)( \S+))|((ajed)( \S+))|((fluxone)( \S+)))'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
