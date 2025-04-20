import re
import typing
import dataclasses


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Spdtl(DataOption_, keyword='spdtl'):
    """
    Represents INP spdtl elements.

    Attributes:
        keyword: keyword in {"force", "off"}.
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if keyword is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, keyword)

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

        if isinstance(self.keyword, types.String):
            keyword = self.keyword
        elif isinstance(self.keyword, str):
            keyword = types.String.from_mcnp(self.keyword)

        return Spdtl(
            keyword=keyword,
        )
