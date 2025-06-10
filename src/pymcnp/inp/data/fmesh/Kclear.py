import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Kclear(_option.FmeshOption):
    """
    Represents INP kclear elements.

    Attributes:
        count: KCODE cycles between zeros.
    """

    _KEYWORD = 'kclear'

    _ATTRS = {
        'count': types.Integer,
    }

    _REGEX = re.compile(rf'\Akclear( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, count: types.Integer):
        """
        Initializes ``Kclear``.

        Parameters:
            count: KCODE cycles between zeros.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.Integer] = count


@dataclasses.dataclass
class KclearBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Kclear``.

    Attributes:
        count: KCODE cycles between zeros.
    """

    count: str | int | types.Integer

    def build(self):
        """
        Builds ``KclearBuilder`` into ``Kclear``.

        Returns:
            ``Kclear`` for ``KclearBuilder``.
        """

        count = self.count
        if isinstance(self.count, types.Integer):
            count = self.count
        elif isinstance(self.count, int):
            count = types.Integer(self.count)
        elif isinstance(self.count, str):
            count = types.Integer.from_mcnp(self.count)

        return Kclear(
            count=count,
        )

    @staticmethod
    def unbuild(ast: Kclear):
        """
        Unbuilds ``Kclear`` into ``KclearBuilder``

        Returns:
            ``KclearBuilder`` for ``Kclear``.
        """

        return KclearBuilder(
            count=copy.deepcopy(ast.count),
        )
