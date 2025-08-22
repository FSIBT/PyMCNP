import re

from . import surface
from . import _card
from .. import _show
from .. import types
from .. import errors


NUMBER = iter(range(1, 100000000))


class Surface(_card.Card):
    """
    Represents INP surface cards.
    """

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'option': surface.SurfaceOption,
    }

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)?( ({surface.SurfaceOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)

    def __init__(
        self,
        option: surface.SurfaceOption,
        number: types.Integer = next(NUMBER),
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes `Surface`.

        Parameters:
            number: surface number.
            transform: surface transformation.
            option: surface option.
            prefix: surface whitebody flag.

        Returns:
            `Surface`.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.transform: types.Integer = transform
        self.number: types.Integer = number
        self.option: surface.SurfaceOption = option
        self.prefix: types.String = prefix

    def to_mcnp(self):
        """
        Generates INP from `Surface`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self.option}'
        source = _card.Card._postprocess(source)

        return source

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Surface`.

        Returns:
            `pyvista.PolySurface` for `Surface`.
        """

        return self.option.to_show(shapes)

    def __and__(a, b):
        """
        Unites `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` union.
        """

        return types.Geometry.from_mcnp(f'{a.number}:{b.number}')

    def __or__(a, b):
        """
        Intersects `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` intersection.
        """

        return types.Geometry.from_mcnp(f'{a.number} {b.number}')

    def __neg__(self):
        """
        Negatives `Surface`.

        Returns:
            `Surface` negative.
        """

        return types.Geometry.from_mcnp(f'-{self.number}')

    def __pos__(self):
        """
        Positives `Surface`.

        Returns:
            `Surface` positive.
        """

        return types.Geometry.from_mcnp(f'+{self.number}')

    def __invert__(self):
        """
        Inverts `Surface`.

        Returns:
            `Surface` complement.
        """

        return types.Geometry.from_mcnp(f'#{self.number}')

    @property
    def number(self) -> types.Integer:
        """
        Surface number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._number

    @number.setter
    def number(self, number: str | int | types.Integer) -> None:
        """
        Sets `number`.

        Parameters:
            number: Surface number.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if number is not None:
            if isinstance(number, types.Integer):
                number = number
            elif isinstance(number, int):
                number = types.Integer(number)
            elif isinstance(number, str):
                number = types.Integer.from_mcnp(number)

        if number is None or not (1 <= number <= 99_999_999 if not self.transform else 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, number)

        self._number: types.Integer = number

    @property
    def transform(self) -> types.Integer:
        """
        Surface transform.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._transform

    @transform.setter
    def transform(self, transform: str | int | types.Integer = None) -> None:
        """
        Sets `transform`.

        Parameters:
            transform: Surface transform.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if transform is not None:
            if isinstance(transform, types.Integer):
                transform = transform
            elif isinstance(transform, int):
                transform = types.Integer(transform)
            elif isinstance(transform, str):
                transform = types.Integer.from_mcnp(transform)

        if transform is not None and not (0 <= transform <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, transform)

        self._transform: types.Integer = transform

    @property
    def option(self) -> surface.SurfaceOption:
        """
        Surface option.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._option

    @option.setter
    def option(self, option: str | surface.SurfaceOption) -> None:
        """
        Sets `option`.

        Parameters:
            option: Surface option.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if option is not None:
            if isinstance(option, surface.SurfaceOption):
                option = option
            elif isinstance(option, str):
                option = surface.SurfaceOption.from_mcnp(option)

        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, option)

        self._option: surface.SurfaceOption = option

    @property
    def prefix(self) -> types.String:
        """
        Surface whitebody/reflecting flag.

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
            prefix: Surface whitebody/reflecting flag.

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
