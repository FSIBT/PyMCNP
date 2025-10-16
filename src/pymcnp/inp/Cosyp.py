import re

from . import _card
from .. import types
from .. import errors


class Cosyp(_card.Card):
    """
    Represents INP cosyp cards.
    """

    _KEYWORD = 'cosyp'

    _ATTRS = {
        'pre': types.Integer,
        'axsh': types.Integer,
        'axsv': types.Integer,
        'emaps': types.Tuple(types.Real),
    }

    _REGEX = re.compile(
        rf'\Acosyp( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE
    )

    def __init__(self, pre: str | int | types.Integer, axsh: str | int | types.Integer, axsv: str | int | types.Integer, emaps: list[str] | list[float] | list[types.Real]):
        """
        Initializes `Cosyp`.

        Parameters:
            pre: Prefix number of the COSY map files.
            axsh: Horiztonal axis orientation.
            axsv: Vertical axis orientation.
            emaps: Tuple of operating beam energies.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.pre: types.Integer = pre
        self.axsh: types.Integer = axsh
        self.axsv: types.Integer = axsv
        self.emaps: types.Tuple(types.Real) = emaps

    @property
    def pre(self) -> types.Integer:
        """
        Prefix number of the COSY map files

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._pre

    @pre.setter
    def pre(self, pre: str | int | types.Integer) -> None:
        """
        Sets `pre`.

        Parameters:
            pre: Prefix number of the COSY map files.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if pre is not None:
            if isinstance(pre, types.Integer):
                pre = pre
            elif isinstance(pre, int):
                pre = types.Integer(pre)
            elif isinstance(pre, str):
                pre = types.Integer.from_mcnp(pre)

        if pre is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, pre)

        self._pre: types.Integer = pre

    @property
    def axsh(self) -> types.Integer:
        """
        Horiztonal axis orientation

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._axsh

    @axsh.setter
    def axsh(self, axsh: str | int | types.Integer) -> None:
        """
        Sets `axsh`.

        Parameters:
            axsh: Horiztonal axis orientation.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if axsh is not None:
            if isinstance(axsh, types.Integer):
                axsh = axsh
            elif isinstance(axsh, int):
                axsh = types.Integer(axsh)
            elif isinstance(axsh, str):
                axsh = types.Integer.from_mcnp(axsh)

        if axsh is None or axsh not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, axsh)

        self._axsh: types.Integer = axsh

    @property
    def axsv(self) -> types.Integer:
        """
        Vertical axis orientation

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._axsv

    @axsv.setter
    def axsv(self, axsv: str | int | types.Integer) -> None:
        """
        Sets `axsv`.

        Parameters:
            axsv: Vertical axis orientation.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if axsv is not None:
            if isinstance(axsv, types.Integer):
                axsv = axsv
            elif isinstance(axsv, int):
                axsv = types.Integer(axsv)
            elif isinstance(axsv, str):
                axsv = types.Integer.from_mcnp(axsv)

        if axsv is None or axsv not in {1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, axsv)

        self._axsv: types.Integer = axsv

    @property
    def emaps(self) -> types.Tuple(types.Real):
        """
        Tuple of operating beam energies

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._emaps

    @emaps.setter
    def emaps(self, emaps: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets `emaps`.

        Parameters:
            emaps: Tuple of operating beam energies.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if emaps is not None:
            array = []
            for item in emaps:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            emaps = types.Tuple(types.Real)(array)

        if emaps is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, emaps)

        self._emaps: types.Tuple(types.Real) = emaps
