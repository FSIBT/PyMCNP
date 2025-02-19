import re
import typing


from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class TrEntry_Rotation(_entry.TrEntry_):
    """
    Represents INP data card data option rotation entries.

    Attributes:
        xx: Rotation matrix xx' component.
        xy: Rotation matrix xy' component.
        xz: Rotation matrix xz' component.
        yx: Rotation matrix yx' component.
        yy: Rotation matrix yy' component.
        yz: Rotation matrix yz' component.
        zx: Rotation matrix zx' component.
        zy: Rotation matrix zy' component.
        zz: Rotation matrix zz' component.
    """

    _REGEX = re.compile(
        r'((?:\A)\S+)((?: )\S+)((?: )\S+)((?: )\S+)((?: )\S+)((?: )\S+)((?: )\S+)((?: )\S+)((?: )\S+)(?:\Z)'
    )

    def __init__(
        self,
        xx: types.Real,
        xy: types.Real,
        xz: types.Real,
        yx: types.Real,
        yy: types.Real,
        yz: types.Real,
        zx: types.Real,
        zy: types.Real,
        zz: types.Real,
    ):
        """
        Initializes ``TrEntry_Rotation``.

        Parameters:
            xx: Rotation matrix xx' component.
            xy: Rotation matrix xy' component.
            xz: Rotation matrix xz' component.
            yx: Rotation matrix yx' component.
            yy: Rotation matrix yy' component.
            yz: Rotation matrix yz' component.
            zx: Rotation matrix zx' component.
            zy: Rotation matrix zy' component.
            zz: Rotation matrix zz' component.

        Returns:
            ``TrEntryRotation``.

        Raises:
            InpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        if xx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, xx)
        if xy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, xy)
        if xz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, xz)
        if yx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, yx)
        if yy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, yy)
        if yz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, yz)
        if zx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, zx)
        if zy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, zy)
        if zz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_ENTRY_VALUE, zz)

        self.parameters: typing.Final[tuple[any]] = tuple([xx, xy, xz, yx, yy, yz, zx, zy, zz])
        self.xx: typing.Final[types.Real] = xx
        self.xy: typing.Final[types.Real] = xy
        self.xz: typing.Final[types.Real] = xz
        self.yx: typing.Final[types.Real] = yx
        self.yy: typing.Final[types.Real] = yy
        self.yz: typing.Final[types.Real] = yz
        self.zx: typing.Final[types.Real] = zx
        self.zy: typing.Final[types.Real] = zy
        self.zz: typing.Final[types.Real] = zz

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TrEntry_Rotation`` from INP.

        Parameters:
            INP for ``TrEntry_Rotation``.

        Returns:
            ``TrEntry_Rotation``.

        Raises:
            InpError: SYNTAX_TR_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = TrEntry_Rotation._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_TR_ENTRY, source)

        xx = types.Real.from_mcnp(tokens[1].strip())
        xy = types.Real.from_mcnp(tokens[2].strip())
        xz = types.Real.from_mcnp(tokens[3].strip())
        yx = types.Real.from_mcnp(tokens[4].strip())
        yy = types.Real.from_mcnp(tokens[5].strip())
        yz = types.Real.from_mcnp(tokens[6].strip())
        zx = types.Real.from_mcnp(tokens[7].strip())
        zy = types.Real.from_mcnp(tokens[8].strip())
        zz = types.Real.from_mcnp(tokens[9].strip())

        return TrEntry_Rotation(xx, xy, xz, yx, yy, yz, zx, zy, zz)
