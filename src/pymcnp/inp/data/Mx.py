import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Mx(DataOption):
    """
    Represents INP mx elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        zaids: Zaid substitutions for particles.
    """

    _KEYWORD = 'mx'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'zaids': types.Tuple[types.Zaid],
    }

    _REGEX = re.compile(rf'\Amx(\d+):(\S+)((?: {types.Zaid._REGEX.pattern})+?)\Z')

    def __init__(
        self, suffix: types.Integer, designator: types.Designator, zaids: types.Tuple[types.Zaid]
    ):
        """
        Initializes ``Mx``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            zaids: Zaid substitutions for particles.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zaids)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                zaids,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.designator: typing.Final[types.Designator] = designator
        self.zaids: typing.Final[types.Tuple[types.Zaid]] = zaids


@dataclasses.dataclass
class MxBuilder:
    """
    Builds ``Mx``.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        zaids: Zaid substitutions for particles.
    """

    suffix: str | int | types.Integer
    designator: str | types.Designator
    zaids: list[str] | list[types.Zaid]

    def build(self):
        """
        Builds ``MxBuilder`` into ``Mx``.

        Returns:
            ``Mx`` for ``MxBuilder``.
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

        if self.zaids:
            zaids = []
            for item in self.zaids:
                if isinstance(item, types.Zaid):
                    zaids.append(item)
                elif isinstance(item, str):
                    zaids.append(types.Zaid.from_mcnp(item))
                else:
                    zaids.append(item.build())
            zaids = types.Tuple(zaids)
        else:
            zaids = None

        return Mx(
            suffix=suffix,
            designator=designator,
            zaids=zaids,
        )

    @staticmethod
    def unbuild(ast: Mx):
        """
        Unbuilds ``Mx`` into ``MxBuilder``

        Returns:
            ``MxBuilder`` for ``Mx``.
        """

        return Mx(
            suffix=copy.deepcopy(ast.suffix),
            designator=copy.deepcopy(ast.designator),
            zaids=copy.deepcopy(ast.zaids),
        )
