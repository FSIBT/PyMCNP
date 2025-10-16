import re

from . import _card
from .. import types
from .. import errors


class Spdtl(_card.Card):
    """
    Represents INP `spdtl` cards.
    """

    _KEYWORD = 'spdtl'

    _ATTRS = {
        'keyword': types.String,
    }

    _REGEX = re.compile(rf'\Aspdtl( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, keyword: str | types.String):
        """
        Initializes `Spdtl`.

        Parameters:
            keyword: keyword in {"force", "off"}.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.keyword: types.String = keyword

    @property
    def keyword(self) -> types.String:
        """
        Keyword in {"force", "off"}

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._keyword

    @keyword.setter
    def keyword(self, keyword: str | types.String) -> None:
        """
        Sets `keyword`.

        Parameters:
            keyword: keyword in {"force", "off"}.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if keyword is not None:
            if isinstance(keyword, types.String):
                keyword = keyword
            elif isinstance(keyword, str):
                keyword = types.String.from_mcnp(keyword)

        if keyword is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, keyword)

        self._keyword: types.String = keyword
