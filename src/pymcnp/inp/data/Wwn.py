import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Wwn(DataOption):
    """
    Represents INP wwn elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        bounds: Lower weight bound.
    """

    _KEYWORD = 'wwn'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwn(\d+):(\S+)((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(
        self, suffix: types.Integer, designator: types.Designator, bounds: types.Tuple[types.Real]
    ):
        """
        Initializes ``Wwn``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            bounds: Lower weight bound.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds


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
    bounds: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``WwnBuilder`` into ``Wwn``.

        Returns:
            ``Wwn`` for ``WwnBuilder``.
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

        if self.bounds:
            bounds = []
            for item in self.bounds:
                if isinstance(item, types.Real):
                    bounds.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    bounds.append(types.Real(item))
                elif isinstance(item, str):
                    bounds.append(types.Real.from_mcnp(item))
            bounds = types.Tuple(bounds)
        else:
            bounds = None

        return Wwn(
            suffix=suffix,
            designator=designator,
            bounds=bounds,
        )

    @staticmethod
    def unbuild(ast: Wwn):
        """
        Unbuilds ``Wwn`` into ``WwnBuilder``

        Returns:
            ``WwnBuilder`` for ``Wwn``.
        """

        return Wwn(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            bounds=copy.deepcopy(ast.bounds),
        )
