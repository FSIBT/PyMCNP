import re
import typing


from ....option_ import Option_


class BlockOption_(Option_):
    """
    Represents generic INP block options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'fissneut( \S+)|libname( \S+)|diffsol( \S+)|tsaepsi( \S+)|tsabeta( \S+)|rzmflux( \S+)|fluxone( \S+)|ngroup( \S+)|nosolv( \S+)|noedit( \S+)|nogeod( \S+)|nomacr( \S+)|noslnp( \S+)|noedtt( \S+)|noadjm( \S+)|ntichi( \S+)|ibfrnt( \S+)|ibback( \S+)|nosigf( \S+)|srcacc( \S+)|tsaits( \S+)|ptconv( \S+)|xsectp( \S+)|fissrp( \S+)|sourcp( \S+)|raflux( \S+)|rmflux( \S+)|avatar( \S+)|asleft( \S+)|asrite( \S+)|asbott( \S+)|asfrnt( \S+)|asback( \S+)|massed( \S+)|rzflux( \S+)|edoutf( \S+)|byvolp( \S+)|iquad( \S+)|fmmix( \S+)|nomix( \S+)|noasg( \S+)|balxs( \S+)|trcor( \S+)|tsasn( \S+)|astop( \S+)|niso( \S+)|ievt( \S+)|isct( \S+)|epsi( \S+)|oitm( \S+)|norm( \S+)|angp( \S+)|balp( \S+)|pted( \S+)|zned( \S+)|ajed( \S+)|isn( \S+)|lib( \S+)|lng( \S+)|ith( \S+)|ibl( \S+)|ibr( \S+)|ibt( \S+)|ibb( \S+)|mt( \S+)'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
