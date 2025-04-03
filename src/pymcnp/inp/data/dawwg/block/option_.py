import re
import typing


from ....option_ import Option_
from .....utils import types


class BlockOption_(Option_):
    """
    Represents generic INP block options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'fissneut( {types.IntegerOrJump._REGEX.pattern})|libname( {types.String._REGEX.pattern})|diffsol( {types.String._REGEX.pattern})|tsaepsi( {types.RealOrJump._REGEX.pattern})|tsabeta( {types.RealOrJump._REGEX.pattern})|rzmflux( {types.IntegerOrJump._REGEX.pattern})|fluxone( {types.IntegerOrJump._REGEX.pattern})|ngroup( {types.IntegerOrJump._REGEX.pattern})|nosolv( {types.IntegerOrJump._REGEX.pattern})|noedit( {types.IntegerOrJump._REGEX.pattern})|nogeod( {types.IntegerOrJump._REGEX.pattern})|nomacr( {types.IntegerOrJump._REGEX.pattern})|noslnp( {types.IntegerOrJump._REGEX.pattern})|noedtt( {types.IntegerOrJump._REGEX.pattern})|noadjm( {types.IntegerOrJump._REGEX.pattern})|ntichi( {types.IntegerOrJump._REGEX.pattern})|ibfrnt( {types.IntegerOrJump._REGEX.pattern})|ibback( {types.IntegerOrJump._REGEX.pattern})|nosigf( {types.IntegerOrJump._REGEX.pattern})|srcacc( {types.String._REGEX.pattern})|tsaits( {types.IntegerOrJump._REGEX.pattern})|ptconv( {types.IntegerOrJump._REGEX.pattern})|xsectp( {types.IntegerOrJump._REGEX.pattern})|fissrp( {types.IntegerOrJump._REGEX.pattern})|sourcp( {types.IntegerOrJump._REGEX.pattern})|raflux( {types.IntegerOrJump._REGEX.pattern})|rmflux( {types.IntegerOrJump._REGEX.pattern})|avatar( {types.IntegerOrJump._REGEX.pattern})|asleft( {types.IntegerOrJump._REGEX.pattern})|asrite( {types.IntegerOrJump._REGEX.pattern})|asbott( {types.IntegerOrJump._REGEX.pattern})|asfrnt( {types.IntegerOrJump._REGEX.pattern})|asback( {types.IntegerOrJump._REGEX.pattern})|massed( {types.IntegerOrJump._REGEX.pattern})|rzflux( {types.IntegerOrJump._REGEX.pattern})|edoutf( {types.IntegerOrJump._REGEX.pattern})|byvolp( {types.IntegerOrJump._REGEX.pattern})|iquad( {types.IntegerOrJump._REGEX.pattern})|fmmix( {types.IntegerOrJump._REGEX.pattern})|nomix( {types.IntegerOrJump._REGEX.pattern})|noasg( {types.IntegerOrJump._REGEX.pattern})|balxs( {types.IntegerOrJump._REGEX.pattern})|trcor( {types.String._REGEX.pattern})|tsasn( {types.IntegerOrJump._REGEX.pattern})|astop( {types.IntegerOrJump._REGEX.pattern})|niso( {types.IntegerOrJump._REGEX.pattern})|ievt( {types.IntegerOrJump._REGEX.pattern})|isct( {types.IntegerOrJump._REGEX.pattern})|epsi( {types.RealOrJump._REGEX.pattern})|oitm( {types.IntegerOrJump._REGEX.pattern})|norm( {types.RealOrJump._REGEX.pattern})|angp( {types.IntegerOrJump._REGEX.pattern})|balp( {types.IntegerOrJump._REGEX.pattern})|pted( {types.IntegerOrJump._REGEX.pattern})|zned( {types.IntegerOrJump._REGEX.pattern})|ajed( {types.IntegerOrJump._REGEX.pattern})|isn( {types.IntegerOrJump._REGEX.pattern})|lib( {types.String._REGEX.pattern})|lng( {types.IntegerOrJump._REGEX.pattern})|ith( {types.IntegerOrJump._REGEX.pattern})|ibl( {types.IntegerOrJump._REGEX.pattern})|ibr( {types.IntegerOrJump._REGEX.pattern})|ibt( {types.IntegerOrJump._REGEX.pattern})|ibb( {types.IntegerOrJump._REGEX.pattern})|mt( {types.IntegerOrJump._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
