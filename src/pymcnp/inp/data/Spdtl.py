import re

from . import _option
from ... import types
from ... import errors


class Spdtl(_option.DataOption):
    """
    Represents INP spdtl elements.
    """

    _KEYWORD = 'spdtl'

    _ATTRS = {
        'keyword': types.String,
    }

    _REGEX = re.compile(rf'\Aspdtl( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, keyword: str | types.String):
        """
        Initializes ``Spdtl``.

        Parameters:
            keyword: keyword in {"force", "off"}.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.keyword: types.String = keyword

    @property
    def keyword(self) -> types.String:
        """
        Keyword in {"force", "off"}

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._keyword

    @keyword.setter
    def keyword(self, keyword: str | types.String) -> None:
        """
        Sets ``keyword``.

        Parameters:
            keyword: keyword in {"force", "off"}.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if keyword is not None:
            if isinstance(keyword, types.String):
                keyword = keyword
            elif isinstance(keyword, str):
                keyword = types.String.from_mcnp(keyword)

        if keyword is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, keyword)

        self._keyword: types.String = keyword
