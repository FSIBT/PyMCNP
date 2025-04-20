import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class F_1(DataOption_, keyword='f'):
    """
    Represents INP f variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        spheres: Detector points.
        nd: Total/average specified surfaces/cells option.
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if spheres is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, spheres)

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

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        spheres = []
        for item in self.spheres:
            if isinstance(item, types.Sphere):
                spheres.append(item)
            elif isinstance(item, str):
                spheres.append(types.Sphere.from_mcnp(item))
            else:
                spheres.append(item.build())
        spheres = types.Tuple(spheres)

        nd = None
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
