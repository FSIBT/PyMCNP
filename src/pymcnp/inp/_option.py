from ..utils import _object


class InpOption_(_object.McnpRegistry_):
    """
    Represents generic INP options.

    Attributes:
        keyword: INP option keyword.
        value: INP option value.
    """

    def to_mcnp(self):
        """
        Generates INP from ``InpOption_``.

        Returns:
            INP option.
        """

        return f'{self._KEYWORD}{self.suffix if hasattr(self, 'suffix') else ""}{f":{self.designator}" if hasattr(self, 'designator') else ""} {self.value}'
