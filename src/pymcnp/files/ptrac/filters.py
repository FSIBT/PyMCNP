from . import event


class Filters:
    @staticmethod
    def filter_source(evnt: event.Event) -> bool:
        return True

    @staticmethod
    def filter_bank(evnt: event.Event) -> bool:
        return True

    @staticmethod
    def filter_surface(evnt: event.Event) -> bool:
        return True

    @staticmethod
    def filter_collision(evnt: event.Event) -> bool:
        return True

    @staticmethod
    def filter_terminal(evnt: event.Event) -> bool:
        return True

    @staticmethod
    def filter_flag(evnt: event.Event) -> bool:
        return True
