import abc

import numpy


class Shape(metaclass=abc.ABCMeta):
    """
    Represents generic visualizations.

    Attributes:
        surface: Underlying surface visualization.
        cell: Underlying cell visualization.
    """

    def __init__(self, surface, cell):
        """
        Initializes `Shape`.

        Parameters:
            surface: Underlying surface visualization.
            cell: Underlying cell visualization.

        Returns:
            `Shape`
        """

        self.surface = surface
        self.cell = cell

    @abc.abstractmethod
    def __add__(a, b):
        """
        Adds `Shape` instances.

        Parameters:
            a: Addend #1.
            b: Addend #2.

        Returns:
            Merged `Shape`.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __and__(a, b):
        """
        Unites `Shape`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Shape` union.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __or__(a, b):
        """
        Intersects `Shape`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
        `Shape` intersection.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def __invert__(a):
        """
        Complements `Shape`.

        Parameters:
            a: Operand #1.

        Returns:
        `Shape` complement.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def rotate(self, axis: numpy.ndarray, angle: float, center: tuple[float, float, float]):
        """
        Rotates `Shape`.

        Parameters:


        Returns:
            `Shape` rotated.
        """

        raise NotImplementedError

    @abc.abstractmethod
    def translate(self, vector: numpy.ndarray):
        """
        Rotates `Shape`.

        Parameters:
            vector: Translation to translate.

        Returns:
            `Shape` translated.
        """

        raise NotImplementedError
