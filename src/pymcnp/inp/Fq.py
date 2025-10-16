import re

from . import _card
from .. import types
from .. import errors


class Fq(_card.Card):
    """
    Represents INP `fq` cards.
    """

    _KEYWORD = 'fq'

    _ATTRS = {
        'suffix': types.Integer,
        'a1': types.String,
        'a2': types.String,
        'a3': types.String,
        'a4': types.String,
        'a5': types.String,
        'a6': types.String,
        'a7': types.String,
        'a8': types.String,
    }

    _REGEX = re.compile(
        rf'\Afq(\d+)?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        suffix: str | int | types.Integer = None,
        a1: str | types.String = None,
        a2: str | types.String = None,
        a3: str | types.String = None,
        a4: str | types.String = None,
        a5: str | types.String = None,
        a6: str | types.String = None,
        a7: str | types.String = None,
        a8: str | types.String = None,
    ):
        """
        Initializes `Fq`.

        Parameters:
            suffix: Data card option suffix.
            a1: Letters representing tally bin types.
            a2: Letters representing tally bin types.
            a3: Letters representing tally bin types.
            a4: Letters representing tally bin types.
            a5: Letters representing tally bin types.
            a6: Letters representing tally bin types.
            a7: Letters representing tally bin types.
            a8: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.suffix: types.Integer = suffix
        self.a1: types.String = a1
        self.a2: types.String = a2
        self.a3: types.String = a3
        self.a4: types.String = a4
        self.a5: types.String = a5
        self.a6: types.String = a6
        self.a7: types.String = a7
        self.a8: types.String = a8

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is not None and not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def a1(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a1

    @a1.setter
    def a1(self, a1: str | types.String) -> None:
        """
        Sets `a1`.

        Parameters:
            a1: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a1 is not None:
            if isinstance(a1, types.String):
                a1 = a1
            elif isinstance(a1, str):
                a1 = types.String.from_mcnp(a1)

        if a1 is not None and a1.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a1)

        self._a1: types.String = a1

    @property
    def a2(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a2

    @a2.setter
    def a2(self, a2: str | types.String) -> None:
        """
        Sets `a2`.

        Parameters:
            a2: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a2 is not None:
            if isinstance(a2, types.String):
                a2 = a2
            elif isinstance(a2, str):
                a2 = types.String.from_mcnp(a2)

        if a2 is not None and a2.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a2)

        self._a2: types.String = a2

    @property
    def a3(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a3

    @a3.setter
    def a3(self, a3: str | types.String) -> None:
        """
        Sets `a3`.

        Parameters:
            a3: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a3 is not None:
            if isinstance(a3, types.String):
                a3 = a3
            elif isinstance(a3, str):
                a3 = types.String.from_mcnp(a3)

        if a3 is not None and a3.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a3)

        self._a3: types.String = a3

    @property
    def a4(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a4

    @a4.setter
    def a4(self, a4: str | types.String) -> None:
        """
        Sets `a4`.

        Parameters:
            a4: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a4 is not None:
            if isinstance(a4, types.String):
                a4 = a4
            elif isinstance(a4, str):
                a4 = types.String.from_mcnp(a4)

        if a4 is not None and a4.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a4)

        self._a4: types.String = a4

    @property
    def a5(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a5

    @a5.setter
    def a5(self, a5: str | types.String) -> None:
        """
        Sets `a5`.

        Parameters:
            a5: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a5 is not None:
            if isinstance(a5, types.String):
                a5 = a5
            elif isinstance(a5, str):
                a5 = types.String.from_mcnp(a5)

        if a5 is not None and a5.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a5)

        self._a5: types.String = a5

    @property
    def a6(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a6

    @a6.setter
    def a6(self, a6: str | types.String) -> None:
        """
        Sets `a6`.

        Parameters:
            a6: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a6 is not None:
            if isinstance(a6, types.String):
                a6 = a6
            elif isinstance(a6, str):
                a6 = types.String.from_mcnp(a6)

        if a6 is not None and a6.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a6)

        self._a6: types.String = a6

    @property
    def a7(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a7

    @a7.setter
    def a7(self, a7: str | types.String) -> None:
        """
        Sets `a7`.

        Parameters:
            a7: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a7 is not None:
            if isinstance(a7, types.String):
                a7 = a7
            elif isinstance(a7, str):
                a7 = types.String.from_mcnp(a7)

        if a7 is not None and a7.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a7)

        self._a7: types.String = a7

    @property
    def a8(self) -> types.String:
        """
        Letters representing tally bin types

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._a8

    @a8.setter
    def a8(self, a8: str | types.String) -> None:
        """
        Sets `a8`.

        Parameters:
            a8: Letters representing tally bin types.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if a8 is not None:
            if isinstance(a8, types.String):
                a8 = a8
            elif isinstance(a8, str):
                a8 = types.String.from_mcnp(a8)

        if a8 is not None and a8.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, a8)

        self._a8: types.String = a8
