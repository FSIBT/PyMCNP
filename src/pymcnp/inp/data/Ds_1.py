import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ds_1(DataOption):
    """
    Represents INP ds variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        ijs: Dependent source independent & dependent variables.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'ijs': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) t((?: {types.IndependentDependent._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, ijs: types.Tuple[types.IndependentDependent]):
        """
        Initializes ``Ds_1``.

        Parameters:
            suffix: Data card option suffix.
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if ijs is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ijs)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ijs,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.ijs: typing.Final[types.Tuple[types.IndependentDependent]] = ijs


@dataclasses.dataclass
class DsBuilder_1:
    """
    Builds ``Ds_1``.

    Attributes:
        suffix: Data card option suffix.
        ijs: Dependent source independent & dependent variables.
    """

    suffix: str | int | types.Integer
    ijs: list[str] | list[types.IndependentDependent]

    def build(self):
        """
        Builds ``DsBuilder_1`` into ``Ds_1``.

        Returns:
            ``Ds_1`` for ``DsBuilder_1``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        ijs = []
        for item in self.ijs:
            if isinstance(item, types.IndependentDependent):
                ijs.append(item)
            elif isinstance(item, str):
                ijs.append(types.IndependentDependent.from_mcnp(item))
            else:
                ijs.append(item.build())
        ijs = types.Tuple(ijs)

        return Ds_1(
            suffix=suffix,
            ijs=ijs,
        )
