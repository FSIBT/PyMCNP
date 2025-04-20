import re
import typing
import dataclasses


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Dg(ActOption_, keyword='dg'):
    """
    Represents INP dg elements.

    Attributes:
        source: Delayed gamma data source.
    """

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'\Adg( {types.String._REGEX.pattern})\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``Dg``.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if source is None or source not in {'line', 'mg', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, source)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                source,
            ]
        )

        self.source: typing.Final[types.String] = source


@dataclasses.dataclass
class DgBuilder:
    """
    Builds ``Dg``.

    Attributes:
        source: Delayed gamma data source.
    """

    source: str | types.String

    def build(self):
        """
        Builds ``DgBuilder`` into ``Dg``.

        Returns:
            ``Dg`` for ``DgBuilder``.
        """

        if isinstance(self.source, types.String):
            source = self.source
        elif isinstance(self.source, str):
            source = types.String.from_mcnp(self.source)

        return Dg(
            source=source,
        )
