from . import meshtal
from .Meshtal import Meshtal


class MeshtalFiltered:
    """
    Filters MESHTAL files.

    Attributes:
        meshtal: ``Meshtal`` to filter.
    """

    def __init__(self, meshtal: Meshtal):
        """
        Initializes ``MeshtalFiltered``.

        Parameters:
            meshtal: ``Meshtal`` to filter.
        """

        self.meshtal: Meshtal = meshtal

    @staticmethod
    def check(tally: meshtal.Tally) -> bool:
        """
        Runs when ``run`` filters MESHTAL source tallies.

        Returns:
            True/False if the given tally should/shouldn't be kept.
        """

        raise NotImplementedError

    def run(self):
        """
        Filters MESHTAL.
        """

        def histories():
            for tally in self.meshtal.tallies:
                if self.check(tally):
                    yield tally
                else:
                    continue

        return histories
