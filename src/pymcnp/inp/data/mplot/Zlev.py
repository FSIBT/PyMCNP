import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Zlev(MplotOption, keyword='zlev'):
    """
    Represents INP zlev elements.

    Attributes:
        n: Scales of tally plots.
    """

    _ATTRS = {
        'n': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Azlev((?: {types.String._REGEX.pattern})+?)\Z')

    def __init__(self, n: types.Tuple[types.String]):
        """
        Initializes ``Zlev``.

        Parameters:
            n: Scales of tally plots.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if n is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, n)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                n,
            ]
        )

        self.n: typing.Final[types.Tuple[types.String]] = n


@dataclasses.dataclass
class ZlevBuilder:
    """
    Builds ``Zlev``.

    Attributes:
        n: Scales of tally plots.
    """

    n: list[str] | list[types.String]

    def build(self):
        """
        Builds ``ZlevBuilder`` into ``Zlev``.

        Returns:
            ``Zlev`` for ``ZlevBuilder``.
        """

        n = []
        for item in self.n:
            if isinstance(item, types.String):
                n.append(item)
            elif isinstance(item, str):
                n.append(types.String.from_mcnp(item))
            else:
                n.append(item.build())
        n = types.Tuple(n)

        return Zlev(
            n=n,
        )
