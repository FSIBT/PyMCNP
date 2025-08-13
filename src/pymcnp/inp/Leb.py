import re

from . import _card
from .. import types
from .. import errors


class Leb(_card.Card):
    """
    Represents INP `leb` cards.
    """

    _KEYWORD = 'leb'

    _ATTRS = {
        'yzere': types.Real,
        'bzere': types.Real,
        'yzero': types.Real,
        'bzero': types.Real,
    }

    _REGEX = re.compile(rf'\Aleb( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(
        self, yzere: str | int | float | types.Real = None, bzere: str | int | float | types.Real = None, yzero: str | int | float | types.Real = None, bzero: str | int | float | types.Real = None
    ):
        """
        Initializes `Leb`.

        Parameters:
            yzere: Y0 parameter in level-density formula for Z≤70.
            bzere: B0 parameter in level-density formula for Z≤70.
            yzero: Y0 parameter in level-density formula for Z≥71.
            bzero: B0 parameter in level-density formula for Z≥70.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.yzere: types.Real = yzere
        self.bzere: types.Real = bzere
        self.yzero: types.Real = yzero
        self.bzero: types.Real = bzero

    @property
    def yzere(self) -> types.Real:
        """
        Y0 parameter in level-density formula for Z≤70

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._yzere

    @yzere.setter
    def yzere(self, yzere: str | int | float | types.Real) -> None:
        """
        Sets `yzere`.

        Parameters:
            yzere: Y0 parameter in level-density formula for Z≤70.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if yzere is not None:
            if isinstance(yzere, types.Real):
                yzere = yzere
            elif isinstance(yzere, int) or isinstance(yzere, float):
                yzere = types.Real(yzere)
            elif isinstance(yzere, str):
                yzere = types.Real.from_mcnp(yzere)

        if yzere is not None and not (isinstance(yzere.value, types.Jump) or yzere > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, yzere)

        self._yzere: types.Real = yzere

    @property
    def bzere(self) -> types.Real:
        """
        B0 parameter in level-density formula for Z≤70

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bzere

    @bzere.setter
    def bzere(self, bzere: str | int | float | types.Real) -> None:
        """
        Sets `bzere`.

        Parameters:
            bzere: B0 parameter in level-density formula for Z≤70.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bzere is not None:
            if isinstance(bzere, types.Real):
                bzere = bzere
            elif isinstance(bzere, int) or isinstance(bzere, float):
                bzere = types.Real(bzere)
            elif isinstance(bzere, str):
                bzere = types.Real.from_mcnp(bzere)

        if bzere is not None and not (isinstance(bzere.value, types.Jump) or bzere > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bzere)

        self._bzere: types.Real = bzere

    @property
    def yzero(self) -> types.Real:
        """
        Y0 parameter in level-density formula for Z≥71

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._yzero

    @yzero.setter
    def yzero(self, yzero: str | int | float | types.Real) -> None:
        """
        Sets `yzero`.

        Parameters:
            yzero: Y0 parameter in level-density formula for Z≥71.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if yzero is not None:
            if isinstance(yzero, types.Real):
                yzero = yzero
            elif isinstance(yzero, int) or isinstance(yzero, float):
                yzero = types.Real(yzero)
            elif isinstance(yzero, str):
                yzero = types.Real.from_mcnp(yzero)

        if yzero is not None and not (isinstance(yzero.value, types.Jump) or yzero > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, yzero)

        self._yzero: types.Real = yzero

    @property
    def bzero(self) -> types.Real:
        """
        B0 parameter in level-density formula for Z≥70

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bzero

    @bzero.setter
    def bzero(self, bzero: str | int | float | types.Real) -> None:
        """
        Sets `bzero`.

        Parameters:
            bzero: B0 parameter in level-density formula for Z≥70.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bzero is not None:
            if isinstance(bzero, types.Real):
                bzero = bzero
            elif isinstance(bzero, int) or isinstance(bzero, float):
                bzero = types.Real(bzero)
            elif isinstance(bzero, str):
                bzero = types.Real.from_mcnp(bzero)

        if bzero is not None and not (isinstance(bzero.value, types.Jump) or bzero > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bzero)

        self._bzero: types.Real = bzero
