import re

from . import data
from . import _card
from .. import types
from .. import errors


class Data(_card.Card):
    """
    Represents INP data elements.
    """

    _ATTRS = {'option': data.DataOption}

    _REGEX = re.compile(rf'\A({data.DataOption._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, option: data.DataOption):
        """
        Initializes ``Data``.

        Parameters:
            option: Data option.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.option: data.DataOption = option

    def to_mcnp(self):
        """
        Generates INP from ``Data``.

        Returns:
            INP data card.
        """

        source = f'{self.option}'
        source = _card.Card._postprocess(source)

        return source

    @property
    def option(self) -> types.String:
        """
        Data option.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | data.DataOption) -> None:
        """
        Sets ``option``.

        Parameters:
            option: Comment option.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if option is not None:
            if isinstance(option, data.DataOption):
                option = option
            elif isinstance(option, str):
                option = data.DataOption.from_mcnp(option)

        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, option)

        self._option: data.DataOption = option
