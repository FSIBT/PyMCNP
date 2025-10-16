import re

from . import contour
from . import _option
from ... import types
from ... import errors


class Contour(_option.MplotOption):
    """
    Represents INP `contour` elements.
    """

    _KEYWORD = 'contour'

    _ATTRS = {
        'cmin': types.Real,
        'cmax': types.Real,
        'cstep': types.Real,
        'options': types.Tuple(contour.ContourOption),
    }

    _REGEX = re.compile(
        rf'\Acontour( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})((?: (?:{contour.ContourOption._REGEX.pattern[2:-2]}))+?)?\Z',
        re.IGNORECASE,
    )

    def __init__(self, cmin: str | int | float | types.Real, cmax: str | int | float | types.Real, cstep: str | int | float | types.Real, options: list[str] | list[contour.ContourOption] = None):
        """
        Initializes `Contour`.

        Parameters:
            cmin: Contour lower limit.
            cmax: Contour upper limit.
            cstep: Contour interval.
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.cmin: types.Real = cmin
        self.cmax: types.Real = cmax
        self.cstep: types.Real = cstep
        self.options: types.Tuple(contour.ContourOption) = options

    @property
    def cmin(self) -> types.Real:
        """
        Contour lower limit

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cmin

    @cmin.setter
    def cmin(self, cmin: str | int | float | types.Real) -> None:
        """
        Sets `cmin`.

        Parameters:
            cmin: Contour lower limit.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cmin is not None:
            if isinstance(cmin, types.Real):
                cmin = cmin
            elif isinstance(cmin, int) or isinstance(cmin, float):
                cmin = types.Real(cmin)
            elif isinstance(cmin, str):
                cmin = types.Real.from_mcnp(cmin)

        if cmin is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cmin)

        self._cmin: types.Real = cmin

    @property
    def cmax(self) -> types.Real:
        """
        Contour upper limit

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cmax

    @cmax.setter
    def cmax(self, cmax: str | int | float | types.Real) -> None:
        """
        Sets `cmax`.

        Parameters:
            cmax: Contour upper limit.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cmax is not None:
            if isinstance(cmax, types.Real):
                cmax = cmax
            elif isinstance(cmax, int) or isinstance(cmax, float):
                cmax = types.Real(cmax)
            elif isinstance(cmax, str):
                cmax = types.Real.from_mcnp(cmax)

        if cmax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cmax)

        self._cmax: types.Real = cmax

    @property
    def cstep(self) -> types.Real:
        """
        Contour interval

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._cstep

    @cstep.setter
    def cstep(self, cstep: str | int | float | types.Real) -> None:
        """
        Sets `cstep`.

        Parameters:
            cstep: Contour interval.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cstep is not None:
            if isinstance(cstep, types.Real):
                cstep = cstep
            elif isinstance(cstep, int) or isinstance(cstep, float):
                cstep = types.Real(cstep)
            elif isinstance(cstep, str):
                cstep = types.Real.from_mcnp(cstep)

        if cstep is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, cstep)

        self._cstep: types.Real = cstep

    @property
    def options(self) -> types.Tuple(contour.ContourOption):
        """
        Dictionary of options

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._options

    @options.setter
    def options(self, options: list[str] | list[contour.ContourOption]) -> None:
        """
        Sets `options`.

        Parameters:
            options: Dictionary of options.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if options is not None:
            array = []
            for item in options:
                if isinstance(item, contour.ContourOption):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(contour.ContourOption.from_mcnp(item))
            options = types.Tuple(contour.ContourOption)(array)

        self._options: types.Tuple(contour.ContourOption) = options
