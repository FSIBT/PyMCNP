import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Iso(_option.KsenOption):
    """
    Represents INP iso elements.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    _KEYWORD = 'iso'

    _ATTRS = {
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Aiso((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, zaids: types.Tuple[types.Zaid]):
        """
        Initializes ``Iso``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class IsoBuilder(_option.KsenOptionBuilder):
    """
    Builds ``Iso``.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    zaids: list[str] | list[types.Zaid]

    def build(self):
        """
        Builds ``IsoBuilder`` into ``Iso``.

        Returns:
            ``Iso`` for ``IsoBuilder``.
        """

        if self.zaids:
            zaids = []
            for item in self.zaids:
                if isinstance(item, types.Zaid):
                    zaids.append(item)
                elif isinstance(item, str):
                    zaids.append(types.Zaid.from_mcnp(item))
            zaids = types.Tuple(zaids)
        else:
            zaids = None

        return Iso(
            zaids=zaids,
        )

    @staticmethod
    def unbuild(ast: Iso):
        """
        Unbuilds ``Iso`` into ``IsoBuilder``

        Returns:
            ``IsoBuilder`` for ``Iso``.
        """

        return IsoBuilder(
            zaids=copy.deepcopy(ast.zaids),
        )
