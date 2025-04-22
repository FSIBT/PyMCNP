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

from .._option import Option
from ...utils import types


class DataOption(Option):
    """
    Represents generic INP data options.
    """

    _KEYWORD = ''
    _SUBCLASSES = {}
    _REGEX = re.compile(
        r'\A(?:'
        rf'phys:n( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|phys:p( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|phys:e( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?'
        rf'|phys:h( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?'
        rf'|dawwg((?: (?:{dawwg.DawwgOption._REGEX.pattern}))+?)?'
        rf'|embed((?: (?:{embed.EmbedOption._REGEX.pattern}))+?)?'
        rf'|embee(\d+)((?: (?:{embee.EmbeeOption._REGEX.pattern}))+?)?'
        rf'|embeb(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|embem(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|embtb(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|embtm(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|embdb(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|embdf(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|otfdb((?: {types.Zaid._REGEX.pattern})+?)'
        rf'|totnu( {types.String._REGEX.pattern})?'
        rf'|awtab((?: {types.Substance._REGEX.pattern})+?)'
        rf'|mgopt( {types.String._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|thtme((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|mphys( {types.String._REGEX.pattern})?'
        rf'|fmult( {types.Zaid._REGEX.pattern})((?: (?:{fmult.FmultOption._REGEX.pattern}))+?)?'
        rf'|tropt((?: (?:{tropt.TroptOption._REGEX.pattern}))+?)?'
        rf'|cosyp( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|bflcl((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|kcode( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|kopts((?: (?:{kopts.KoptsOption._REGEX.pattern}))+?)?'
        rf'|notrn'
        rf'|kpert(\d+)((?: (?:{kpert.KpertOption._REGEX.pattern}))+?)?'
        rf'|fmesh(\d+):(\S+)((?: (?:{fmesh.FmeshOption._REGEX.pattern}))+?)?'
        rf'|spdtl( {types.String._REGEX.pattern})'
        rf'|esplt:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|tsplt:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|bbrem( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|pikmt((?: {types.PhotonBias._REGEX.pattern})+?)'
        rf'|print((?: {types.IntegerOrJump._REGEX.pattern})+?)?'
        rf'|talnp((?: {types.IntegerOrJump._REGEX.pattern})+?)?'
        rf'|prdmp( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|ptrac((?: (?:{ptrac.PtracOption._REGEX.pattern}))+?)?'
        rf'|histp( {types.IntegerOrJump._REGEX.pattern})?((?: {types.IntegerOrJump._REGEX.pattern})+?)?'
        rf'|files((?: {types.File._REGEX.pattern})+?)'
        rf'|area((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|fill((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|uran((?: {types.Stochastic._REGEX.pattern})+?)'
        rf'|nonu((?: {types.IntegerOrJump._REGEX.pattern})+?)?'
        rf'|void((?: {types.IntegerOrJump._REGEX.pattern})+?)?'
        rf'|drxs((?: {types.Zaid._REGEX.pattern})+?)?'
        rf'|mode((?: {types.Designator._REGEX.pattern})+?)'
        rf'|phys:(\S+)( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?'
        rf'|elpt((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|cosy((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|bfld(\d+)( {types.String._REGEX.pattern})((?: (?:{bfld.BfldOption._REGEX.pattern}))+?)?'
        rf'|sdef((?: (?:{sdef.SdefOption._REGEX.pattern}))+?)?'
        rf'|ksrc((?: {types.Location._REGEX.pattern})+?)'
        rf'|hsrc( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|[*]c(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|pert(\d+):(\S+)((?: (?:{pert.PertOption._REGEX.pattern}))+?)?'
        rf'|ksen(\d+)( {types.String._REGEX.pattern})((?: (?:{ksen.KsenOption._REGEX.pattern}))+?)?'
        rf'|wwge((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|wwgt((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|mesh((?: (?:{mesh.MeshOption._REGEX.pattern}))+?)?'
        rf'|ctme( {types.IntegerOrJump._REGEX.pattern})'
        rf'|stop((?: (?:{stop.StopOption._REGEX.pattern}))+?)?'
        rf'|rand((?: (?:{rand.RandOption._REGEX.pattern}))+?)?'
        rf'|dbcn( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|lost( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|idum((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|rdum((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|vol( no)?((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|lat((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|act((?: (?:{act.ActOption._REGEX.pattern}))+?)?'
        rf'|cut( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|lca( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|lcb( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|lcc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|lea( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|leb( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|unc((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|ssw((?: {types.IntegerOrJump._REGEX.pattern})+?)((?: {types.IntegerOrJump._REGEX.pattern})+?)((?: (?:{ssw.SswOption._REGEX.pattern}))+?)?'
        rf'|ssr((?: (?:{ssr.SsrOption._REGEX.pattern}))+?)?'
        rf'|fip(\d+):(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|fir(\d+):(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|fic(\d+):(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|imp:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|var((?: (?:{var.VarOption._REGEX.pattern}))+?)?'
        rf'|wwe:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|wwt:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|wwn(\d+):(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|wwp:(\S+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|wwg( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.Jump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})'
        rf'|ext:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|fcl:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|dxt:(\S+)( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.Shell._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})'
        rf'|dxc(\d+):(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|pwt((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|nps( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})?'
        rf'|tr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|tr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|tr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|tr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|tr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?'
        rf'|dm((?: {types.Zaid._REGEX.pattern})+?)'
        rf'|mt(\d+)( {types.String._REGEX.pattern})'
        rf'|mx(\d+):(\S+)((?: {types.Zaid._REGEX.pattern})+?)'
        rf'|xs(\d+)((?: {types.Substance._REGEX.pattern})+?)'
        rf'|si(\d+)( {types.String._REGEX.pattern})((?: {types.DistributionNumber._REGEX.pattern})+?)'
        rf'|si(\d+)( {types.String._REGEX.pattern})((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|sp(\d+)( [dcvw])?((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|sp( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})?'
        rf'|sb(\d+)( [dcvw])?((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|sb( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})?'
        rf'|ds(\d+)(  [hls])?((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|ds(\d+) t((?: {types.IndependentDependent._REGEX.pattern})+?)'
        rf'|ds(\d+) q((?: {types.IndependentDependent._REGEX.pattern})+?)'
        rf'|sc(\d+)((?: {types.String._REGEX.pattern})+?)'
        rf'|fc(\d+)( [\S\s]+)'
        rf'|fq(\d+)( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})( {types.String._REGEX.pattern})'
        rf'|de(\d+)( (?:log|lin))?((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|df(\d+)( (?:log|lin))?((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|fm(\d+)( [\S\s]+)'
        rf'|df(\d+)((?: (?:{df_1.Df_1Option._REGEX.pattern}))+?)'
        rf'|em(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|tm(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|cm(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|cf(\d+)((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|sf(\d+)((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|fs(\d+)((?: {types.IntegerOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|sd((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|fu(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( nt)?( c)?'
        rf'|ft(\d+)( [\S\s]+)'
        rf'|dd(\d+)((?: {types.Diagnostic._REGEX.pattern})+?)'
        rf'|pd(\d+):(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)'
        rf'|za( {types.String._REGEX.pattern})?'
        rf'|zb( {types.String._REGEX.pattern})?'
        rf'|zc( {types.String._REGEX.pattern})?'
        rf'|zd( {types.String._REGEX.pattern})?'
        rf'|u((?: {types.IntegerOrJump._REGEX.pattern})+?)'
        rf'|m(\d+)((?: {types.Substance._REGEX.pattern})+?)((?: (?:{m.MOption._REGEX.pattern}))+?)?'
        rf'|f(\d*[123467]):(\S+)((?: {types.IntegerOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?'
        rf'|f(\d*[5]):(\S+)((?: {types.Sphere._REGEX.pattern})+?)( {types.String._REGEX.pattern})?'
        rf'|f(\d*[5])([xyz]):(\S+)((?: {types.Ring._REGEX.pattern})+?)( {types.String._REGEX.pattern})?'
        rf'|f(\d*[8]):(\S+)((?: {types.IntegerOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?'
        rf'|e(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|t(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        rf'|t(\d+)((?: (?:{t_1.T_1Option._REGEX.pattern}))+?)'
        rf'|c(\d+)((?: {types.RealOrJump._REGEX.pattern})+?)( {types.String._REGEX.pattern})?( {types.String._REGEX.pattern})?'
        r')\Z'
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
