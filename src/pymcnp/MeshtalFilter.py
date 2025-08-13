from . import _doer
from . import meshtal
from .Meshtal import Meshtal


class MeshtalFilter(_doer.Doer):
    """
    Filters `Meshtal`.
    """

    def check(self, tally: meshtal.Tally) -> bool:
        """
        Runs when `run` filters MESHTAL source tallies.

        Parameters:
            tally: Tally to check.

        Returns:
            True/False if the given tally should/shouldn't be kept.
        """

        return True

    def __call__(self, file: Meshtal):
        """
        Filters given `Meshtal`.

        Parameters:
            file: File to filter.

        Yields:
            Accepted tallies.
        """

        def tallies():
            for tally in file.tallies:
                if self.check(tally):
                    yield tally
                else:
                    continue

        return tallies()
