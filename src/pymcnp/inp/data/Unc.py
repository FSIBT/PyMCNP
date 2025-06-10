import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Unc(_option.DataOption):
    """
    Represents INP unc elements.

    Attributes:
        designator: Data option particle designator.
        settings: Tuple of uncollided secondary settings.
    """

    _KEYWORD = 'unc'

    _ATTRS = {
        'designator': types.Designator,
        'settings': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aunc:(\S+)((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, designator: types.Designator, settings: types.Tuple[types.Integer]):
        """
        Initializes ``Unc``.

        Parameters:
            designator: Data option particle designator.
            settings: Tuple of uncollided secondary settings.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if settings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.settings: typing.Final[types.Tuple[types.Integer]] = settings


@dataclasses.dataclass
class UncBuilder(_option.DataOptionBuilder):
    """
    Builds ``Unc``.

    Attributes:
        designator: Data option particle designator.
        settings: Tuple of uncollided secondary settings.
    """

    designator: str | types.Designator
    settings: list[str] | list[int] | list[types.Integer]

    def build(self):
        """
        Builds ``UncBuilder`` into ``Unc``.

        Returns:
            ``Unc`` for ``UncBuilder``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        if self.settings:
            settings = []
            for item in self.settings:
                if isinstance(item, types.Integer):
                    settings.append(item)
                elif isinstance(item, int):
                    settings.append(types.Integer(item))
                elif isinstance(item, str):
                    settings.append(types.Integer.from_mcnp(item))
            settings = types.Tuple(settings)
        else:
            settings = None

        return Unc(
            designator=designator,
            settings=settings,
        )

    @staticmethod
    def unbuild(ast: Unc):
        """
        Unbuilds ``Unc`` into ``UncBuilder``

        Returns:
            ``UncBuilder`` for ``Unc``.
        """

        return UncBuilder(
            designator=copy.deepcopy(ast.designator),
            settings=copy.deepcopy(ast.settings),
        )
