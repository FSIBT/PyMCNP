import re

from . import _entry
from ... import types
from ... import errors
from ...utils import _parser


class Geometry(_entry.CellEntry):
    """
    Represents MCNP geometries.

    Attributes:
        infix: Geometry infix formula.
    """

    _REGEX = re.compile(r'\A(.+)\Z', re.IGNORECASE)

    def __init__(self, infix: types.String):
        """
        Initializes ``Geometry``.

        Parameters:
            infix: Geometry infix formula.

        Returns:
            ``Geometry``.

        Raises:
            InpError: SEMANTICS_ENTRY.
        """

        self.infix: types.String = infix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Geometry`` from INP.

        Parameters:
            INP for ``Geometry``.

        Returns:
            ``Geometry``.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Geometry._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        infix = types.String.from_mcnp(tokens[1])

        return Geometry(infix)

    def to_mcnp(self):
        """
        Generates INP from ``Geometry``.

        Returns:
            INP for ``Geometry``.
        """

        return self.infix.value

    def __and__(a, b):
        """
        Unites ``Geometry``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Geometry`` union.
        """

        return Geometry(infix=f'({a.infix}):({b.infix})')

    def __or__(a, b):
        """
        Intersects ``Geometry``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Geometry`` intersection.
        """

        return Geometry(infix=f'({a.infix}) ({b.infix})')

    def __neg__(self):
        """
        Negatives ``Geometry``.

        Returns:
            ``Geometry`` negative.
        """

        return Geometry(infix=f'-({self.infix})')

    def __pos__(self):
        """
        Positives ``Geometry``.

        Returns:
            ``Geometry`` positive.
        """

        return Geometry(infix=f'+({self.infix})')

    def __invert__(self):
        """
        Inverts ``Geometry``.

        Returns:
            ``Geometry`` complement.
        """

        return Geometry(infix=f'#({self.infix})')

    @property
    def infix(self) -> types.String:
        """
        Geometry infix formula.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._infix

    @infix.setter
    def infix(self, infix: str | types.String) -> None:
        """
        Sets ``infix``.

        Parameters:
            infix: Geometry infix formula.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if infix is not None:
            if isinstance(infix, types.String):
                infix = infix
            elif isinstance(infix, str):
                infix = types.String.from_mcnp(infix)

        if infix is None:
            raise errors.TypesError(errors.InpCode.SEMANTICS_ENTRY, infix)

        temp = re.sub(r' 0+', '', infix.value)
        temp = re.sub(r' +', ' ', temp)
        temp = re.sub(r'\+', '', temp)
        temp = re.sub(r' ?: ?', '+', temp)
        temp = re.sub(r' ', '*', temp)
        temp = re.sub(r'#', '-', temp)
        temp = re.sub(r'\+-', '-', temp)
        temp = re.sub(r'(\d)\(', r'\1*(', temp)

        for number in re.split(r'[*#:+ ()-]+', temp):
            if number and not re.match(r'\d+(?:[.][1-8])?', number):
                raise errors.TypesError(errors.InpCode.SEMANTICS_ENTRY, infix)

        try:
            eval(temp)
        except Exception:
            raise errors.TypesError(errors.InpCode.SEMANTICS_ENTRY, infix)

        self._infix: types.String = infix
