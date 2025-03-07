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
        rf'fissneut( {types.Integer._REGEX.pattern})|libname( {types.String._REGEX.pattern})|diffsol( {types.String._REGEX.pattern})|tsaepsi( {types.Real._REGEX.pattern})|tsabeta( {types.Real._REGEX.pattern})|rzmflux( {types.Integer._REGEX.pattern})|fluxone( {types.Integer._REGEX.pattern})|ngroup( {types.Integer._REGEX.pattern})|nosolv( {types.Integer._REGEX.pattern})|noedit( {types.Integer._REGEX.pattern})|nogeod( {types.Integer._REGEX.pattern})|nomacr( {types.Integer._REGEX.pattern})|noslnp( {types.Integer._REGEX.pattern})|noedtt( {types.Integer._REGEX.pattern})|noadjm( {types.Integer._REGEX.pattern})|ntichi( {types.Integer._REGEX.pattern})|ibfrnt( {types.Integer._REGEX.pattern})|ibback( {types.Integer._REGEX.pattern})|nosigf( {types.Integer._REGEX.pattern})|srcacc( {types.String._REGEX.pattern})|tsaits( {types.Integer._REGEX.pattern})|ptconv( {types.Integer._REGEX.pattern})|xsectp( {types.Integer._REGEX.pattern})|fissrp( {types.Integer._REGEX.pattern})|sourcp( {types.Integer._REGEX.pattern})|raflux( {types.Integer._REGEX.pattern})|rmflux( {types.Integer._REGEX.pattern})|avatar( {types.Integer._REGEX.pattern})|asleft( {types.Integer._REGEX.pattern})|asrite( {types.Integer._REGEX.pattern})|asbott( {types.Integer._REGEX.pattern})|asfrnt( {types.Integer._REGEX.pattern})|asback( {types.Integer._REGEX.pattern})|massed( {types.Integer._REGEX.pattern})|rzflux( {types.Integer._REGEX.pattern})|edoutf( {types.Integer._REGEX.pattern})|byvolp( {types.Integer._REGEX.pattern})|iquad( {types.Integer._REGEX.pattern})|fmmix( {types.Integer._REGEX.pattern})|nomix( {types.Integer._REGEX.pattern})|noasg( {types.Integer._REGEX.pattern})|balxs( {types.Integer._REGEX.pattern})|trcor( {types.String._REGEX.pattern})|tsasn( {types.Integer._REGEX.pattern})|astop( {types.Integer._REGEX.pattern})|niso( {types.Integer._REGEX.pattern})|ievt( {types.Integer._REGEX.pattern})|isct( {types.Integer._REGEX.pattern})|epsi( {types.Real._REGEX.pattern})|oitm( {types.Integer._REGEX.pattern})|norm( {types.Real._REGEX.pattern})|angp( {types.Integer._REGEX.pattern})|balp( {types.Integer._REGEX.pattern})|pted( {types.Integer._REGEX.pattern})|zned( {types.Integer._REGEX.pattern})|ajed( {types.Integer._REGEX.pattern})|isn( {types.Integer._REGEX.pattern})|lib( {types.String._REGEX.pattern})|lng( {types.Integer._REGEX.pattern})|ith( {types.Integer._REGEX.pattern})|ibl( {types.Integer._REGEX.pattern})|ibr( {types.Integer._REGEX.pattern})|ibt( {types.Integer._REGEX.pattern})|ibb( {types.Integer._REGEX.pattern})|mt( {types.Integer._REGEX.pattern})'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
