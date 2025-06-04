import re
import copy
import typing
import dataclasses


from ._option import ActOption
from ....utils import types
from ....utils import errors


class Dg(ActOption):
    """
    Represents INP dg elements.

    Attributes:
        source: Delayed gamma data source.
    """

    _KEYWORD = 'dg'

    _ATTRS = {
        'source': types.String,
    }

    _REGEX = re.compile(rf'\Adg( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, source: types.String):
        """
        Initializes ``Dg``.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if source is None or source not in {'line', 'mg', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, source)

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

        source = self.source
        if isinstance(self.source, types.String):
            source = self.source
        elif isinstance(self.source, str):
            source = types.String.from_mcnp(self.source)

        return Dg(
            source=source,
        )

    @staticmethod
    def unbuild(ast: Dg):
        """
        Unbuilds ``Dg`` into ``DgBuilder``

        Returns:
            ``DgBuilder`` for ``Dg``.
        """

        return Dg(
            source=copy.deepcopy(ast.source),
        )
