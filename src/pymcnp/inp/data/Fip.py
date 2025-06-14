import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Fip(_option.DataOption):
    """
    Represents INP fip elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        x1: Pinhole center x-coordinate.
        y1: Pinhole center y-coordinate.
        z1: Pinhole center z-coordinate.
        ro: Pinhole exclusion radius.
        x2: Reference direction x-coordinate.
        y2: Reference direction y-coordinate.
        z2: Reference direction z-coordinate.
        f1: Cylindrical collimator radius.
        f2: Pinhole radius in the direction perpendiuclar to the reference direction.
        f3: Distance between pinhole and and detector grid.
    """

    _KEYWORD = 'fip'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'x1': types.Real,
        'y1': types.Real,
        'z1': types.Real,
        'ro': types.Real,
        'x2': types.Real,
        'y2': types.Real,
        'z2': types.Real,
        'f1': types.Real,
        'f2': types.Real,
        'f3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Afip(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        x1: types.Real,
        y1: types.Real,
        z1: types.Real,
        ro: types.Real,
        x2: types.Real,
        y2: types.Real,
        z2: types.Real,
        f1: types.Real,
        f2: types.Real,
        f3: types.Real,
    ):
        """
        Initializes ``Fip``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            x1: Pinhole center x-coordinate.
            y1: Pinhole center y-coordinate.
            z1: Pinhole center z-coordinate.
            ro: Pinhole exclusion radius.
            x2: Reference direction x-coordinate.
            y2: Reference direction y-coordinate.
            z2: Reference direction z-coordinate.
            f1: Cylindrical collimator radius.
            f2: Pinhole radius in the direction perpendiuclar to the reference direction.
            f3: Distance between pinhole and and detector grid.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999 and suffix.value % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x1)
        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y1)
        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z1)
        if ro is None or not (ro.value == 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ro)
        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x2)
        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y2)
        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z2)
        if f1 is None or not (f1.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f1)
        if f2 is None or not (f2.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f2)
        if f3 is None or not (f3.value >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, f3)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x1,
                y1,
                z1,
                ro,
                x2,
                y2,
                z2,
                f1,
                f2,
                f3,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.x1: typing.Final[types.Real] = x1
        self.y1: typing.Final[types.Real] = y1
        self.z1: typing.Final[types.Real] = z1
        self.ro: typing.Final[types.Real] = ro
        self.x2: typing.Final[types.Real] = x2
        self.y2: typing.Final[types.Real] = y2
        self.z2: typing.Final[types.Real] = z2
        self.f1: typing.Final[types.Real] = f1
        self.f2: typing.Final[types.Real] = f2
        self.f3: typing.Final[types.Real] = f3


@dataclasses.dataclass
class FipBuilder(_option.DataOptionBuilder):
    """
    Builds ``Fip``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        x1: Pinhole center x-coordinate.
        y1: Pinhole center y-coordinate.
        z1: Pinhole center z-coordinate.
        ro: Pinhole exclusion radius.
        x2: Reference direction x-coordinate.
        y2: Reference direction y-coordinate.
        z2: Reference direction z-coordinate.
        f1: Cylindrical collimator radius.
        f2: Pinhole radius in the direction perpendiuclar to the reference direction.
        f3: Distance between pinhole and and detector grid.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    x1: str | float | types.Real
    y1: str | float | types.Real
    z1: str | float | types.Real
    ro: str | float | types.Real
    x2: str | float | types.Real
    y2: str | float | types.Real
    z2: str | float | types.Real
    f1: str | float | types.Real
    f2: str | float | types.Real
    f3: str | float | types.Real

    def build(self):
        """
        Builds ``FipBuilder`` into ``Fip``.

        Returns:
            ``Fip`` for ``FipBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        x1 = self.x1
        if isinstance(self.x1, types.Real):
            x1 = self.x1
        elif isinstance(self.x1, float) or isinstance(self.x1, int):
            x1 = types.Real(self.x1)
        elif isinstance(self.x1, str):
            x1 = types.Real.from_mcnp(self.x1)

        y1 = self.y1
        if isinstance(self.y1, types.Real):
            y1 = self.y1
        elif isinstance(self.y1, float) or isinstance(self.y1, int):
            y1 = types.Real(self.y1)
        elif isinstance(self.y1, str):
            y1 = types.Real.from_mcnp(self.y1)

        z1 = self.z1
        if isinstance(self.z1, types.Real):
            z1 = self.z1
        elif isinstance(self.z1, float) or isinstance(self.z1, int):
            z1 = types.Real(self.z1)
        elif isinstance(self.z1, str):
            z1 = types.Real.from_mcnp(self.z1)

        ro = self.ro
        if isinstance(self.ro, types.Real):
            ro = self.ro
        elif isinstance(self.ro, float) or isinstance(self.ro, int):
            ro = types.Real(self.ro)
        elif isinstance(self.ro, str):
            ro = types.Real.from_mcnp(self.ro)

        x2 = self.x2
        if isinstance(self.x2, types.Real):
            x2 = self.x2
        elif isinstance(self.x2, float) or isinstance(self.x2, int):
            x2 = types.Real(self.x2)
        elif isinstance(self.x2, str):
            x2 = types.Real.from_mcnp(self.x2)

        y2 = self.y2
        if isinstance(self.y2, types.Real):
            y2 = self.y2
        elif isinstance(self.y2, float) or isinstance(self.y2, int):
            y2 = types.Real(self.y2)
        elif isinstance(self.y2, str):
            y2 = types.Real.from_mcnp(self.y2)

        z2 = self.z2
        if isinstance(self.z2, types.Real):
            z2 = self.z2
        elif isinstance(self.z2, float) or isinstance(self.z2, int):
            z2 = types.Real(self.z2)
        elif isinstance(self.z2, str):
            z2 = types.Real.from_mcnp(self.z2)

        f1 = self.f1
        if isinstance(self.f1, types.Real):
            f1 = self.f1
        elif isinstance(self.f1, float) or isinstance(self.f1, int):
            f1 = types.Real(self.f1)
        elif isinstance(self.f1, str):
            f1 = types.Real.from_mcnp(self.f1)

        f2 = self.f2
        if isinstance(self.f2, types.Real):
            f2 = self.f2
        elif isinstance(self.f2, float) or isinstance(self.f2, int):
            f2 = types.Real(self.f2)
        elif isinstance(self.f2, str):
            f2 = types.Real.from_mcnp(self.f2)

        f3 = self.f3
        if isinstance(self.f3, types.Real):
            f3 = self.f3
        elif isinstance(self.f3, float) or isinstance(self.f3, int):
            f3 = types.Real(self.f3)
        elif isinstance(self.f3, str):
            f3 = types.Real.from_mcnp(self.f3)

        return Fip(
            suffix=suffix,
            designator=designator,
            x1=x1,
            y1=y1,
            z1=z1,
            ro=ro,
            x2=x2,
            y2=y2,
            z2=z2,
            f1=f1,
            f2=f2,
            f3=f3,
        )

    @staticmethod
    def unbuild(ast: Fip):
        """
        Unbuilds ``Fip`` into ``FipBuilder``

        Returns:
            ``FipBuilder`` for ``Fip``.
        """

        return FipBuilder(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            x1=copy.deepcopy(ast.x1),
            y1=copy.deepcopy(ast.y1),
            z1=copy.deepcopy(ast.z1),
            ro=copy.deepcopy(ast.ro),
            x2=copy.deepcopy(ast.x2),
            y2=copy.deepcopy(ast.y2),
            z2=copy.deepcopy(ast.z2),
            f1=copy.deepcopy(ast.f1),
            f2=copy.deepcopy(ast.f2),
            f3=copy.deepcopy(ast.f3),
        )
