import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Dm(_option.DataOption):
    """
    Represents INP dm elements.

    Attributes:
        suffix: Data card option suffix.
        zaids: Tuple of ZAID aliases.
    """

    _KEYWORD = 'dm'

    _ATTRS = {
        'suffix': types.Integer,
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Adm(\d+)((?: {types.Zaid._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, zaids: types.Tuple[types.Zaid]):
        """
        Initializes ``Dm``.

        Parameters:
            suffix: Data card option suffix.
            zaids: Tuple of ZAID aliases.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class DmBuilder(_option.DataOptionBuilder):
    """
    Builds ``Dm``.

    Attributes:
        suffix: Data card option suffix.
        zaids: Tuple of ZAID aliases.
    """

    suffix: str | int | types.Integer
    zaids: list[str] | list[types.Zaid]

    def build(self):
        """
        Builds ``DmBuilder`` into ``Dm``.

        Returns:
            ``Dm`` for ``DmBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

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

        return Dm(
            suffix=suffix,
            zaids=zaids,
        )

    @staticmethod
    def unbuild(ast: Dm):
        """
        Unbuilds ``Dm`` into ``DmBuilder``

        Returns:
            ``DmBuilder`` for ``Dm``.
        """

        return DmBuilder(
            suffix=copy.deepcopy(ast.suffix),
            zaids=copy.deepcopy(ast.zaids),
        )
