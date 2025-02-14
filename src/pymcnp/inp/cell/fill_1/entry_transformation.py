import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class Fill1Entry_Transformation(_entry.Fill1Entry_):
    """
    Represents INP cell card cell option transformation entries.

    Attributes:
        o1: Fill displacement vector x-coordinate.
        o2: Fill displacement vector y-coordinate.
        o3: Fill displacement vector z-coordinate.
        xx: Fill rotation matrix xx-entry.
        xy: Fill rotation matrix xy-entry.
        xz: Fill rotation matrix xz-entry.
        yx: Fill rotation matrix yx-entry.
        yy: Fill rotation matrix yy-entry.
        yz: Fill rotation matrix yz-entry.
        zx: Fill rotation matrix zx-entry.
        zy: Fill rotation matrix zy-entry.
        zz: Fill rotation matrix zz-entry.
        m: Fill coordinate system setting.
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
        Initializes ``Fill1Entry_Transformation``.

        Parameters:
            o1: Fill displacement vector x-coordinate.
            o2: Fill displacement vector y-coordinate.
            o3: Fill displacement vector z-coordinate.
            xx: Fill rotation matrix xx-entry.
            xy: Fill rotation matrix xy-entry.
            xz: Fill rotation matrix xz-entry.
            yx: Fill rotation matrix yx-entry.
            yy: Fill rotation matrix yy-entry.
            yz: Fill rotation matrix yz-entry.
            zx: Fill rotation matrix zx-entry.
            zy: Fill rotation matrix zy-entry.
            zz: Fill rotation matrix zz-entry.
            m: Fill coordinate system setting.

        Returns:
            ``Fill1EntryTransformation``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, yy)
        if yz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, yz)
        if zx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, zx)
        if zy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, zy)
        if zz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, zz)
        if m is None or m not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_OPTION_VALUE, m)

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
        Generates ``Fill1Entry_Transformation`` from INP.

        Parameters:
            INP for ``Fill1Entry_Transformation``.

        Returns:
            ``Fill1Entry_Transformation``.

        Raises:
            McnpError: SYNTAX_FILL_1_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Fill1Entry_Transformation._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FILL_1_ENTRY, source)

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

        return Fill1Entry_Transformation(o1, o2, o3, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)
