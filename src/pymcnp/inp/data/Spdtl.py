import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Spdtl(DataOption):
    """
    Represents INP spdtl elements.

    Attributes:
        keyword: keyword in {"force", "off"}.
    """

    _KEYWORD = 'spdtl'

    _ATTRS = {
        'keyword': types.String,
    }

    _REGEX = re.compile(rf'\Aspdtl( {types.String._REGEX.pattern})\Z')

    def __init__(self, keyword: types.String):
        """
        Initializes ``Spdtl``.

        Parameters:
            keyword: keyword in {"force", "off"}.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if keyword is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, keyword)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                keyword,
            ]
        )

        self.keyword: typing.Final[types.String] = keyword


@dataclasses.dataclass
class SpdtlBuilder:
    """
    Builds ``Spdtl``.

    Attributes:
        keyword: keyword in {"force", "off"}.
    """

    keyword: str | types.String

    def build(self):
        """
        Builds ``SpdtlBuilder`` into ``Spdtl``.

        Returns:
            ``Spdtl`` for ``SpdtlBuilder``.
        """

        keyword = self.keyword
        if isinstance(self.keyword, types.String):
            keyword = self.keyword
        elif isinstance(self.keyword, str):
            keyword = types.String.from_mcnp(self.keyword)

        return Spdtl(
            keyword=keyword,
        )

    @staticmethod
    def unbuild(ast: Spdtl):
        """
        Unbuilds ``Spdtl`` into ``SpdtlBuilder``

        Returns:
            ``SpdtlBuilder`` for ``Spdtl``.
        """

        return Spdtl(
            keyword=copy.deepcopy(ast.keyword),
        )
