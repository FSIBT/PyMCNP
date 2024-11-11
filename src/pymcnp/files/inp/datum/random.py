from enum import Enum
import re
from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class RandomKeyword(str, Enum):
    """
    ``RandomKeyword`` represents INP random number generator
    data card keywords.

    ``RandomKeyword`` implements INP random number generator
    data card keywords as a Python inner class. It enumerates MCNP
    keywords and provides methods for casting strings to
    ``RandomKeyword`` instances. It represents the INP
    random number generator data card keyword syntax element, so
    ``Random`` and ``RandomOption`` depend on
    ``RandomKeyword`` as an enum.
    """

    GEN = 'gen'
    SEED = 'seed'
    STRIDE = 'stride'
    HIST = 'hist'

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``RandomKeyword`` objects
        from INP.

        ``from_mcnp`` constructs instances of
        ``RandomKeyword`` from INP source strings, so it
        operates as a class constructor method and INP parser helper
        function.

        Parameters:
            source: INP for source definition option keyword.

        Returns:
            ``RandomKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_RAND_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in RandomKeyword]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_RAND_KEYWORD)

        return RandomKeyword(source)


class RandomOption:
    """
    ``RandomOption`` represents INP random number generator data
    card options.

    ``RandomOption`` implements INP random number generator data
    card options. Its attributes store keywords and values, and its methods
    provide entry and endpoints for working with INP random number
    generator data card options. It represents the generic INP random
    number generator data card option syntax element, so
    ``Random`` depends on ``RandomOption`` as a generic
    data structure and superclass.

    """

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``RandomOption`` objects from
        INP.

        ``from_mcnp`` constructs instances of ``RandomOption``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function. Although defined on the
        superclass, it returns ``RandomOption`` subclasses.

        Parameters:
            source: INP for random number generator option.

        Returns:
            ``RandomOption`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM_SOURCE.
            MCNPSyntaxError: TOOLONG_DATUM_SOURCE.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_RAND),
        )

        # Processing Keyword
        keyword = RandomKeyword.from_mcnp(tokens.popl())

        # Processing Values
        match keyword:
            case RandomKeyword.GEN | RandomKeyword.SEED | RandomKeyword.STRIDE | RandomKeyword.HIST:
                value = types.McnpInteger.from_mcnp(tokens.popl())

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_RAND)

        match keyword:
            case RandomKeyword.GEN:
                obj = Gen(value)
            case RandomKeyword.SEED:
                obj = Seed(value)
            case RandomKeyword.STRIDE:
                obj = Stride(value)
            case RandomKeyword.HIST:
                obj = Hist(value)

        return obj

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``RandomOption`` objects.

        ``to_mcnp`` creates INP source string from ``RandomOption``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``RandomOption`` object.
        """

        return f'{self.keyword.to_mcnp()}={self.value.to_mcnp()}'


class Gen(RandomOption):
    """
    ``Gen`` represents INP Gen source definition data card
    options.

    ``Gen`` inherits attributes from ``RandomOption``. It
    represents the INP Gen source definition data card option syntax element.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        ``__init__`` initializes ``Gen``.

        Parameters:
            setting: Type of pseudorandom number generator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_RAND_VALUE.
        """

        if setting is None or setting not in {1, 2, 3, 4}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_RAND_VALUE)

        self.keyword = RandomKeyword.GEN
        self.value = setting
        self.setting = setting


class Seed(RandomOption):
    """
    ``Seed`` represents INP Seed source definition data card
    options.

    ``Seed`` inherits attributes from ``RandomOption``. It
    represents the INP Seed source definition data card option syntax
    element.

    Attributes:
        seed: Random number generator seed.
    """

    def __init__(self, seed: types.McnpInteger):
        """
        ``__init__`` initializes ``Seed``.

        Parameters:
            seed: Random number generator seed.

        Raises:
            MCNPSemanticError: INVALID_DATUM_RAND_VALUE.
        """

        if seed is None or (seed.value % 2 == 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_RAND_VALUE)

        self.keyword = RandomKeyword.SEED
        self.value = seed
        self.seed = seed


class Stride(RandomOption):
    """
    ``Stride`` represents INP Stride source definition data card
    options.

    ``Stride`` inherits attributes from ``RandomOption``. It
    represents the INP Stride source definition data card option syntax
    element.

    Attributes:
        stride: Number of random numbers between source particles.
    """

    def __init__(self, stride: types.McnpInteger):
        """
        ``__init__`` initializes ``Stride``.

        Parameters:
            stride: Number of random numbers between source particles.

        Raises:
            MCNPSemanticError: INVALID_DATUM_RAND_VALUE.
        """

        if stride is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_RAND_VALUE)

        self.keyword = RandomKeyword.STRIDE
        self.value = stride
        self.stride = stride


class Hist(RandomOption):
    """
    ``Hist`` represents INP Hist source definition data card
    options.

    ``Hist`` inherits attributes from ``RandomOption``. It
    represents the INP Hist source definition data card option syntax
    element.

    Attributes:
        number: History number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        ``__init__`` initializes ``Hist``.

        Parameters:
            number: History number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_RAND_VALUE.
        """

        if number is None or not (number >= 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_RAND_VALUE)

        self.keyword = RandomKeyword.HIST
        self.value = number
        self.number = number


class Random(Datum):
    """
    ``Random`` represents INP random number generator data
    cards.

    ``Random`` inherits attributes from ``Datum``. It represents
    the INP random number data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    def __init__(self, pairs: tuple[RandomOption]):
        """
        ``__init__`` initializes ``Random``.

        Parameters:
            pairs: Tuple of key-value pairs.
        """

        if pairs is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for pair in pairs:
            if pair is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'rand')
        self.mnemonic: Final[DatumMnemonic] = DatumMnemonic.RANDOM
        self.parameters: Final[tuple] = pairs

        self.pairs: Final[tuple[RandomOption]] = pairs
