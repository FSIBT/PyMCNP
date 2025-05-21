import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class F_1(DataOption):
    """
    Represents INP f variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        spheres: Detector points.
        nd: Total/average specified surfaces/cells option.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'spheres': types.Tuple[types.Sphere],
        'nd': types.String,
    }

    _REGEX = re.compile(
        rf'\Af(\d*[5]):(\S+)((?: {types.Sphere._REGEX.pattern})+?)( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        spheres: types.Tuple[types.Sphere],
        nd: types.String = None,
    ):
        """
        Initializes ``F_1``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            spheres: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999 and suffix.value % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if spheres is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, spheres)
        if nd is not None and not (nd == 'nd'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nd)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                spheres,
                nd,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.spheres: typing.Final[types.Tuple[types.Sphere]] = spheres
        self.nd: typing.Final[types.String] = nd


@dataclasses.dataclass
class FBuilder_1:
    """
    Builds ``F_1``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        spheres: Detector points.
        nd: Total/average specified surfaces/cells option.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    spheres: list[str] | list[types.Sphere]
    nd: str | types.String = None

    def build(self):
        """
        Builds ``FBuilder_1`` into ``F_1``.

        Returns:
            ``F_1`` for ``FBuilder_1``.
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

        if self.spheres:
            spheres = []
            for item in self.spheres:
                if isinstance(item, types.Sphere):
                    spheres.append(item)
                elif isinstance(item, str):
                    spheres.append(types.Sphere.from_mcnp(item))
                else:
                    spheres.append(item.build())
            spheres = types.Tuple(spheres)
        else:
            spheres = None

        nd = self.nd
        if isinstance(self.nd, types.String):
            nd = self.nd
        elif isinstance(self.nd, str):
            nd = types.String.from_mcnp(self.nd)

        return F_1(
            suffix=suffix,
            designator=designator,
            spheres=spheres,
            nd=nd,
        )

    @staticmethod
    def unbuild(ast: F_1):
        """
        Unbuilds ``F_1`` into ``FBuilder_1``

        Returns:
            ``FBuilder_1`` for ``F_1``.
        """

        return F_1(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            spheres=copy.deepcopy(ast.spheres),
            nd=copy.deepcopy(ast.nd),
        )
