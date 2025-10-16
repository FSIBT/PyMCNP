import re
import typing

from . import _type
from .Real import Real
from .Integer import Integer
from .. import errors


class Transformation_0(_type.Type):
    """
    Represents MCNP transformations.

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
        r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        yz: Real,
        zx: Real,
        zy: Real,
        zz: Real,
        m: Integer = None,
    ):
        """
        Initializes `Transformation_0`.

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
            `Transformation_0`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yy)
        if yz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yz)
        if zx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, zx)
        if zy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, zy)
        if zz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, zz)
        if m is not None and m.value not in {-1, 1}:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.yz: typing.Final[Real] = yz
        self.zx: typing.Final[Real] = zx
        self.zy: typing.Final[Real] = zy
        self.zz: typing.Final[Real] = zz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Transformation_0` from INP.

        Parameters:
            INP for `Transformation_0`.

        Returns:
            `Transformation_0`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Transformation_0._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        yz = Real.from_mcnp(tokens[9])
        zx = Real.from_mcnp(tokens[10])
        zy = Real.from_mcnp(tokens[11])
        zz = Real.from_mcnp(tokens[12])
        m = Integer.from_mcnp(tokens[13]) if tokens[13] else None

        return Transformation_0(o1, o2, o3, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)

    def to_mcnp(self):
        """
        Generates INP from `Transformation_0`.

        Returns:
            INP for `Transformation_0`.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.zx} {self.zy} {self.zz} {self.m if self.m is not None else ""}'


class Transformation_1(_type.Type):
    """
    Represents MCNP transformations.

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
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z', re.IGNORECASE)

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        yz: Real,
        m: Integer = None,
    ):
        """
        Initializes `Transformation_1`.

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
            m: Transformation coordinate system setting.

        Returns:
            `Transformation_1`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yy)
        if yz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yz)
        if m is not None and m.value not in {-1, 1}:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.yz: typing.Final[Real] = yz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Transformation_1` from INP.

        Parameters:
            INP for `Transformation_1`.

        Returns:
            `Transformation_1`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Transformation_1._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        yz = Real.from_mcnp(tokens[9])
        m = Integer.from_mcnp(tokens[10]) if tokens[10] else None

        return Transformation_1(o1, o2, o3, xx, xy, xz, yx, yy, yz, m)

    def to_mcnp(self):
        """
        Generates INP from `Transformation_1`.

        Returns:
            INP for `Transformation_1`.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.m if self.m is not None else ""}'


class Transformation_2(_type.Type):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z', re.IGNORECASE)

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        m: Integer = None,
    ):
        """
        Initializes `Transformation_2`.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            m: Transformation coordinate system setting.

        Returns:
            `Transformation_2`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, yy)
        if m is not None and m.value not in {-1, 1}:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Transformation_2` from INP.

        Parameters:
            INP for `Transformation_2`.

        Returns:
            `Transformation_2`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Transformation_2._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        m = Integer.from_mcnp(tokens[9]) if tokens[9] else None

        return Transformation_2(o1, o2, o3, xx, xy, xz, yx, yy, m)

    def to_mcnp(self):
        """
        Generates INP from `Transformation_2`.

        Returns:
            INP for `Transformation_2`.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.m if self.m is not None else ""}'


class Transformation_3(_type.Type):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z', re.IGNORECASE)

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        m: Integer = None,
    ):
        """
        Initializes `Transformation_3`.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            m: Transformation coordinate system setting.

        Returns:
            `Transformation_3`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, xz)
        if m is not None and m.value not in {-1, 1}:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Transformation_3` from INP.

        Parameters:
            INP for `Transformation_3`.

        Returns:
            `Transformation_3`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Transformation_3._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        m = Integer.from_mcnp(tokens[7]) if tokens[7] else None

        return Transformation_3(o1, o2, o3, xx, xy, xz, m)

    def to_mcnp(self):
        """
        Generates INP from `Transformation_3`.

        Returns:
            INP for `Transformation_3`.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.m if self.m is not None else ""}'


class Transformation_4(_type.Type):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'\A(?:[(])?([\d.ed+-]+) ([\d.ed+-]+) ([\d.ed+-]*)(?: ([\d.ed+-]*))?(?:[)])?\Z', re.IGNORECASE)

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        m: Integer = None,
    ):
        """
        Initializes `Transformation_4`.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            m: Transformation coordinate system setting.

        Returns:
            `Transformation_4`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, o3)
        if m is not None and m.value not in {-1, 1}:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Transformation_4` from INP.

        Parameters:
            INP for `Transformation_4`.

        Returns:
            `Transformation_4`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Transformation_4._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        m = Integer.from_mcnp(tokens[4]) if tokens[4] else None

        return Transformation_4(o1, o2, o3, m)

    def to_mcnp(self):
        """
        Generates INP from `Transformation_4`.

        Returns:
            INP for `Transformation_4`.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.m if self.m is not None else ""}'
