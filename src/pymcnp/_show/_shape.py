import abc

import numpy


class Shape(metaclass=abc.ABCMeta):
    """
    Represents generic visualizations.

    Attributes:
        data: Underlying visualization.
    """

    def __init__(self, data):
        """
        Initializes ``Shape``.

        Parameters:
            data: Underlying visualization.

        Returns:
            ``Shape``
        """

        self.data = data

    @abc.abstractmethod
    def __add__(a, b):  # pragma: no cover
        """
        Adds ``Shape`` instances.

        Parameters:
            a: Addend #1.
            b: Addend #2.

        Returns:
            Merged ``Shape``.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __and__(a, b):  # pragma: no cover
        """
        Unites ``Shape``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``Shape`` union.
        """

        raise NotImplementedError

    # @abc.abstractmethod
    # def __or__(a, b):  # pragma: no cover
    # """
    # Intersects ``Shape``.

    # Parameters:
    # a: Operand #1.
    # b: Operand #2.

    # Returns:
    # ``Shape`` intersection.
    # """

    # raise NotImplementedError

    # @abc.abstractmethod
    # def __invert__(a):  # pragma: no cover
    # """
    # Inverts ``Shape``.

    # Parameters:
    # a: Operand #1.

    # Returns:
    # ``Shape`` complement.
    # """

    # raise NotImplementedError

    @abc.abstractmethod
    def rotate(self, axis: numpy.ndarray):  # pragma: no cover
        """
        Rotates ``Shape``.

        Parameters:


        Returns:
            ``Shape`` rotated.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def translate(self, vector: numpy.ndarray):  # pragma: no cover
        """
        Rotates ``Shape``.

        Parameters:
            vector: Translation to translate.

        Returns:
            ``Shape`` translated.
        """

        raise NotImplementedError
