import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ds_2(DataOption):
    """
    Represents INP ds variation #2 elements.

    Attributes:
        suffix: Data card option suffix.
        vss: Dependent source independent & dependent variables.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'vss': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) q((?: {types.IndependentDependent._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, vss: types.Tuple[types.IndependentDependent]):
        """
        Initializes ``Ds_2``.

        Parameters:
            suffix: Data card option suffix.
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if vss is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vss)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                vss,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.vss: typing.Final[types.Tuple[types.IndependentDependent]] = vss


@dataclasses.dataclass
class DsBuilder_2:
    """
    Builds ``Ds_2``.

    Attributes:
        suffix: Data card option suffix.
        vss: Dependent source independent & dependent variables.
    """

    suffix: str | int | types.Integer
    vss: list[str] | list[types.IndependentDependent]

    def build(self):
        """
        Builds ``DsBuilder_2`` into ``Ds_2``.

        Returns:
            ``Ds_2`` for ``DsBuilder_2``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        vss = []
        for item in self.vss:
            if isinstance(item, types.IndependentDependent):
                vss.append(item)
            elif isinstance(item, str):
                vss.append(types.IndependentDependent.from_mcnp(item))
            else:
                vss.append(item.build())
        vss = types.Tuple(vss)

        return Ds_2(
            suffix=suffix,
            vss=vss,
        )
