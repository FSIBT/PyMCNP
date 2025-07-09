import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Pd(_option.DataOption):
    """
    Represents INP pd elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        probabilities: Probability of contribution to DXTRAN.
    """

    _KEYWORD = 'pd'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probabilities': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Apd(\d+):(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, designator: types.Designator, probabilities: types.Tuple[types.Real]):
        """
        Initializes ``Pd``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            probabilities: Probability of contribution to DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if probabilities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probabilities)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                probabilities,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.probabilities: typing.Final[types.Tuple[types.Real]] = probabilities


@dataclasses.dataclass
class PdBuilder(_option.DataOptionBuilder):
    """
    Builds ``Pd``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        probabilities: Probability of contribution to DXTRAN.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    probabilities: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``PdBuilder`` into ``Pd``.

        Returns:
            ``Pd`` for ``PdBuilder``.
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

        if self.probabilities:
            probabilities = []
            for item in self.probabilities:
                if isinstance(item, types.Real):
                    probabilities.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    probabilities.append(types.Real(item))
                elif isinstance(item, str):
                    probabilities.append(types.Real.from_mcnp(item))
            probabilities = types.Tuple(probabilities)
        else:
            probabilities = None

        return Pd(
            suffix=suffix,
            designator=designator,
            probabilities=probabilities,
        )

    @staticmethod
    def unbuild(ast: Pd):
        """
        Unbuilds ``Pd`` into ``PdBuilder``

        Returns:
            ``PdBuilder`` for ``Pd``.
        """

        return PdBuilder(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            probabilities=copy.deepcopy(ast.probabilities),
        )
