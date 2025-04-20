import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwn(DataOption_, keyword='wwn'):
    """
    Represents INP wwn elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        bounds: Lower weight bound.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(
        self,
        suffix: types.Integer,
        designator: types.Designator,
        bounds: types.Tuple[types.RealOrJump],
    ):
        """
        Initializes ``Wwn``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            bounds: Lower weight bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds


@dataclasses.dataclass
class WwnBuilder:
    """
    Builds ``Wwn``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        bounds: Lower weight bound.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    bounds: list[str] | list[float] | list[types.RealOrJump]

    def build(self):
        """
        Builds ``WwnBuilder`` into ``Wwn``.

        Returns:
            ``Wwn`` for ``WwnBuilder``.
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

        bounds = []
        for item in self.bounds:
            if isinstance(item, types.RealOrJump):
                bounds.append(item)
            elif isinstance(item, float) or isinstance(item, int):
                bounds.append(types.RealOrJump(item))
            elif isinstance(item, str):
                bounds.append(types.RealOrJump.from_mcnp(item))
        bounds = types.Tuple(bounds)

        return Wwn(
            suffix=suffix,
            designator=designator,
            bounds=bounds,
        )
