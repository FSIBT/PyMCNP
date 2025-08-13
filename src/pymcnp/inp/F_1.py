import re

from . import f_1
from . import _card
from .. import types
from .. import errors


class F_1(_card.Card):
    """
    Represents INP `f` elements variation #1.
    """

    _KEYWORD = 'f'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'designator': types.Designator,
        'spheres': types.Tuple(f_1.Sphere),
        'nd': types.String,
    }

    _REGEX = re.compile(r'\A([*+])?f(\d*[5])(?::(\S+))?((?: \S+ \S+ \S+ \S+)+?)( nd)?\Z', re.IGNORECASE)

    def __init__(
        self, suffix: str | int | types.Integer, spheres: list[str] | list[f_1.Sphere], prefix: str | types.String = None, designator: str | types.Designator = None, nd: str | types.String = None
    ):
        """
        Initializes `F_1`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            designator: Data card particle designator.
            spheres: Detector points.
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.spheres: types.Tuple(f_1.Sphere) = spheres
        self.nd: types.String = nd

    @property
    def prefix(self) -> types.String:
        """
        Star prefix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*', '+'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

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

        if suffix is None or not (suffix <= 99_999_999 and suffix % 10 == 5):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data card particle designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        self._designator: types.Designator = designator

    @property
    def spheres(self) -> types.Tuple(f_1.Sphere):
        """
        Detector points

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres

    @spheres.setter
    def spheres(self, spheres: list[str] | list[f_1.Sphere]) -> None:
        """
        Sets `spheres`.

        Parameters:
            spheres: Detector points.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres is not None:
            array = []
            for item in spheres:
                if isinstance(item, f_1.Sphere):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(f_1.Sphere.from_mcnp(item))
            spheres = types.Tuple(f_1.Sphere)(array)

        if spheres is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres)

        self._spheres: types.Tuple(f_1.Sphere) = spheres

    @property
    def nd(self) -> types.String:
        """
        Total/average specified surfaces/cells option

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nd

    @nd.setter
    def nd(self, nd: str | types.String) -> None:
        """
        Sets `nd`.

        Parameters:
            nd: Total/average specified surfaces/cells option.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nd is not None:
            if isinstance(nd, types.String):
                nd = nd
            elif isinstance(nd, str):
                nd = types.String.from_mcnp(nd)

        if nd is not None and not (nd == 'nd'):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nd)

        self._nd: types.String = nd
