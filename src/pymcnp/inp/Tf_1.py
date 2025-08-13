import re

from . import _card
from .. import types
from .. import errors


class Tf_1(_card.Card):
    """
    Represents INP `tf` elements variation #1.
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
        'if2': types.Integer,
        'id2': types.Integer,
        'iu2': types.Integer,
        'is2': types.Integer,
        'im2': types.Integer,
        'ic2': types.Integer,
        'ie2': types.Integer,
        'it2': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Atf(\d+)( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
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
        if2: str | int | types.Integer = None,
        id2: str | int | types.Integer = None,
        iu2: str | int | types.Integer = None,
        is2: str | int | types.Integer = None,
        im2: str | int | types.Integer = None,
        ic2: str | int | types.Integer = None,
        ie2: str | int | types.Integer = None,
        it2: str | int | types.Integer = None,
    ):
        """
        Initializes `Tf_1`.

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
            if2: Cell, surface, or detector bin number.
            id2: Total, flagged, or un-collided bin number.
            iu2: User bin number.
            is2: Segment bin number.
            im2: Multiplier bin number.
            ic2: Cosine bin number.
            ie2: Energy bin number.
            it2: Time bin number.

        Raises:
            InpError: SEMANTICS_CARD.
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
        self.if2: types.Integer = if2
        self.id2: types.Integer = id2
        self.iu2: types.Integer = iu2
        self.is2: types.Integer = is2
        self.im2: types.Integer = im2
        self.ic2: types.Integer = ic2
        self.ie2: types.Integer = ie2
        self.it2: types.Integer = it2

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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def if1(self) -> types.Integer:
        """
        Cell, surface, or detector bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._if1

    @if1.setter
    def if1(self, if1: str | int | types.Integer) -> None:
        """
        Sets `if1`.

        Parameters:
            if1: Cell, surface, or detector bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if if1 is not None:
            if isinstance(if1, types.Integer):
                if1 = if1
            elif isinstance(if1, int):
                if1 = types.Integer(if1)
            elif isinstance(if1, str):
                if1 = types.Integer.from_mcnp(if1)

        self._if1: types.Integer = if1

    @property
    def id1(self) -> types.Integer:
        """
        Total, flagged, or un-collided bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._id1

    @id1.setter
    def id1(self, id1: str | int | types.Integer) -> None:
        """
        Sets `id1`.

        Parameters:
            id1: Total, flagged, or un-collided bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if id1 is not None:
            if isinstance(id1, types.Integer):
                id1 = id1
            elif isinstance(id1, int):
                id1 = types.Integer(id1)
            elif isinstance(id1, str):
                id1 = types.Integer.from_mcnp(id1)

        self._id1: types.Integer = id1

    @property
    def iu1(self) -> types.Integer:
        """
        User bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._iu1

    @iu1.setter
    def iu1(self, iu1: str | int | types.Integer) -> None:
        """
        Sets `iu1`.

        Parameters:
            iu1: User bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if iu1 is not None:
            if isinstance(iu1, types.Integer):
                iu1 = iu1
            elif isinstance(iu1, int):
                iu1 = types.Integer(iu1)
            elif isinstance(iu1, str):
                iu1 = types.Integer.from_mcnp(iu1)

        self._iu1: types.Integer = iu1

    @property
    def is1(self) -> types.Integer:
        """
        Segment bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._is1

    @is1.setter
    def is1(self, is1: str | int | types.Integer) -> None:
        """
        Sets `is1`.

        Parameters:
            is1: Segment bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if is1 is not None:
            if isinstance(is1, types.Integer):
                is1 = is1
            elif isinstance(is1, int):
                is1 = types.Integer(is1)
            elif isinstance(is1, str):
                is1 = types.Integer.from_mcnp(is1)

        self._is1: types.Integer = is1

    @property
    def im1(self) -> types.Integer:
        """
        Multiplier bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._im1

    @im1.setter
    def im1(self, im1: str | int | types.Integer) -> None:
        """
        Sets `im1`.

        Parameters:
            im1: Multiplier bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if im1 is not None:
            if isinstance(im1, types.Integer):
                im1 = im1
            elif isinstance(im1, int):
                im1 = types.Integer(im1)
            elif isinstance(im1, str):
                im1 = types.Integer.from_mcnp(im1)

        self._im1: types.Integer = im1

    @property
    def ic1(self) -> types.Integer:
        """
        Cosine bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ic1

    @ic1.setter
    def ic1(self, ic1: str | int | types.Integer) -> None:
        """
        Sets `ic1`.

        Parameters:
            ic1: Cosine bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ic1 is not None:
            if isinstance(ic1, types.Integer):
                ic1 = ic1
            elif isinstance(ic1, int):
                ic1 = types.Integer(ic1)
            elif isinstance(ic1, str):
                ic1 = types.Integer.from_mcnp(ic1)

        self._ic1: types.Integer = ic1

    @property
    def ie1(self) -> types.Integer:
        """
        Energy bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ie1

    @ie1.setter
    def ie1(self, ie1: str | int | types.Integer) -> None:
        """
        Sets `ie1`.

        Parameters:
            ie1: Energy bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ie1 is not None:
            if isinstance(ie1, types.Integer):
                ie1 = ie1
            elif isinstance(ie1, int):
                ie1 = types.Integer(ie1)
            elif isinstance(ie1, str):
                ie1 = types.Integer.from_mcnp(ie1)

        self._ie1: types.Integer = ie1

    @property
    def it1(self) -> types.Integer:
        """
        Time bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._it1

    @it1.setter
    def it1(self, it1: str | int | types.Integer) -> None:
        """
        Sets `it1`.

        Parameters:
            it1: Time bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if it1 is not None:
            if isinstance(it1, types.Integer):
                it1 = it1
            elif isinstance(it1, int):
                it1 = types.Integer(it1)
            elif isinstance(it1, str):
                it1 = types.Integer.from_mcnp(it1)

        self._it1: types.Integer = it1

    @property
    def if2(self) -> types.Integer:
        """
        Cell, surface, or detector bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._if2

    @if2.setter
    def if2(self, if2: str | int | types.Integer) -> None:
        """
        Sets `if2`.

        Parameters:
            if2: Cell, surface, or detector bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if if2 is not None:
            if isinstance(if2, types.Integer):
                if2 = if2
            elif isinstance(if2, int):
                if2 = types.Integer(if2)
            elif isinstance(if2, str):
                if2 = types.Integer.from_mcnp(if2)

        self._if2: types.Integer = if2

    @property
    def id2(self) -> types.Integer:
        """
        Total, flagged, or un-collided bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._id2

    @id2.setter
    def id2(self, id2: str | int | types.Integer) -> None:
        """
        Sets `id2`.

        Parameters:
            id2: Total, flagged, or un-collided bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if id2 is not None:
            if isinstance(id2, types.Integer):
                id2 = id2
            elif isinstance(id2, int):
                id2 = types.Integer(id2)
            elif isinstance(id2, str):
                id2 = types.Integer.from_mcnp(id2)

        self._id2: types.Integer = id2

    @property
    def iu2(self) -> types.Integer:
        """
        User bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._iu2

    @iu2.setter
    def iu2(self, iu2: str | int | types.Integer) -> None:
        """
        Sets `iu2`.

        Parameters:
            iu2: User bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if iu2 is not None:
            if isinstance(iu2, types.Integer):
                iu2 = iu2
            elif isinstance(iu2, int):
                iu2 = types.Integer(iu2)
            elif isinstance(iu2, str):
                iu2 = types.Integer.from_mcnp(iu2)

        self._iu2: types.Integer = iu2

    @property
    def is2(self) -> types.Integer:
        """
        Segment bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._is2

    @is2.setter
    def is2(self, is2: str | int | types.Integer) -> None:
        """
        Sets `is2`.

        Parameters:
            is2: Segment bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if is2 is not None:
            if isinstance(is2, types.Integer):
                is2 = is2
            elif isinstance(is2, int):
                is2 = types.Integer(is2)
            elif isinstance(is2, str):
                is2 = types.Integer.from_mcnp(is2)

        self._is2: types.Integer = is2

    @property
    def im2(self) -> types.Integer:
        """
        Multiplier bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._im2

    @im2.setter
    def im2(self, im2: str | int | types.Integer) -> None:
        """
        Sets `im2`.

        Parameters:
            im2: Multiplier bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if im2 is not None:
            if isinstance(im2, types.Integer):
                im2 = im2
            elif isinstance(im2, int):
                im2 = types.Integer(im2)
            elif isinstance(im2, str):
                im2 = types.Integer.from_mcnp(im2)

        self._im2: types.Integer = im2

    @property
    def ic2(self) -> types.Integer:
        """
        Cosine bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ic2

    @ic2.setter
    def ic2(self, ic2: str | int | types.Integer) -> None:
        """
        Sets `ic2`.

        Parameters:
            ic2: Cosine bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ic2 is not None:
            if isinstance(ic2, types.Integer):
                ic2 = ic2
            elif isinstance(ic2, int):
                ic2 = types.Integer(ic2)
            elif isinstance(ic2, str):
                ic2 = types.Integer.from_mcnp(ic2)

        self._ic2: types.Integer = ic2

    @property
    def ie2(self) -> types.Integer:
        """
        Energy bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ie2

    @ie2.setter
    def ie2(self, ie2: str | int | types.Integer) -> None:
        """
        Sets `ie2`.

        Parameters:
            ie2: Energy bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ie2 is not None:
            if isinstance(ie2, types.Integer):
                ie2 = ie2
            elif isinstance(ie2, int):
                ie2 = types.Integer(ie2)
            elif isinstance(ie2, str):
                ie2 = types.Integer.from_mcnp(ie2)

        self._ie2: types.Integer = ie2

    @property
    def it2(self) -> types.Integer:
        """
        Time bin number

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._it2

    @it2.setter
    def it2(self, it2: str | int | types.Integer) -> None:
        """
        Sets `it2`.

        Parameters:
            it2: Time bin number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if it2 is not None:
            if isinstance(it2, types.Integer):
                it2 = it2
            elif isinstance(it2, int):
                it2 = types.Integer(it2)
            elif isinstance(it2, str):
                it2 = types.Integer.from_mcnp(it2)

        self._it2: types.Integer = it2
