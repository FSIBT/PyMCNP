from . import abc
from . import ptrac
from .Ptrac import Ptrac


class PtracFilter(abc.Utility):
    """
    Filters PTRAC files.
    """

    def check_source(self, event: ptrac.block.Event) -> bool:
        """
        Checks source events.

        Parameters:
            event: Source event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_bank(self, event: ptrac.block.Event) -> bool:
        """
        Checks bank events.

        Parameters:
            event: Bank event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_surface(self, event: ptrac.block.Event) -> bool:
        """
        Checks surface events.

        Parameters:
            event: Surface event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_collision(self, event: ptrac.block.Event) -> bool:
        """
        Checks collision events.

        Parameters:
            event: Collision event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_terminal(self, event: ptrac.block.Event) -> bool:
        """
        Checks terminal events.

        Parameters:
            event: Terminal event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def run(self, file: Ptrac):
        """
        Filters ptrac files.

        Parameters:
            file: Ptrac file to check.

        Yields:
            Accepted events.
        """

        for history in file.histories:
            kind = history.i.event_type
            for event in history.events:
                match kind.strip():
                    case '1000':
                        check = self.check_source
                    case '3000':
                        check = self.check_surface
                    case '4000':
                        check = self.check_collision
                    case '5000':
                        check = self.check_terminal
                    case _:
                        check = self.check_bank

                kind = event.j.type

                if check(event):
                    yield event
                else:
                    continue
