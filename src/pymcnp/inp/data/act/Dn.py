import re
import typing
import dataclasses


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dn(ActOption_, keyword='dn'):
    """
    Represents INP dn elements.

    Attributes:
        source: Delayed neutron data source.
    """

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'\Adn( {types.String._REGEX.pattern})\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``Dn``.

        Parameters:
            source: Delayed neutron data source.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if source is None or source not in {'model', 'library', 'both', 'prompt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, source)

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

        if isinstance(self.source, types.String):
            source = self.source
        elif isinstance(self.source, str):
            source = types.String.from_mcnp(self.source)

        return Dn(
            source=source,
        )
