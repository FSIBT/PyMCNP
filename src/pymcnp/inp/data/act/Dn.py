import re
import copy
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Dn(ActOption):
    """
    Represents INP dn elements.

    Attributes:
        source: Delayed neutron data source.
    """

    _KEYWORD = 'dn'

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'\Adn( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``Dn``.

        Parameters:
            source: Delayed neutron data source.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if source is None or source not in {'model', 'library', 'both', 'prompt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, source)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                source,
            ]
        )

        self.source: typing.Final[types.String] = source


@dataclasses.dataclass
class DnBuilder:
    """
    Builds ``Dn``.

    Attributes:
        source: Delayed neutron data source.
    """

    source: str | types.String

    def build(self):
        """
        Builds ``DnBuilder`` into ``Dn``.

        Returns:
            ``Dn`` for ``DnBuilder``.
        """

        source = self.source
        if isinstance(self.source, types.String):
            source = self.source
        elif isinstance(self.source, str):
            source = types.String.from_mcnp(self.source)

        return Dn(
            source=source,
        )

    @staticmethod
    def unbuild(ast: Dn):
        """
        Unbuilds ``Dn`` into ``DnBuilder``

        Returns:
            ``DnBuilder`` for ``Dn``.
        """

        return Dn(
            source=copy.deepcopy(ast.source),
        )
