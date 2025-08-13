import re

from . import _option
from ... import types
from ... import errors


class Ext(_option.CellOption):
    """
    Represents INP `ext` elements.
    """

    _KEYWORD = 'ext'

    _ATTRS = {
        'designator': types.Designator,
        'stretch': types.String,
    }

    _REGEX = re.compile(rf'\Aext:(\S+)( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, designator: str | types.Designator, stretch: str | types.String):
        """
        Initializes `Ext`.

        Parameters:
            designator: Cell particle designator.
            stretch: Cell exponential transform stretching specifier.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.designator: types.Designator = designator
        self.stretch: types.String = stretch

    @property
    def designator(self) -> types.Designator:
        """
        Cell particle designator

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Cell particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

    @property
    def stretch(self) -> types.String:
        """
        Cell exponential transform stretching specifier

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._stretch

    @stretch.setter
    def stretch(self, stretch: str | types.String) -> None:
        """
        Sets `stretch`.

        Parameters:
            stretch: Cell exponential transform stretching specifier.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if stretch is not None:
            if isinstance(stretch, types.String):
                stretch = stretch
            elif isinstance(stretch, str):
                stretch = types.String.from_mcnp(stretch)

        if stretch is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, stretch)

        self._stretch: types.String = stretch
