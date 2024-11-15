from enum import Enum

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class ActivationControlKeyword(str, Enum):
    """
    ``ActivationControlKeyword`` represents INP activation control data
    card keywords.

    ``ActivationControlKeyword`` implements INP activation control data
    card keywords as a Python inner class. It enumerates MCNP keywords
    and provides methods for casting strings to
    ``ActivationControlKeyword`` instances. It represents the INP
    activation control data card keyword syntax element, so
    ``ActivationControl`` and ``ActivationControlOption`` depend on
    ``ActivationControlKeyword`` as an enum.
    """

    FISSION = 'fission'
    NON_FISSION = 'nonfiss'
    DELAYED_NEUTRON = 'dn'
    DELAYED_GAMMA = 'dg'
    THRESH = 'thresh'
    DNBAIS = 'dnbais'
    NAP = 'nap'
    DNEB = 'dneb'
    DGEB = 'degb'
    PECUT = 'pecut'
    HLCUT = 'hlcut'
    SAMPLE = 'sample'

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``ActivationControlKeyword`` objects
        from INP.

        ``from_mcnp`` constructs instances of
        ``ActivationControlKeyword`` from INP source strings, so it
        operates as a class constructor method and INP parser helper function.

        Parameters:
            source: INP for activation control option keyword.

        Returns:
            ``ActivationControlKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in ActivationControlKeyword]:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_KEYWORD
            )

        return ActivationControlKeyword(source)


class ActivationControlOption:
    """
    ``ActivationControlOption`` represents INP activation control data card
    options.

    ``ActivationControlOption`` implements INP activation control data card
    options. Its attributes store keywords and values, and its methods
    provide entry and endpoints for working with INP activation control
    data card options. It represents the generic INP activation control
    data card option syntax element, so ``ActivationControl`` depends on
    ``ActivationControlOption`` as a generic data structure and superclass.

    Attributes:
        keyword: Activation control data card option keyword.
        value: Activation control data card option value.
    """

    def __init__(self):
        """Needs to be implemented in subclass."""

        raise NotImplementedError

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``ActivationControlOption`` objects from
        INP.

        ``from_mcnp`` constructs instances of ``ActivationControlOption``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function. Although defined on the
        superclass, it returns ``ActivationControlOption`` subclasses.

        Parameters:
            source: INP for activation option.

        Returns:
            ``ActivationControlOption`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM_ACTIVATION.
            MCNPSyntaxError: TOOLONG_DATUM_ACTIVATION.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split('='),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_ACTIVATION),
        )

        # Processing Keyword
        keyword = ActivationControlKeyword.from_mcnp(tokens.popl())

        # Processing Values
        match keyword:
            case (
                ActivationControlKeyword.FISSION
                | ActivationControlKeyword.NON_FISSION
                | ActivationControlKeyword.DELAYED_NEUTRON
                | ActivationControlKeyword.DELAYED_GAMMA
                | ActivationControlKeyword.SAMPLE
            ):
                value = tokens.popl()

            case ActivationControlKeyword.THRESH | ActivationControlKeyword.PECUT:
                value = types.McnpReal.from_mcnp(tokens.popl())

            case (
                ActivationControlKeyword.DNABIS
                | ActivationControlKeyword.NAP
                | ActivationControlKeyword.HLCUT
            ):
                value = types.McnpInteger.from_mcnp(tokens.popl())

            case ActivationControlKeyword.DNEB | ActivationControlKeyword.DGEB:
                assert False, 'Unimplemented'

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_ACTIVATION)

        # create correct subclass
        if keyword is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_KEYWORD
            )

        match keyword:
            case ActivationControlKeyword.FISSION:
                obj = Fission(value)
            case ActivationControlKeyword.NON_FISSION:
                obj = NonFission(value)
            case ActivationControlKeyword.DELAYED_NEUTRON:
                obj = DelayedNeutron(value)
            case ActivationControlKeyword.DELAYED_GAMMA:
                obj = DelayedGamma(value)
            case ActivationControlKeyword.THRESH:
                obj = Thresh(value)
            case ActivationControlKeyword.DNBAIS:
                obj = Dnbais(value)
            case ActivationControlKeyword.NAP:
                obj = Nap(value)
            case ActivationControlKeyword.PECUT:
                obj = Pecut(value)
            case ActivationControlKeyword.HLCUT:
                obj = Hlcut(value)
            case ActivationControlKeyword.SAMPLE:
                obj = Sample(value)
            case ActivationControlKeyword.DNEB:
                assert False, 'Unimplemented'
            case ActivationControlKeyword.DGEB:
                assert False, 'Unimplemented'

        return obj

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``ActivationOption`` objects.

        ``to_mcnp`` creates INP source string from ``ActivationOption``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``ActivationOption`` object.
        """

        return f'{self.keyword.to_mcnp()}={self.value.to_mcnp()}'


class Fission(ActivationControlOption):
    """
    ``Fission`` represents INP Fission activation control data card
    options.

    ``Fission`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Fission activation control data card option syntax element.

    Attributes:
        particle: Type of delayed particles to be produced.
    """

    def __init__(self, particle: str):
        """
        ``__init__`` initializes ``Fission``.

        Parameters:
            particle: Delayed particle(s) to be produced.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if particle is None or particle not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.FISSION
        self.value = particle
        self.particle = particle


