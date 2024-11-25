"""
Contains the ``Bfld`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ...utils import types, errors, _parser


class BfldKeyword(DataKeyword):
    """
    Represents INP bfld data card option keywords.

    ``BfldKeyword`` implements ``DataKeyword``.
    """

    FIELD = 'field'
    VEC = 'vec'
    MAXDEFLC = 'maxdeflc'
    MAXSTEP = 'maxstep'
    AXS = 'axs'
    FFEDGES = 'ffedges'
    REFPNT = 'refpnt'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``BfldKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``BfldKeyword``.

        Returns:
            ``BfldKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return BfldKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Field(DataOption):
    """
    Represents INP field data card field options.

    ``Field`` implements ``DataOption``.

    Attributes:
        strength_gradient: Magnetic field strength/gradient.
    """

    def __init__(self, strength_gradient: types.McnpReal):
        """
        Initializes ``Bfld``.

        Parameters:
            strength_gradient: Magnetic field strength/gradient.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if strength_gradient is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[BfldKeyword] = BfldKeyword.FIELD
        self.value: Final[types.McnpReal] = strength_gradient
        self.strength_gradient: Final[types.McnpReal] = strength_gradient

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Field`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Field``.

        Returns:
            ``Field`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'field':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Field(value)


class Vec(DataOption):
    """
    Represents INP vec data card vec options.

    ``Vec`` implements ``DataOption``.

    Attributes:
        vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Bfld``.

        Parameters:
            vector: Direction of mangentic field or plane corresponding to the x-axis of the quadrapole.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[BfldKeyword] = BfldKeyword.VEC
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Vec`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Vec``.

        Returns:
            ``Vec`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'vec':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Vec(value)


class Maxdeflc(DataOption):
    """
    Represents INP maxdeflc data card maxdeflc options.

    ``Maxdeflc`` implements ``DataOption``.

    Attributes:
        angle: Maximum deflection angles.
    """

    def __init__(self, angle: types.McnpReal):
        """
        Initializes ``Bfld``.

        Parameters:
            angle: Maximum deflection angles.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if angle is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[BfldKeyword] = BfldKeyword.MAXDEFLC
        self.value: Final[types.McnpReal] = angle
        self.angle: Final[types.McnpReal] = angle

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Maxdeflc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Maxdeflc``.

        Returns:
            ``Maxdeflc`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'maxdeflc':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Maxdeflc(value)


class Maxstep(DataOption):
    """
    Represents INP maxstep data card maxstep options.

    ``Maxstep`` implements ``DataOption``.

    Attributes:
        size: Maximum step size.
    """

    def __init__(self, size: types.McnpReal):
        """
        Initializes ``Bfld``.

        Parameters:
            size: Maximum step size.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if size is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[BfldKeyword] = BfldKeyword.MAXSTEP
        self.value: Final[types.McnpReal] = size
        self.size: Final[types.McnpReal] = size

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Maxstep`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Maxstep``.

        Returns:
            ``Maxstep`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'maxstep':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Maxstep(value)


class Axs(DataOption):
    """
    Represents INP axs data card axs options.

    ``Axs`` implements ``DataOption``.

    Attributes:
        vector: Direction of the cosines of the quadropole beam axis.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Bfld``.

        Parameters:
            vector: Direction of the cosines of the quadropole beam axis.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[BfldKeyword] = BfldKeyword.AXS
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Axs`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Axs``.

        Returns:
            ``Axs`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'axs':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Axs(value)


class Ffedges(DataOption):
    """
    Represents INP ffedges data card ffedges options.

    ``Ffedges`` implements ``DataOption``.

    Attributes:
        numbers: Surface numbers to apply field fringe edges.
    """

    def __init__(self, numbers: tuple[types.McnpReal]):
        """
        Initializes ``Bfld``.

        Parameters:
            numbers: Surface numbers to apply field fringe edges.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[BfldKeyword] = BfldKeyword.FFEDGES
        self.value: Final[tuple[types.McnpReal]] = numbers
        self.numbers: Final[tuple[types.McnpReal]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ffedges`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ffedges``.

        Returns:
            ``Ffedges`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ffedges':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Ffedges(value)


class Refpnt(DataOption):
    """
    Represents INP refpnt data card refpnt options.

    ``Refpnt`` implements ``DataOption``.

    Attributes:
        point: Point anywhere on the quadrapole beam.
    """

    def __init__(self, point: tuple[types.McnpReal]):
        """
        Initializes ``Bfld``.

        Parameters:
            point: Point anywhere on the quadrapole beam.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if point is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in point:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(point))

        self.keyword: Final[BfldKeyword] = BfldKeyword.REFPNT
        self.value: Final[tuple[types.McnpReal]] = point
        self.point: Final[tuple[types.McnpReal]] = point

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Refpnt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Refpnt``.

        Returns:
            ``Refpnt`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'refpnt':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Refpnt(value)


class Bfld(Data):
    """
    Represents INP bfld data cards.

    ``Bfld`` implements ``Data``.

    Attributes:
        kind: Magnetic field type.
        suffix: Data card suffix..
        pairs: Dictionary of options.
    """

    def __init__(self, kind: str, suffix: types.McnpInteger, pairs: dict[DataOption]):
        """
        Initializes ``Bfld``.

        Parameters:
            kind: Magnetic field type.
            suffix: Data card suffix..
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if kind is None or type not in {'const', 'quad', 'quadff'}:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(kind))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.BFLD
        self.parameters: Final[tuple[any]] = tuple([kind] + [suffix] + [pairs])
        self.kind: Final[str] = kind
        self.suffix: Final[types.McnpInteger] = suffix
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = f'bfld{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Bfld`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for bfld data cards.

        Returns:
            ``Bfld`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |:|=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        mnemonic = mnemonic[0] if mnemonic else ''
        if mnemonic != 'bfld':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[4:])

        kind = tokens.popl()
        pairs = {}
        keywords = re.findall(
            r'field|vec|maxdeflc|maxstep|axs|ffedges|refpnt', ' '.join(tokens.deque)
        )
        values = re.split(r'field|vec|maxdeflc|maxstep|axs|ffedges|refpnt', ' '.join(tokens.deque))[
            1:
        ]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'field':
                    pairs['field'] = Field.from_mcnp(f'{keyword}={value}')
                case 'vec':
                    pairs['vec'] = Vec.from_mcnp(f'{keyword}={value}')
                case 'maxdeflc':
                    pairs['maxdeflc'] = Maxdeflc.from_mcnp(f'{keyword}={value}')
                case 'maxstep':
                    pairs['maxstep'] = Maxstep.from_mcnp(f'{keyword}={value}')
                case 'axs':
                    pairs['axs'] = Axs.from_mcnp(f'{keyword}={value}')
                case 'ffedges':
                    pairs['ffedges'] = Ffedges.from_mcnp(f'{keyword}={value}')
                case 'refpnt':
                    pairs['refpnt'] = Refpnt.from_mcnp(f'{keyword}={value}')

        data = Bfld(kind, suffix, pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Bfld`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Bfld``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {self.kind.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
