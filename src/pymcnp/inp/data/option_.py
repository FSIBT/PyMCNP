import re
import typing

from . import dawwg
from . import embed
from . import embee
from . import m
from . import act
from . import fmult
from . import tropt
from . import bfld
from . import sdef
from . import ssw
from . import ssr
from . import kopts
from . import t_1
from . import df_1
from . import pert
from . import kpert
from . import ksen
from . import fmesh
from . import var
from . import mesh
from . import stop
from . import ptrac
from . import rand

from ..option_ import Option_
from ...utils import types


class DataOption_(Option_):
    """
    Represents generic INP data options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        rf'phys:n( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|phys:p( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|phys:e( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|phys:h( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|dawwg(( ({dawwg.DawwgOption_._REGEX.pattern}))+)?|embed(( ({embed.EmbedOption_._REGEX.pattern}))+)?|embee(\S+)(( ({embee.EmbeeOption_._REGEX.pattern}))+)?|embeb(\S+)(( \S+)+)|embem(\S+)(( \S+)+)|embtb(\S+)(( \S+)+)|embtm(\S+)(( \S+)+)|embdb(\S+)(( \S+)+)|embdf(\S+)(( \S+)+)|otfdb(( \S+)+)|totnu( \S+)?|awtab(( {types.SubstanceEntry._REGEX.pattern})+)|mgopt( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|thtme(( \S+)+)|mphys( \S+)?|fmult( \S+)(( ({fmult.FmultOption_._REGEX.pattern}))+)?|tropt(( ({tropt.TroptOption_._REGEX.pattern}))+)?|cosyp( \S+)( \S+)( \S+)(( \S+)+)|bflcl(( \S+)+)|kcode( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|kopts(( ({kopts.KoptsOption_._REGEX.pattern}))+)?|notrn|kpert(\S+)(( ({kpert.KpertOption_._REGEX.pattern}))+)?|fmesh(\S+):(\S+)(( ({fmesh.FmeshOption_._REGEX.pattern}))+)?|spdtl( \S+)|esplt:(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|tsplt:(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|bbrem( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)(( \S+)+)|pikmt(( {types.PhotonBiasEntry._REGEX.pattern})+)|print(( \S+)+)?|talnp(( \S+)+)?|prdmp( \S+)( \S+)( \S+)( \S+)( \S+)|ptrac(( ({ptrac.PtracOption_._REGEX.pattern}))+)?|histp( \S+)?(( \S+)+)?|files(( {types.FileEntry._REGEX.pattern})+)|area(( \S+)+)|fill(( \S+)+)|uran(( {types.StochasticEntry._REGEX.pattern})+)|nonu(( \S+)+)?|void(( \S+)+)?|drxs(( \S+)+)?|mode(( \S+)+)|phys:(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|elpt(( \S+)+)|cosy(( \S+)+)|bfld(\S+)( \S+)(( ({bfld.BfldOption_._REGEX.pattern}))+)?|sdef(( ({sdef.SdefOption_._REGEX.pattern}))+)?|ksrc(( {types.LocationEntry._REGEX.pattern})+)|hsrc( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|[*]c(\S+)(( \S+)+)( \S+)?( \S+)?|pert(\S+):(\S+)(( ({pert.PertOption_._REGEX.pattern}))+)?|ksen(\S+)( \S+)(( ({ksen.KsenOption_._REGEX.pattern}))+)?|wwge(( \S+)+)|wwgt(( \S+)+)|mesh(( ({mesh.MeshOption_._REGEX.pattern}))+)?|ctme( \S+)|stop(( ({stop.StopOption_._REGEX.pattern}))+)?|rand(( ({rand.RandOption_._REGEX.pattern}))+)?|dbcn( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|lost( \S+)( \S+)|idum(( \S+)+)|rdum(( \S+)+)|vol( \S+)?(( \S+)+)|lat(( \S+)+)|act(( ({act.ActOption_._REGEX.pattern}))+)?|cut( \S+)( \S+)( \S+)( \S+)( \S+)|lca( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|lcb( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|lcc( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|lea( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|leb( \S+)( \S+)( \S+)( \S+)|unc(( \S+)+)|ssw(( \S+)+)(( \S+)+)(( ({ssw.SswOption_._REGEX.pattern}))+)?|ssr(( ({ssr.SsrOption_._REGEX.pattern}))+)?|fip(\S+):(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|fir(\S+):(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|fic(\S+):(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|imp:(\S+)(( \S+)+)|var(( ({var.VarOption_._REGEX.pattern}))+)?|wwe:(\S+)(( \S+)+)|wwt:(\S+)(( \S+)+)|wwn(\S+):(\S+)(( \S+)+)|wwp:(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|wwg( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|ext:(\S+)(( \S+)+)|fcl:(\S+)(( \S+)+)|dxt:(\S+)( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( {types.ShellEntry._REGEX.pattern})( \S+)( \S+)( \S+)|dxc(\S+):(\S+)(( \S+)+)|pwt(( \S+)+)|nps( \S+)( \S+)?|tr(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|dm(( \S+)+)|mt(\S+)( \S+)|mx(\S+):(\S+)(( \S+)+)|xs(\S+)(( {types.SubstanceEntry._REGEX.pattern})+)|si(\S+)( \S+)(( \S+)+)|si(\S+)( \S+)(( \S+)+)|sp(\S+)( \S+)(( \S+)+)|sp( \S+)( \S+)( \S+)?|sb(\S+)( \S+)(( \S+)+)|sb( \S+)( \S+)( \S+)?|ds(\S+)( \S+)(( \S+)+)|ds(\S+)( \S+)(( {types.IndependentDependentEntry._REGEX.pattern})+)|ds(\S+)( \S+)(( {types.IndependentDependentEntry._REGEX.pattern})+)|sc(\S+)(( \S+)+)|fc(\S+)( \S+)|fq(\S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)|de(\S+)( \S+)(( \S+)+)|df(\S+)( \S+)(( \S+)+)|df(\S+)(( ({df_1.Df_1Option_._REGEX.pattern}))+)|em(\S+)(( \S+)+)|tm(\S+)(( \S+)+)|cm(\S+)(( \S+)+)|cf(\S+)(( \S+)+)|sf(\S+)(( \S+)+)|fs(\S+)(( \S+)+)( \S+)?( \S+)?|sd(( \S+)+)|fu(\S+)(( \S+)+)( \S+)?( \S+)?|dd(\S+)(( {types.DiagnosticEntry._REGEX.pattern})+)|pd(\S+):(\S+)(( \S+)+)|za( \S+)?|zb( \S+)?|zc( \S+)?|zd( \S+)?|u(( \S+)+)|m(\S+)(( {types.SubstanceEntry._REGEX.pattern})+)(( ({m.MOption_._REGEX.pattern}))+)?|f(\S+):(\S+)(( \S+)+)( \S+)?|f(\S+):(\S+)(( {types.SphereEntry._REGEX.pattern})+)( \S+)?|f(\S+):(\S+)( \S+)(( {types.RingEntry._REGEX.pattern})+)( \S+)?|f(\S+):(\S+)(( \S+)+)( \S+)?|e(\S+)(( \S+)+)( \S+)?( \S+)?|t(\S+)(( \S+)+)( \S+)?( \S+)?|t(\S+)(( ({t_1.T_1Option_._REGEX.pattern}))+)|c(\S+)(( \S+)+)( \S+)?( \S+)?'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
