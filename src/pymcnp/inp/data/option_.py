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
        rf'\A(?:phys:n( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|phys:p( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|phys:e( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|phys:h( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|dawwg((?: (?:{dawwg.DawwgOption_._REGEX.pattern}))+?)?'
        rf'|embed((?: (?:{embed.EmbedOption_._REGEX.pattern}))+?)?'
        rf'|embee(\d+)((?: (?:{embee.EmbeeOption_._REGEX.pattern}))+?)?'
        rf'|embeb(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|embem(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|embtb(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|embtm(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|embdb(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|embdf(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|otfdb((?: {types.Zaid._REGEX.pattern})+?)'
        rf'|totnu( {types.String._REGEX.pattern})?'
        rf'|awtab((?: {types.Substance._REGEX.pattern})+?)'
        rf'|mgopt( {types.String._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|thtme((?: {types.Real._REGEX.pattern})+?)'
        rf'|mphys( {types.String._REGEX.pattern})?'
        rf'|fmult( {types.Zaid._REGEX.pattern})((?: (?:{fmult.FmultOption_._REGEX.pattern}))+?)?'
        rf'|tropt((?: (?:{tropt.TroptOption_._REGEX.pattern}))+?)?'
        rf'|cosyp( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})((?: {types.Real._REGEX.pattern})+?)'
        rf'|bflcl((?: {types.Integer._REGEX.pattern})+?)'
        rf'|kcode( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|kopts((?: (?:{kopts.KoptsOption_._REGEX.pattern}))+?)?'
        rf'|notrn'
        rf'|kpert(\d+)((?: (?:{kpert.KpertOption_._REGEX.pattern}))+?)?'
        rf'|fmesh(\d+):(\S+)((?: (?:{fmesh.FmeshOption_._REGEX.pattern}))+?)?'
        rf'|spdtl( {types.String._REGEX.pattern})'
        rf'|esplt:(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|tsplt:(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|bbrem( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})((?: {types.Integer._REGEX.pattern})+?)'
        rf'|pikmt((?: {types.PhotonBias._REGEX.pattern})+?)'
        rf'|print((?: {types.Integer._REGEX.pattern})+?)?'
        rf'|talnp((?: {types.Integer._REGEX.pattern})+?)?'
        rf'|prdmp( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|ptrac((?: (?:{ptrac.PtracOption_._REGEX.pattern}))+?)?'
        rf'|histp( {types.Integer._REGEX.pattern})?((?: {types.Integer._REGEX.pattern})+?)?'
        rf'|files((?: {types.File._REGEX.pattern})+?)'
        rf'|area((?: {types.Real._REGEX.pattern})+?)'
        rf'|fill((?: {types.Integer._REGEX.pattern})+?)'
        rf'|uran((?: {types.Stochastic._REGEX.pattern})+?)'
        rf'|nonu((?: {types.Integer._REGEX.pattern})+?)?'
        rf'|void((?: {types.Integer._REGEX.pattern})+?)?'
        rf'|drxs((?: {types.Zaid._REGEX.pattern})+?)?'
        rf'|mode((?: {types.Designator._REGEX.pattern})+?)'
        rf'|phys:(\S+)( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|elpt((?: {types.Real._REGEX.pattern})+?)'
        rf'|cosy((?: {types.Integer._REGEX.pattern})+?)'
        rf'|bfld(\d+)( {types.String._REGEX.pattern})((?: (?:{bfld.BfldOption_._REGEX.pattern}))+?)?'
        rf'|sdef((?: (?:{sdef.SdefOption_._REGEX.pattern}))+?)?'
        rf'|ksrc((?: {types.Location._REGEX.pattern})+?)'
        rf'|hsrc( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|[*]c(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|pert(\d+):(\S+)((?: (?:{pert.PertOption_._REGEX.pattern}))+?)?'
        rf'|ksen(\d+)( {types.String._REGEX.pattern})((?: (?:{ksen.KsenOption_._REGEX.pattern}))+?)?'
        rf'|wwge((?: {types.Real._REGEX.pattern})+?)'
        rf'|wwgt((?: {types.Real._REGEX.pattern})+?)'
        rf'|mesh((?: (?:{mesh.MeshOption_._REGEX.pattern}))+?)?'
        rf'|ctme( {types.Integer._REGEX.pattern})'
        rf'|stop((?: (?:{stop.StopOption_._REGEX.pattern}))+?)?'
        rf'|rand((?: (?:{rand.RandOption_._REGEX.pattern}))+?)?'
        rf'|dbcn( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|lost( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|idum((?: {types.Integer._REGEX.pattern})+?)'
        rf'|rdum((?: {types.Real._REGEX.pattern})+?)'
        rf'|vol( no)?((?: {types.Real._REGEX.pattern})+?)'
        rf'|lat((?: {types.Integer._REGEX.pattern})+?)'
        rf'|act((?: (?:{act.ActOption_._REGEX.pattern}))+?)?'
        rf'|cut( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|lca( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|lcb( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|lcc( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|lea( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|leb( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|unc((?: {types.Integer._REGEX.pattern})+?)'
        rf'|ssw((?: {types.Integer._REGEX.pattern})+?)((?: {types.Integer._REGEX.pattern})+?)((?: (?:{ssw.SswOption_._REGEX.pattern}))+?)?'
        rf'|ssr((?: (?:{ssr.SsrOption_._REGEX.pattern}))+?)?'
        rf'|fip(\d+):(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|fir(\d+):(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|fic(\d+):(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|imp:(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|var((?: (?:{var.VarOption_._REGEX.pattern}))+?)?'
        rf'|wwe:(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|wwt:(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|wwn(\d+):(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|wwp:(\S+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|wwg( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Integer._REGEX.pattern})'
        rf'|ext:(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|fcl:(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|dxt:(\S+)( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
        rf'|dxc(\d+):(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|pwt((?: {types.Real._REGEX.pattern})+?)'
        rf'|nps( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})?'
        rf'|tr(\d+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})?'
        rf'|tr(\d+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})?'
        rf'|tr(\d+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})?'
        rf'|tr(\d+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})?'
        rf'|dm((?: {types.Zaid._REGEX.pattern})+?)'
        rf'|mt(\d+)( {types.String._REGEX.pattern})'
        rf'|mx(\d+):(\S+)((?: {types.Zaid._REGEX.pattern})+?)'
        rf'|xs(\d+)((?: {types.Substance._REGEX.pattern})+?)'
        rf'|si(\d+)( {types.String._REGEX.pattern})((?: {types.DistributionNumber._REGEX.pattern})+?)'
        rf'|si(\d+)( {types.String._REGEX.pattern})((?: {types.Real._REGEX.pattern})+?)'
        rf'|sp(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern})+?)'
        rf'|sp( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?'
        rf'|sb(\d+)( [dcvw])?((?: {types.Real._REGEX.pattern})+?)'
        rf'|sb( {types.Integer._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})?'
        rf'|ds(\d+)( {types.String._REGEX.pattern})?((?: {types.Real._REGEX.pattern})+?)'
        rf'|ds(\d+)((?: {types.IndependentDependent._REGEX.pattern})+?)'
        rf'|ds(\d+)((?: {types.IndependentDependent._REGEX.pattern})+?)'
        rf'|sc(\d+)((?: {types.String._REGEX.pattern})+?)'
        rf'|fc(\d+)( {types.String._REGEX.pattern})'
        rf'|fq(\d+)( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})'
        rf'|de(\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern})+?)'
        rf'|df(\d+)( (?:log|lin))?((?: {types.Real._REGEX.pattern})+?)'
        rf'|df(\d+)((?: (?:{df_1.Df_1Option_._REGEX.pattern}))+?)'
        rf'|em(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|tm(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|cm(\d+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|cf(\d+)((?: {types.Integer._REGEX.pattern})+?)'
        rf'|sf(\d+)((?: {types.Integer._REGEX.pattern})+?)'
        rf'|fs(\d+)((?: {types.Integer._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|sd((?: {types.Real._REGEX.pattern})+?)'
        rf'|fu(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|dd(\d+)((?: {types.Diagnostic._REGEX.pattern})+?)'
        rf'|pd(\d+):(\S+)((?: {types.Real._REGEX.pattern})+?)'
        rf'|za( {types.String._REGEX.pattern})?'
        rf'|zb( {types.String._REGEX.pattern})?'
        rf'|zc( {types.String._REGEX.pattern})?'
        rf'|zd( {types.String._REGEX.pattern})?'
        rf'|u((?: {types.Integer._REGEX.pattern})+?)'
        rf'|m(\d+)((?: {types.Substance._REGEX.pattern})+?)((?: (?:{m.MOption_._REGEX.pattern}))+?)?'
        rf'|f(\d*[12467]):(\S+)((?: {types.Integer._REGEX.pattern})+?)( t)?'
        rf'|f(\d*[5]):(\S+)((?: {types.Sphere._REGEX.pattern})+?)( nd)?'
        rf'|f(\d*[5])([xyz]):(\S+)((?: {types.Ring._REGEX.pattern})+?)( nd)?'
        rf'|f(\d*[8]):(\S+)((?: {types.Integer._REGEX.pattern})+?)( t)?'
        rf'|e(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|t(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|t(\d+)((?: (?:{t_1.T_1Option_._REGEX.pattern}))+?)'
        rf'|c(\d+)((?: {types.Real._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?)\Z'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
