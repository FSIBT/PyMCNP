import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class F_2(DataOption, keyword='f'):
    """
    Represents INP f variation #2 elements.

    Attributes:
        suffix: Data card option suffix.
        a: Letter.
        designator: Data card particle designator.
        rings: Detector points.
        nd: Total/average specified surfaces/cells option.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'a': types.String,
        'designator': types.Designator,
        'rings': types.Tuple[types.Ring],
        'nd': types.String,
    }

    _REGEX = re.compile(
        rf'\Af(\d*[5])([xyz]):(\S+)((?: {types.Ring._REGEX.pattern})+?)( {types.String._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        a: types.String,
        designator: types.Designator,
        rings: types.Tuple[types.Ring],
        nd: types.String = None,
    ):
        """
        Initializes ``F_2``.

        Parameters:
            suffix: Data card option suffix.
            a: Letter.
            designator: Data card particle designator.
            rings: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if a is None or a not in {'x', 'y', 'z'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if rings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                a,
                rings,
                nd,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.a: typing.Final[types.String] = a
        self.designator: typing.Final[types.Designator] = designator
        self.rings: typing.Final[types.Tuple[types.Ring]] = rings
        self.nd: typing.Final[types.String] = nd


@dataclasses.dataclass
class FBuilder_2:
    """
    Builds ``F_2``.

    Attributes:
        suffix: Data card option suffix.
        a: Letter.
        designator: Data card particle designator.
        rings: Detector points.
        nd: Total/average specified surfaces/cells option.
    """

    suffix: str | int | types.Integer
    a: str | types.String
    designator: str | types.Designator
    rings: list[str] | list[types.Ring]
    nd: str | types.String = None

    def build(self):
        """
        Builds ``FBuilder_2`` into ``F_2``.

        Returns:
            ``F_2`` for ``FBuilder_2``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.a, types.String):
            a = self.a
        elif isinstance(self.a, str):
            a = types.String.from_mcnp(self.a)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        rings = []
        for item in self.rings:
            if isinstance(item, types.Ring):
                rings.append(item)
            elif isinstance(item, str):
                rings.append(types.Ring.from_mcnp(item))
            else:
                rings.append(item.build())
        rings = types.Tuple(rings)

        nd = None
        if isinstance(self.nd, types.String):
            nd = self.nd
        elif isinstance(self.nd, str):
            nd = types.String.from_mcnp(self.nd)

        return F_2(
            suffix=suffix,
            a=a,
            designator=designator,
            rings=rings,
            nd=nd,
        )
