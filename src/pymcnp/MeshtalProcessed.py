from . import meshtal
from .Meshtal import Meshtal


class MeshtalProcessed:
    """
    Processes MESHTAL.

    Attributes:
        meshtal: ``Meshtal`` to process.
    """

    def __init__(self, meshtal: Meshtal):
        """
        Initializes ``MeshtalProcessed``.

        Parameters:
            meshtal: ``Meshtal`` to process.
        """

        self.meshtal: Meshtal = meshtal

    def prehook(self):
        """
        Runs before ``run``.
        """

        pass

    def posthook(self):
        """
        Runs after ``run``.
        """

        pass

    def process(self, tally: meshtal.Tally):
        """
        Runs when ``run`` processes MESHTAL tallies.
        """

        raise NotImplementedError

    def run(self):
        """
        Processes MESHTAL.
        """

        self.prehook()

        for tally in self.meshtal.tallies:
            self.process(tally)

        self.posthook()
