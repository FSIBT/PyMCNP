from ..utils import _object


class InpEntry_(_object.McnpElement_):
    """
    Represents generic INP card entries.

    Attributes:
        Parameters: INP card entry entries.
    """

    def to_mcnp(self):
        """
        Generates INP from ``InpEntry_``.

        Returns:
            INP entry.
        """

        return ' '.join(str(parameter) for parameter in self.parameters)
