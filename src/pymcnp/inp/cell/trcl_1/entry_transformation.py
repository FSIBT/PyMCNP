import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class Trcl1Entry_Transformation(_entry.Trcl1Entry_):
    """
    Represents INP cell card cell option transformation entries.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        yz: Transformation rotation matrix yz-entry.
        zx: Transformation rotation matrix zx-entry.
        zy: Transformation rotation matrix zy-entry.
        zz: Transformation rotation matrix zz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(
        r'( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)'
    )

    def __init__(
        self,
        o1: types.Real,
        o2: types.Real,
        o3: types.Real,
        xx: types.Real,
        xy: types.Real,
        xz: types.Real,
        yx: types.Real,
        yy: types.Real,
        yz: types.Real,
        zx: types.Real,
        zy: types.Real,
        zz: types.Real,
        m: types.Real,
    ):
        """
        Initializes ``Trcl1Entry_Transformation``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            yz: Transformation rotation matrix yz-entry.
            zx: Transformation rotation matrix zx-entry.
            zy: Transformation rotation matrix zy-entry.
            zz: Transformation rotation matrix zz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Trcl1EntryTransformation``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if o1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, o1)
        if o2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, o2)
        if o3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, o3)
        if xx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, xx)
        if xy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, xy)
        if xz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, xz)
        if yx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, yx)
        if yy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, yy)
        if yz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, yz)
        if zx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, zx)
        if zy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, zy)
        if zz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, zz)
        if m is None or m not in {-1, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, m)

        self.parameters: typing.Final[tuple[any]] = types._Tuple(
            [o1, o2, o3, xx, xy, xz, yx, yy, yz, zx, zy, zz, m]
        )
        self.o1: typing.Final[types.Real] = o1
        self.o2: typing.Final[types.Real] = o2
        self.o3: typing.Final[types.Real] = o3
        self.xx: typing.Final[types.Real] = xx
        self.xy: typing.Final[types.Real] = xy
        self.xz: typing.Final[types.Real] = xz
        self.yx: typing.Final[types.Real] = yx
        self.yy: typing.Final[types.Real] = yy
        self.yz: typing.Final[types.Real] = yz
        self.zx: typing.Final[types.Real] = zx
        self.zy: typing.Final[types.Real] = zy
        self.zz: typing.Final[types.Real] = zz
        self.m: typing.Final[types.Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Trcl1Entry_Transformation`` from INP.

        Parameters:
            INP for ``Trcl1Entry_Transformation``.

        Returns:
            ``Trcl1Entry_Transformation``.

        Raises:
            InpError: SYNTAX_TRCL_1_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Trcl1Entry_Transformation._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        o1 = types.Real.from_mcnp(tokens[1])
        o2 = types.Real.from_mcnp(tokens[2])
        o3 = types.Real.from_mcnp(tokens[3])
        xx = types.Real.from_mcnp(tokens[4])
        xy = types.Real.from_mcnp(tokens[5])
        xz = types.Real.from_mcnp(tokens[6])
        yx = types.Real.from_mcnp(tokens[7])
        yy = types.Real.from_mcnp(tokens[8])
        yz = types.Real.from_mcnp(tokens[9])
        zx = types.Real.from_mcnp(tokens[10])
        zy = types.Real.from_mcnp(tokens[11])
        zz = types.Real.from_mcnp(tokens[12])
        m = types.Real.from_mcnp(tokens[13])

        return Trcl1Entry_Transformation(o1, o2, o3, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)
