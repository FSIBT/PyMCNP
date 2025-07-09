import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Ds_2(_option.DataOption):
    """
    Represents INP ds variation #2 elements.

    Attributes:
        suffix: Data card option suffix.
        vss: Dependent source independent & dependent variables.
    """

    _KEYWORD = 'ds'

    _ATTRS = {
        'suffix': types.Integer,
        'vss': types.Tuple[types.IndependentDependent],
    }

    _REGEX = re.compile(rf'\Ads(\d+) q((?: {types.IndependentDependent._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: types.Integer, vss: types.Tuple[types.IndependentDependent]):
        """
        Initializes ``Ds_2``.

        Parameters:
            suffix: Data card option suffix.
            vss: Dependent source independent & dependent variables.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix >= 1 and suffix <= 999):
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

    def to_mcnp(self):
        """
        Generates INP from ``Ds_2``.

        Returns:
            INP for ``Ds_2``.
        """

        return f'ds{self.suffix} q {self.vss}'


@dataclasses.dataclass
class DsBuilder_2(_option.DataOptionBuilder):
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

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if self.vss:
            vss = []
            for item in self.vss:
                if isinstance(item, types.IndependentDependent):
                    vss.append(item)
                elif isinstance(item, str):
                    vss.append(types.IndependentDependent.from_mcnp(item))
            vss = types.Tuple(vss)
        else:
            vss = None

        return Ds_2(
            suffix=suffix,
            vss=vss,
        )

    @staticmethod
    def unbuild(ast: Ds_2):
        """
        Unbuilds ``Ds_2`` into ``DsBuilder_2``

        Returns:
            ``DsBuilder_2`` for ``Ds_2``.
        """

        return DsBuilder_2(
            suffix=copy.deepcopy(ast.suffix),
            vss=copy.deepcopy(ast.vss),
        )
