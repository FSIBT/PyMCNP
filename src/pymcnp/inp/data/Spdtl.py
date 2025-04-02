import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Spdtl(DataOption_, keyword='spdtl'):
    """
    Represents INP spdtl elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
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
