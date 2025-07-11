import re

from . import _option
from ...utils import types
from ...utils import errors


class Tf_0(_option.DataOption):
    """
    Represents INP tf variation #0 elements.

    Attributes:
        suffix: Data card option suffix.
        if1: Cell, surface, or detector bin number.
        id1: Total, flagged, or un-collided bin number.
        iu1: User bin number.
        is1: Segment bin number.
        im1: Multiplier bin number.
        ic1: Cosine bin number.
        ie1: Energy bin number.
        it1: Time bin number.
    """

    _KEYWORD = 'tf'

    _ATTRS = {
        'suffix': types.Integer,
        'if1': types.Integer,
        'id1': types.Integer,
        'iu1': types.Integer,
        'is1': types.Integer,
        'im1': types.Integer,
        'ic1': types.Integer,
        'ie1': types.Integer,
        'it1': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Atf(\d+)( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        suffix: str | int | types.Integer,
        if1: str | int | types.Integer = None,
        id1: str | int | types.Integer = None,
        iu1: str | int | types.Integer = None,
        is1: str | int | types.Integer = None,
        im1: str | int | types.Integer = None,
        ic1: str | int | types.Integer = None,
        ie1: str | int | types.Integer = None,
        it1: str | int | types.Integer = None,
    ):
        """
        Initializes ``Tf_0``.

        Parameters:
            suffix: Data card option suffix.
            if1: Cell, surface, or detector bin number.
            id1: Total, flagged, or un-collided bin number.
            iu1: User bin number.
            is1: Segment bin number.
            im1: Multiplier bin number.
            ic1: Cosine bin number.
            ie1: Energy bin number.
            it1: Time bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.if1: types.Integer = if1
        self.id1: types.Integer = id1
        self.iu1: types.Integer = iu1
        self.is1: types.Integer = is1
        self.im1: types.Integer = im1
        self.ic1: types.Integer = ic1
        self.ie1: types.Integer = ie1
        self.it1: types.Integer = it1

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)
            else:
                raise TypeError

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def if1(self) -> types.Integer:
        """
        Gets ``if1``.

        Returns:
            ``if1``.
        """

        return self._if1

    @if1.setter
    def if1(self, if1: str | int | types.Integer) -> None:
        """
        Sets ``if1``.

        Parameters:
            if1: Cell, surface, or detector bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if if1 is not None:
            if isinstance(if1, types.Integer):
                if1 = if1
            elif isinstance(if1, int):
                if1 = types.Integer(if1)
            elif isinstance(if1, str):
                if1 = types.Integer.from_mcnp(if1)
            else:
                raise TypeError

        self._if1: types.Integer = if1

    @property
    def id1(self) -> types.Integer:
        """
        Gets ``id1``.

        Returns:
            ``id1``.
        """

        return self._id1

    @id1.setter
    def id1(self, id1: str | int | types.Integer) -> None:
        """
        Sets ``id1``.

        Parameters:
            id1: Total, flagged, or un-collided bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if id1 is not None:
            if isinstance(id1, types.Integer):
                id1 = id1
            elif isinstance(id1, int):
                id1 = types.Integer(id1)
            elif isinstance(id1, str):
                id1 = types.Integer.from_mcnp(id1)
            else:
                raise TypeError

        self._id1: types.Integer = id1

    @property
    def iu1(self) -> types.Integer:
        """
        Gets ``iu1``.

        Returns:
            ``iu1``.
        """

        return self._iu1

    @iu1.setter
    def iu1(self, iu1: str | int | types.Integer) -> None:
        """
        Sets ``iu1``.

        Parameters:
            iu1: User bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if iu1 is not None:
            if isinstance(iu1, types.Integer):
                iu1 = iu1
            elif isinstance(iu1, int):
                iu1 = types.Integer(iu1)
            elif isinstance(iu1, str):
                iu1 = types.Integer.from_mcnp(iu1)
            else:
                raise TypeError

        self._iu1: types.Integer = iu1

    @property
    def is1(self) -> types.Integer:
        """
        Gets ``is1``.

        Returns:
            ``is1``.
        """

        return self._is1

    @is1.setter
    def is1(self, is1: str | int | types.Integer) -> None:
        """
        Sets ``is1``.

        Parameters:
            is1: Segment bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if is1 is not None:
            if isinstance(is1, types.Integer):
                is1 = is1
            elif isinstance(is1, int):
                is1 = types.Integer(is1)
            elif isinstance(is1, str):
                is1 = types.Integer.from_mcnp(is1)
            else:
                raise TypeError

        self._is1: types.Integer = is1

    @property
    def im1(self) -> types.Integer:
        """
        Gets ``im1``.

        Returns:
            ``im1``.
        """

        return self._im1

    @im1.setter
    def im1(self, im1: str | int | types.Integer) -> None:
        """
        Sets ``im1``.

        Parameters:
            im1: Multiplier bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if im1 is not None:
            if isinstance(im1, types.Integer):
                im1 = im1
            elif isinstance(im1, int):
                im1 = types.Integer(im1)
            elif isinstance(im1, str):
                im1 = types.Integer.from_mcnp(im1)
            else:
                raise TypeError

        self._im1: types.Integer = im1

    @property
    def ic1(self) -> types.Integer:
        """
        Gets ``ic1``.

        Returns:
            ``ic1``.
        """

        return self._ic1

    @ic1.setter
    def ic1(self, ic1: str | int | types.Integer) -> None:
        """
        Sets ``ic1``.

        Parameters:
            ic1: Cosine bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ic1 is not None:
            if isinstance(ic1, types.Integer):
                ic1 = ic1
            elif isinstance(ic1, int):
                ic1 = types.Integer(ic1)
            elif isinstance(ic1, str):
                ic1 = types.Integer.from_mcnp(ic1)
            else:
                raise TypeError

        self._ic1: types.Integer = ic1

    @property
    def ie1(self) -> types.Integer:
        """
        Gets ``ie1``.

        Returns:
            ``ie1``.
        """

        return self._ie1

    @ie1.setter
    def ie1(self, ie1: str | int | types.Integer) -> None:
        """
        Sets ``ie1``.

        Parameters:
            ie1: Energy bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ie1 is not None:
            if isinstance(ie1, types.Integer):
                ie1 = ie1
            elif isinstance(ie1, int):
                ie1 = types.Integer(ie1)
            elif isinstance(ie1, str):
                ie1 = types.Integer.from_mcnp(ie1)
            else:
                raise TypeError

        self._ie1: types.Integer = ie1

    @property
    def it1(self) -> types.Integer:
        """
        Gets ``it1``.

        Returns:
            ``it1``.
        """

        return self._it1

    @it1.setter
    def it1(self, it1: str | int | types.Integer) -> None:
        """
        Sets ``it1``.

        Parameters:
            it1: Time bin number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if it1 is not None:
            if isinstance(it1, types.Integer):
                it1 = it1
            elif isinstance(it1, int):
                it1 = types.Integer(it1)
            elif isinstance(it1, str):
                it1 = types.Integer.from_mcnp(it1)
            else:
                raise TypeError

        self._it1: types.Integer = it1
