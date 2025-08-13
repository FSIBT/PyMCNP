from . import _doer
from . import meshtal
from .Meshtal import Meshtal


class MeshtalProcessor(_doer.Doer):
    """
    Processes `Meshtal`.
    """

    def prehook(self):
        """
        Runs before processing.
        """

        pass

    def posthook(self):
        """
        Runs after processing.
        """

        pass

    def process(self, tally: meshtal.Tally):
        """
        Processes tallies.

        Parameter:
            tally: Tally to process.
        """

        pass

    def __call__(self, file: Meshtal):
        """
        Processes `Meshtal`.

        Parameter:
            file: File to process.
        """

        self.prehook()

        for tally in file.tallies:
            self.process(tally)

        self.posthook()
