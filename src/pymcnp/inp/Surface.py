import re
import copy
import typing
import dataclasses

from . import surface
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Surface(Card):
    """
    Represents INP surface cards.

    Attributes:
        number: INP surface number.
        transform: INP surface transformation.
        option: INP surface option.
        prefix: INP surface kind setting.
    """

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'option': surface.SurfaceOption,
    }

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)?( ({surface.SurfaceOption._REGEX.pattern}))\Z')

    def __init__(
        self,
        number: types.Integer,
        option: surface.SurfaceOption,
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes ``Surface``.

        Parameters:
            number: INP surface number.
            transform: INP surface transformation.
            option: INP surface option.
            prefix: INP surface kind setting.

        Returns:
            ``Surface``.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None or not (1 <= number.value <= 99_999_999 if not transform else 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)
        if transform is not None and not (0 <= transform.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, transform)
        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, option)
        if prefix is not None and prefix not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self.number: typing.Final[types.Integer] = number
        self.transform: typing.Final[types.Integer] = transform
        self.option: typing.Final[surface.SurfaceOption] = option
        self.prefix: typing.Final[str] = prefix

    def to_mcnp(self):
        """
        Generates INP from ``Surface``.

        Returns:
            INP surface card.
        """

        return _parser.postprocess_continuation_line(
            f'{self.prefix or ""}{self.number} {self.transform or ""} {self.option}'
        )

    def draw(self):
        """
        Generates ``Visualization`` from ``Surface``.

        Returns:
            ``pyvista.PolySurface`` for ``Surface``
        """

        return self.option.draw()


@dataclasses.dataclass
class SurfaceBuilder:
    """
    Builds ``Surface``.

    Attributes:
        number: INP surface number.
        transform: INP surface transformation.
        option: INP surface option.
        prefix: INP surface kind setting.
    """

    number: str | int | types.Integer
    option: (
        str
        | surface.SurfaceOption
        | surface.PBuilder_0
        | surface.PBuilder_1
        | surface.PxBuilder
        | surface.PyBuilder
        | surface.PzBuilder
        | surface.SoBuilder
        | surface.SBuilder
        | surface.SxBuilder
        | surface.SyBuilder
        | surface.SzBuilder
        | surface.C_xBuilder
        | surface.C_yBuilder
        | surface.C_zBuilder
        | surface.CxBuilder
        | surface.CyBuilder
        | surface.CzBuilder
        | surface.K_xBuilder
        | surface.K_yBuilder
        | surface.K_zBuilder
        | surface.KxBuilder
        | surface.KyBuilder
        | surface.KzBuilder
        | surface.SqBuilder
        | surface.GqBuilder
        | surface.TxBuilder
        | surface.TyBuilder
        | surface.TzBuilder
        | surface.XBuilder
        | surface.YBuilder
        | surface.ZBuilder
        | surface.BoxBuilder
        | surface.RppBuilder
        | surface.SphBuilder
        | surface.RccBuilder
        | surface.RhpBuilder
        | surface.RecBuilder
        | surface.TrcBuilder
        | surface.EllBuilder
        | surface.WedBuilder
        | surface.ArbBuilder
    )

    transform: str | int | types.Integer = None
    prefix: str = None

    def __and__(a, b):
        """
        Unites ``SurfaceBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``SurfaceBuilder`` union.
        """

        return types.GeometryBuilder(infix=f'{a.number}:{b.number}')

    def __or__(a, b):
        """
        Intersects ``SurfaceBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``SurfaceBuilder`` intersection.
        """

        return types.GeometryBuilder(infix=f'{a.number} {b.number}')

    def __neg__(self):
        """
        Negatives ``SurfaceBuilder``.

        Returns:
            ``SurfaceBuilder`` negative.
        """

        return types.GeometryBuilder(infix=f'-{self.number}')

    def __pos__(self):
        """
        Positives ``SurfaceBuilder``.

        Returns:
            ``SurfaceBuilder`` positive.
        """

        return types.GeometryBuilder(infix=f'+{self.number}')

    def __invert__(self):
        """
        Inverts ``SurfaceBuilder``.

        Returns:
            ``SurfaceBuilder`` complement.
        """

        return types.GeometryBuilder(infix=f'#{self.number}')

    def build(self):
        """
        Builds ``SurfaceBuilder`` into ``Surface``.

        Returns:
            ``Surface`` for ``SurfaceBuilder``.
        """

        if isinstance(self.number, types.Integer):
            number = self.number
        elif isinstance(self.number, int):
            number = types.Integer(self.number)
        elif isinstance(self.number, str):
            number = types.Integer.from_mcnp(self.number)

        transform = None
        if isinstance(self.transform, types.Integer):
            transform = self.transform
        elif isinstance(self.transform, int):
            transform = types.Integer(self.transform)
        elif isinstance(self.transform, str):
            transform = types.Integer.from_mcnp(self.transform)

        prefix = None
        if isinstance(self.prefix, str):
            prefix = self.prefix

        if isinstance(self.option, str):
            option = types.Surface.from_mcnp(self.option)
        elif isinstance(self.option, surface.SurfaceOption):
            option = self.option
        else:
            option = self.option.build()

        return Surface(
            number=number,
            option=option,
            transform=transform,
            prefix=prefix,
        )

    @staticmethod
    def unbuild(ast: Surface):
        """
        Unbuilds ``Surface`` into ``SurfaceBuilder``

        Returns:
            ``SurfaceBuilder`` for ``Surface``.
        """

        if isinstance(ast.option, surface.P_0):
            option = surface.PBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, surface.P_1):
            option = surface.PBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, surface.Px):
            option = surface.PxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Py):
            option = surface.PyBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Pz):
            option = surface.PzBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.So):
            option = surface.SoBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.S):
            option = surface.SBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Sx):
            option = surface.SxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Sy):
            option = surface.SyBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Sz):
            option = surface.SzBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.C_x):
            option = surface.C_xBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.C_y):
            option = surface.C_yBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.C_z):
            option = surface.C_zBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Cx):
            option = surface.CxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Cy):
            option = surface.CyBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Cz):
            option = surface.CzBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.K_x):
            option = surface.K_xBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.K_y):
            option = surface.K_yBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.K_z):
            option = surface.K_zBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Kx):
            option = surface.KxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Ky):
            option = surface.KyBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Kz):
            option = surface.KzBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Sq):
            option = surface.SqBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Gq):
            option = surface.GqBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Tx):
            option = surface.TxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Ty):
            option = surface.TyBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Tz):
            option = surface.TzBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.X):
            option = surface.XBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Y):
            option = surface.YBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Z):
            option = surface.ZBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Box):
            option = surface.BoxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Rpp):
            option = surface.RppBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Sph):
            option = surface.SphBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Rcc):
            option = surface.RccBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Rhp):
            option = surface.RhpBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Rec):
            option = surface.RecBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Trc):
            option = surface.TrcBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Ell):
            option = surface.EllBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Wed):
            option = surface.WedBuilder.unbuild(ast.option)
        elif isinstance(ast.option, surface.Arb):
            option = surface.ArbBuilder.unbuild(ast.option)

        return SurfaceBuilder(
            number=copy.deepcopy(ast.number),
            option=option,
            transform=copy.deepcopy(ast.transform),
            prefix=copy.deepcopy(ast.prefix),
        )
