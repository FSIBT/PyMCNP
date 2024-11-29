"""
Contains classes representing INP cell card options.
"""

from . import _card


class CellOption(_card.CardOption):
    """
    Represents INP cell card option keywords.

    ``CellOption`` implements ``_card.CardOption``.

    Attributes:
        keyword: Cell card option keyword.
        value: Cell card option value.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CellOption`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CellOption``.
        """

        # Processing Suffix
        suffix_str = str(self.suffix.to_mcnp()) if hasattr(self, 'suffix') else ''

        # Processing Designator
        designator_str = (
            f":{','.join(self.designator.particles)}"
            if hasattr(self, 'designator') and self.designator is not None
            else ''
        )

        value_str = ''
        if isinstance(self.value, tuple):
            value_str = ' '.join(
                [
                    str(param.value) if hasattr(param, 'value') else str(param)
                    for param in self.value
                ]
            )
        else:
            value_str = self.value.value if hasattr(self.value, 'value') else str(self.value)

        return f'{self.keyword.to_mcnp()}{suffix_str}{designator_str}={value_str}'
