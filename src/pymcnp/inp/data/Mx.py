import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Mx(DataOption_, keyword='mx'):
    """
    Represents INP mx elements.

    Attributes:
        suffix: Data card option suffix.
        designator: Data card particle designator.
        zaids: Zaid substitutions for particles.
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if zaids is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zaids)

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

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        zaids = []
        for item in self.zaids:
            if isinstance(item, types.Zaid):
                zaids.append(item)
            elif isinstance(item, str):
                zaids.append(types.Zaid.from_mcnp(item))
            else:
                zaids.append(item.build())
        zaids = types.Tuple(zaids)

        return Mx(
            suffix=suffix,
            designator=designator,
            zaids=zaids,
        )
