"""
Contains the ``Mesh`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_option import DataOption
from ..data_keyword import DataKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class MeshKeyword(DataKeyword):
    """
    Represents INP mesh data card option keywords.

    ``MeshKeyword`` implements ``DataKeyword``.
    """

    GEOM = 'geom'
    REF = 'ref'
    ORIGIN = 'origin'
    AXS = 'axs'
    VEC = 'vec'
    IMESH = 'imesh'
    IINTS = 'iints'
    JMESH = 'jmesh'
    JINTS = 'jints'
    KMESH = 'kmesh'
    KINTS = 'kints'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``MeshKeyword``.

        Returns:
            ``MeshKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return MeshKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Geom(DataOption):
    """
    Represents INP geom data card geom options.

    ``Geom`` implements ``DataOption``.

    Attributes:
        geometry: Controls mesh geometry type.
    """

    def __init__(self, geometry: str):
        """
        Initializes ``Mesh``.

        Parameters:
            geometry: Controls mesh geometry type.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if geometry is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MeshKeyword] = MeshKeyword.GEOM
        self.value: Final[str] = geometry
        self.geometry: Final[str] = geometry

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Geom`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Geom``.

        Returns:
            ``Geom`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'geom':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Geom(value)


class Ref(DataOption):
    """
    Represents INP ref data card ref options.

    ``Ref`` implements ``DataOption``.

    Attributes:
        point: Mesh reference point.
    """

    def __init__(self, point: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            point: Mesh reference point.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if point is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in point:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(point))

        self.keyword: Final[MeshKeyword] = MeshKeyword.REF
        self.value: Final[tuple[types.McnpReal]] = point
        self.point: Final[tuple[types.McnpReal]] = point

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ref`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ref``.

        Returns:
            ``Ref`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ref':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Ref(value)


class Origin(DataOption):
    """
    Represents INP origin data card origin options.

    ``Origin`` implements ``DataOption``.

    Attributes:
        point: Mesh origin point.
    """

    def __init__(self, point: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            point: Mesh origin point.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if point is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in point:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(point))

        self.keyword: Final[MeshKeyword] = MeshKeyword.ORIGIN
        self.value: Final[tuple[types.McnpReal]] = point
        self.point: Final[tuple[types.McnpReal]] = point

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Origin`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Origin``.

        Returns:
            ``Origin`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'origin':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Origin(value)


class Axs(DataOption):
    """
    Represents INP axs data card axs options.

    ``Axs`` implements ``DataOption``.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            vector: Vector giving the direction of the polar axis.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[MeshKeyword] = MeshKeyword.AXS
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


class Vec(DataOption):
    """
    Represents INP vec data card vec options.

    ``Vec`` implements ``DataOption``.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            vector: Vector giving the direction of the polar axis.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[MeshKeyword] = MeshKeyword.VEC
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


class Imesh(DataOption):
    """
    Represents INP imesh data card imesh options.

    ``Imesh`` implements ``DataOption``.

    Attributes:
        vector: Locations of the coarse meshes in the x/r directions.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            vector: Locations of the coarse meshes in the x/r directions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[MeshKeyword] = MeshKeyword.IMESH
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Imesh`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Imesh``.

        Returns:
            ``Imesh`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'imesh':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Imesh(value)


class Iints(DataOption):
    """
    Represents INP iints data card iints options.

    ``Iints`` implements ``DataOption``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the x/r directions.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Mesh``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the x/r directions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MeshKeyword] = MeshKeyword.IINTS
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Iints`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Iints``.

        Returns:
            ``Iints`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'iints':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Iints(value)


class Jmesh(DataOption):
    """
    Represents INP jmesh data card jmesh options.

    ``Jmesh`` implements ``DataOption``.

    Attributes:
        vector: Locations of the coarse meshes in the y/z directions.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            vector: Locations of the coarse meshes in the y/z directions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[MeshKeyword] = MeshKeyword.JMESH
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Jmesh`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Jmesh``.

        Returns:
            ``Jmesh`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'jmesh':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Jmesh(value)


class Jints(DataOption):
    """
    Represents INP jints data card jints options.

    ``Jints`` implements ``DataOption``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the y/z directions.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Mesh``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the y/z directions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MeshKeyword] = MeshKeyword.JINTS
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Jints`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Jints``.

        Returns:
            ``Jints`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'jints':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Jints(value)


class Kmesh(DataOption):
    """
    Represents INP kmesh data card kmesh options.

    ``Kmesh`` implements ``DataOption``.

    Attributes:
        vector: Locations of the coarse meshes in the z/theta directions.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Mesh``.

        Parameters:
            vector: Locations of the coarse meshes in the z/theta directions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[MeshKeyword] = MeshKeyword.KMESH
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Kmesh`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Kmesh``.

        Returns:
            ``Kmesh`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'kmesh':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Kmesh(value)


class Kints(DataOption):
    """
    Represents INP kints data card kints options.

    ``Kints`` implements ``DataOption``.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Mesh``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the z/theta directions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MeshKeyword] = MeshKeyword.KINTS
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Kints`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Kints``.

        Returns:
            ``Kints`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'kints':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Kints(value)


class Mesh(Data):
    """
    Represents INP mesh data cards.

    ``Mesh`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Mesh``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.MESH
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'mesh'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mesh`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for mesh data cards.

        Returns:
            ``Mesh`` object.

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
        if mnemonic != 'mesh':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(
            r'geom|ref|origin|axs|vec|imesh|iints|jmesh|jints|kmesh|kints', ' '.join(tokens.deque)
        )
        values = re.split(
            r'geom|ref|origin|axs|vec|imesh|iints|jmesh|jints|kmesh|kints', ' '.join(tokens.deque)
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'geom':
                    pairs['geom'] = Geom.from_mcnp(f'{keyword}={value}')
                case 'ref':
                    pairs['ref'] = Ref.from_mcnp(f'{keyword}={value}')
                case 'origin':
                    pairs['origin'] = Origin.from_mcnp(f'{keyword}={value}')
                case 'axs':
                    pairs['axs'] = Axs.from_mcnp(f'{keyword}={value}')
                case 'vec':
                    pairs['vec'] = Vec.from_mcnp(f'{keyword}={value}')
                case 'imesh':
                    pairs['imesh'] = Imesh.from_mcnp(f'{keyword}={value}')
                case 'iints':
                    pairs['iints'] = Iints.from_mcnp(f'{keyword}={value}')
                case 'jmesh':
                    pairs['jmesh'] = Jmesh.from_mcnp(f'{keyword}={value}')
                case 'jints':
                    pairs['jints'] = Jints.from_mcnp(f'{keyword}={value}')
                case 'kmesh':
                    pairs['kmesh'] = Kmesh.from_mcnp(f'{keyword}={value}')
                case 'kints':
                    pairs['kints'] = Kints.from_mcnp(f'{keyword}={value}')

        data = Mesh(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Mesh`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Mesh``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