class NonFission(ActivationControlOption):
    """
    ``NonFission`` represents INP NonFission activation control data card
    options.

    ``NonFission`` inherits attributes from ``ActivationControlOption``. It
    represents the INP NonFission activation control data card option syntax element.

    Attributes:
        particle: Type of delayed particles to be produced.
    """

    def __init__(self, particle: str):
        """
        ``__init__`` initializes ``NonFission``.

        Parameters:
            particle: Type of delayed particles to be produced.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if particle is None or particle not in {'none', 'n,p,e,f,a', 'all'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.NON_FISSION
        self.value = particle
        self.particle = particle


class DelayedNeutron(ActivationControlOption):
    """
    ``DelayedNeutron`` represents INP DelayedNeutron activation control
    data card options.

    ``DelayedNeutron`` inherits attributes from
    ``ActivationControlOption``. It represents the INP DelayedNeutron
    activation control data card option syntax element.

    Attributes:
        source: Delayed neutron data source.
    """

    def __init__(self, source: str):
        """
        ``__init__`` initializes ``DelayedNeutron``.

        Parameters:
            source: Delayed neutron data source.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if source is None or source not in {'model', 'library', 'both', 'prompt'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.DELAYED_NEUTRON
        self.value = source
        self.source = source


class DelayedGamma(ActivationControlOption):
    """
    ``DelayedGamma`` represents INP DelayedGamma activation control data
    card options.

    ``DelayedGamma`` inherits attributes from ``ActivationControlOption``.
    It represents the INP DelayedGamma activation control data card option syntax
    element.

    Attributes:
        source: Delayed gamma data source.
    """

    def __init__(self, source: str):
        """
        ``__init__`` initializes ``DelayedGamma``.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if source is None or source not in {'lines', 'mg', 'none'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.DELAYED_GAMMA
        self.value = source
        self.source = source


class Thresh(ActivationControlOption):
    """
    ``Thresh`` represents INP Thresh activation control data card options.

    ``Thresh`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Thresh activation control data card option syntax element.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma.
    """

    def __init__(self, fraction: types.McnpReal):
        """
        ``__init__`` initializes ``Thresh``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if fraction is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.THRESH
        self.value = fraction
        self.fraction = fraction


class Dnbais(ActivationControlOption):
    """
    ``Dnbais`` represents INP Dnbais activation control data card options.

    ``Dnbais`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Dnbais activation control data card option syntax element.

    Attributes:
        count: Maximum number of delayed neutron per interaction.
    """

    def __init__(self, count: types.McnpInteger):
        """
        ``__init__`` initializes ``Dnbais``.

        Parameters:
            count: Maximum number of delayed neutron per interaction.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if count is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.DNBAIS
        self.value = count
        self.count = count


class Nap(ActivationControlOption):
    """
    ``Nap`` represents INP Nap activation control data card options.

    ``Nap`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Nap activation control data card option syntax element.

    Attributes:
        count: Number of acitvation product for distributions.
    """

    def __init__(self, count: types.McnpInteger):
        """
        ``__init__`` initializes ``Nap``.

        Parameters:
            count: Number of acitvation product for distributions.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if count is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.NAP
        self.value = count
        self.count = count


class Pecut(ActivationControlOption):
    """
    ``Pecut`` represents INP Pecut activation control data card options.

    ``Pecut`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Pecut activation control data card option syntax element.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    def __init__(self, cutoff: types.McnpReal):
        """
        ``__init__`` initializes ``Pecut``.

        Parameters:
            cutoff: Delayed-gamma energy cutoff.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if cutoff is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.PECUT
        self.value = cutoff
        self.cutoff = cutoff


class Hlcut(ActivationControlOption):
    """
    ``Hlcut`` represents INP Hlcut activation control data card options.

    ``Hlcut`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Hlcut activation control data card option syntax element.

    Attributes:
        threshold: Spontaneous-decay half-life threshold.
    """

    def __init__(self, threshold: types.McnpInteger):
        """
        ``__init__`` initializes ``Hlcut``.

        Parameters:
            threshold: Spontaneous-decay half-life threshold.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if threshold is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.HLCUT
        self.value = threshold
        self.threshold = threshold


class Sample(ActivationControlOption):
    """
    ``Sample`` represents INP Sample activation control data card options.

    ``Sample`` inherits attributes from ``ActivationControlOption``. It
    represents the INP Sample activation control data card option syntax element.

    Attributes:
        state: Flag for correlated or uncorrelated.
    """

    def __init__(self, state: str):
        """
        ``__init__`` initializes ``Sample``.

        Parameters:
            state: Flag for correlated or uncorrelated.

        Raises:
            MCNPSemanticError: INVALID_DATUM_ACTIVATION_VALUE.
        """

        if state is None or state not in {'correlate', 'nonfiss_cor'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_ACTIVATION_VALUE)

        self.keyword = ActivationControlKeyword.SAMPLE
        self.value = state
        self.state = state


class ActivationControl(Datum):
    """
    ``ActivationControl`` represents INP activation control data cards.

    ``ActivationControl`` inherits attributes from ``Datum``. It represents the
    INP activation control data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    def __init__(self, pairs: tuple[ActivationControlOption]):
        """
        ``__init__`` initializes ``ActivationControl``.

        Parameters:
            pairs: Tuple of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None or not pairs:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for pair in pairs:
            if pair is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'act')
        self.mnemonic = DatumMnemonic.ACTIVATION_CONTROL
        self.parameters = pairs

        self.paris = pairs
