import re

from . import _card
from .. import types
from .. import errors


class Z(_card.Card):
    """
    Represents INP `z` surface cards.
    """

    _KEYWORD = 'z'

    _ATTRS = {
        'prefix': types.String,
        'number': types.Integer,
        'transform': types.Integer,
        'z1': types.Real,
        'r1': types.Real,
        'z2': types.Real,
        'r2': types.Real,
        'z3': types.Real,
        'r3': types.Real,
    }

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? z( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        z1: str | int | float | types.Real,
        r1: str | int | float | types.Real,
        z2: str | int | float | types.Real = None,
        r2: str | int | float | types.Real = None,
        z3: str | int | float | types.Real = None,
        r3: str | int | float | types.Real = None,
        number: types.Integer = None,
        transform: types.Integer = None,
        prefix: str = None,
    ):
        """
        Initializes `Z`.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.
            r1: Z-axisymmetric point-defined surface point #1 radius.
            z2: Z-axisymmetric point-defined surface point #2 z component.
            r2: Z-axisymmetric point-defined surface point #2 radius.
            z3: Z-axisymmetric point-defined surface point #3 z component.
            r3: Z-axisymmetric point-defined surface point #3 radius.
            number: surface number.
            transform: surface transformation.
            prefix: surface whitebody flag.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if number is None:
            number = next(_card.NUMBER)

        self.z1: types.Real = z1
        self.r1: types.Real = r1
        self.z2: types.Real = z2
        self.r2: types.Real = r2
        self.z3: types.Real = z3
        self.r3: types.Real = r3
        self.transform: types.Integer = transform
        self.number: types.Integer = number
        self.prefix: types.String = prefix

    @property
    def z1(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #1 z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z1

    @z1.setter
    def z1(self, z1: str | int | float | types.Real) -> None:
        """
        Sets `z1`.

        Parameters:
            z1: Z-axisymmetric point-defined surface point #1 z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z1 is not None:
            if isinstance(z1, types.Real):
                z1 = z1
            elif isinstance(z1, int) or isinstance(z1, float):
                z1 = types.Real(z1)
            elif isinstance(z1, str):
                z1 = types.Real.from_mcnp(z1)

        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z1)

        self._z1: types.Real = z1

    @property
    def r1(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #1 radius

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._r1

    @r1.setter
    def r1(self, r1: str | int | float | types.Real) -> None:
        """
        Sets `r1`.

        Parameters:
            r1: Z-axisymmetric point-defined surface point #1 radius.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if r1 is not None:
            if isinstance(r1, types.Real):
                r1 = r1
            elif isinstance(r1, int) or isinstance(r1, float):
                r1 = types.Real(r1)
            elif isinstance(r1, str):
                r1 = types.Real.from_mcnp(r1)

        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)

        self._r1: types.Real = r1

    @property
    def z2(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #2 z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z2

    @z2.setter
    def z2(self, z2: str | int | float | types.Real) -> None:
        """
        Sets `z2`.

        Parameters:
            z2: Z-axisymmetric point-defined surface point #2 z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z2 is not None:
            if isinstance(z2, types.Real):
                z2 = z2
            elif isinstance(z2, int) or isinstance(z2, float):
                z2 = types.Real(z2)
            elif isinstance(z2, str):
                z2 = types.Real.from_mcnp(z2)

        self._z2: types.Real = z2

    @property
    def r2(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #2 radius

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._r2

    @r2.setter
    def r2(self, r2: str | int | float | types.Real) -> None:
        """
        Sets `r2`.

        Parameters:
            r2: Z-axisymmetric point-defined surface point #2 radius.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if r2 is not None:
            if isinstance(r2, types.Real):
                r2 = r2
            elif isinstance(r2, int) or isinstance(r2, float):
                r2 = types.Real(r2)
            elif isinstance(r2, str):
                r2 = types.Real.from_mcnp(r2)

        self._r2: types.Real = r2

    @property
    def z3(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #3 z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z3

    @z3.setter
    def z3(self, z3: str | int | float | types.Real) -> None:
        """
        Sets `z3`.

        Parameters:
            z3: Z-axisymmetric point-defined surface point #3 z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z3 is not None:
            if isinstance(z3, types.Real):
                z3 = z3
            elif isinstance(z3, int) or isinstance(z3, float):
                z3 = types.Real(z3)
            elif isinstance(z3, str):
                z3 = types.Real.from_mcnp(z3)

        self._z3: types.Real = z3

    @property
    def r3(self) -> types.Real:
        """
        Z-axisymmetric point-defined surface point #3 radius

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._r3

    @r3.setter
    def r3(self, r3: str | int | float | types.Real) -> None:
        """
        Sets `r3`.

        Parameters:
            r3: Z-axisymmetric point-defined surface point #3 radius.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if r3 is not None:
            if isinstance(r3, types.Real):
                r3 = r3
            elif isinstance(r3, int) or isinstance(r3, float):
                r3 = types.Real(r3)
            elif isinstance(r3, str):
                r3 = types.Real.from_mcnp(r3)

        self._r3: types.Real = r3

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

        if number is None or not (1 <= number <= (99_999_999 if not self.transform else 999)):
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

    def to_mcnp(self):
        """
        Generates INP from `Z`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.z1} {self.r1} {self.z2 if self.z2 is not None else ""} {self.r2 if self.r2 is not None else ""} {self.z3 if self.z3 is not None else ""} {self.r3 if self.r3 is not None else ""}'
        source = _card.Card._postprocess(source)

        return source
