import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Kcode(_option.MplotOption):
    """
    Represents INP kcode elements.

    Attributes:
        i: Lifetime to remove.
    """

    _KEYWORD = 'kcode'

    _ATTRS = {
        'i': types.Integer,
    }

    _REGEX = re.compile(rf'\Akcode( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, i: types.Integer):
        """
        Initializes ``Kcode``.

        Parameters:
            i: Lifetime to remove.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if i is None or not ((i >= 1 and i <= 6) or (i >= 1 and i <= 19)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                i,
            ]
        )

        self.i: typing.Final[types.Integer] = i


@dataclasses.dataclass
class KcodeBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Kcode``.

    Attributes:
        i: Lifetime to remove.
    """

    i: str | int | types.Integer

    def build(self):
        """
        Builds ``KcodeBuilder`` into ``Kcode``.

        Returns:
            ``Kcode`` for ``KcodeBuilder``.
        """

        i = self.i
        if isinstance(self.i, types.Integer):
            i = self.i
        elif isinstance(self.i, int):
            i = types.Integer(self.i)
        elif isinstance(self.i, str):
            i = types.Integer.from_mcnp(self.i)

        return Kcode(
            i=i,
        )

    @staticmethod
    def unbuild(ast: Kcode):
        """
        Unbuilds ``Kcode`` into ``KcodeBuilder``

        Returns:
            ``KcodeBuilder`` for ``Kcode``.
        """

        return KcodeBuilder(
            i=copy.deepcopy(ast.i),
        )
