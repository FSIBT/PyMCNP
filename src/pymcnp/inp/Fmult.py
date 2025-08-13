import re

from . import fmult
from . import _card
from .. import types
from .. import errors


class Fmult(_card.Card):
    """
    Represents INP `fmult` cards.
    """

    _KEYWORD = 'fmult'

    _ATTRS = {
        'zaid': types.Zaid,
        'options': types.Tuple(fmult.FmultOption),
    }

    _REGEX = re.compile(rf'\Afmult( {types.Zaid._REGEX.pattern[2:-2]})((?: (?:{fmult.FmultOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)

    def __init__(self, zaid: str | types.Zaid, options: list[str] | list[fmult.FmultOption] = None):
        """
        Initializes `Fmult`.

        Parameters:
            zaid: Nuclide for which data are entered.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.zaid: types.Zaid = zaid
        self.options: types.Tuple(fmult.FmultOption) = options

    @property
    def zaid(self) -> types.Zaid:
        """
        Nuclide for which data are entered

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zaid

    @zaid.setter
    def zaid(self, zaid: str | types.Zaid) -> None:
        """
        Sets `zaid`.

        Parameters:
            zaid: Nuclide for which data are entered.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zaid is not None:
            if isinstance(zaid, types.Zaid):
                zaid = zaid
            elif isinstance(zaid, str):
                zaid = types.Zaid.from_mcnp(zaid)

        if zaid is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, zaid)

        self._zaid: types.Zaid = zaid

    @property
    def options(self) -> types.Tuple(fmult.FmultOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[fmult.FmultOption]) -> None:
        """
        Sets `options`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, fmult.FmultOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(fmult.FmultOption.from_mcnp(item))
            options = types.Tuple(fmult.FmultOption)(array)

        self._options: types.Tuple(fmult.FmultOption) = options
