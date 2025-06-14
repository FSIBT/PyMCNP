import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Sfnu(_option.FmultOption):
    """
    Represents INP sfnu elements.

    Attributes:
        distribution: V bar for or of cumulative distribution the sampling spontaneous fission.
    """

    _KEYWORD = 'sfnu'

    _ATTRS = {
        'distribution': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Asfnu((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, distribution: types.Tuple[types.Real]):
        """
        Initializes ``Sfnu``.

        Parameters:
            distribution: V bar for or of cumulative distribution the sampling spontaneous fission.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if distribution is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distribution)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                distribution,
            ]
        )

        self.distribution: typing.Final[types.Tuple[types.Real]] = distribution


@dataclasses.dataclass
class SfnuBuilder(_option.FmultOptionBuilder):
    """
    Builds ``Sfnu``.

    Attributes:
        distribution: V bar for or of cumulative distribution the sampling spontaneous fission.
    """

    distribution: list[str] | list[float] | list[types.Real]

    def build(self):
        """
        Builds ``SfnuBuilder`` into ``Sfnu``.

        Returns:
            ``Sfnu`` for ``SfnuBuilder``.
        """

        if self.distribution:
            distribution = []
            for item in self.distribution:
                if isinstance(item, types.Real):
                    distribution.append(item)
                elif isinstance(item, float) or isinstance(item, int):
                    distribution.append(types.Real(item))
                elif isinstance(item, str):
                    distribution.append(types.Real.from_mcnp(item))
            distribution = types.Tuple(distribution)
        else:
            distribution = None

        return Sfnu(
            distribution=distribution,
        )

    @staticmethod
    def unbuild(ast: Sfnu):
        """
        Unbuilds ``Sfnu`` into ``SfnuBuilder``

        Returns:
            ``SfnuBuilder`` for ``Sfnu``.
        """

        return SfnuBuilder(
            distribution=copy.deepcopy(ast.distribution),
        )
