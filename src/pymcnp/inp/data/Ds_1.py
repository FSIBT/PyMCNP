import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Ds_1(_option.DataOption):
    """
    Represents INP ds variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        ijs: Dependent source independent & dependent variables.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'ijs': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) t((?: {types.IndependentDependent._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, ijs: types.Tuple[types.IndependentDependent]):
        """
        Initializes ``Ds_1``.

        Parameters:
            suffix: Data card option suffix.
            ijs: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix >= 1 and suffix <= 999):
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

    def to_mcnp(self):
        """
        Generates INP from ``Ds_1``.

        Returns:
            INP for ``Ds_1``.
        """

        return f'ds{self.suffix} t {self.ijs}'


@dataclasses.dataclass
class DsBuilder_1(_option.DataOptionBuilder):
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

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.ijs:
            ijs = []
            for item in self.ijs:
                if isinstance(item, types.IndependentDependent):
                    ijs.append(item)
                elif isinstance(item, str):
                    ijs.append(types.IndependentDependent.from_mcnp(item))
            ijs = types.Tuple(ijs)
        else:
            ijs = None

        return Ds_1(
            suffix=suffix,
            ijs=ijs,
        )

    @staticmethod
    def unbuild(ast: Ds_1):
        """
        Unbuilds ``Ds_1`` into ``DsBuilder_1``

        Returns:
            ``DsBuilder_1`` for ``Ds_1``.
        """

        return DsBuilder_1(
            suffix=copy.deepcopy(ast.suffix),
            ijs=copy.deepcopy(ast.ijs),
        )
