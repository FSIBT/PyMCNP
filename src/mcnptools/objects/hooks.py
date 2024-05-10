"""Hooks to parse comments in surface entries.
"""


def detector_hook(self):
    """A custom feature used to identify detector surfaces.

    This hook will add a new property "is_detector" to surfaces that
    will be true if a surface comment includes the word "detector". It
    also will keep a list of all detector surfaces in the class.

    """
    self.is_detector: bool = False
    if self.comment:
        self.is_detector = "detector" in self.comment

    if self.is_detector:
        if "all_detectors" not in self.hook_data:
            self.data["all_detectors"] = []
        self.data["all_detectors"].append(self)


def detector_channel_hook(self):
    """A custom feature used to identify detector surfaces and give them an ID.

    This hook will add a new property "is_detector" to surfaces that
    will be true if a surface comment includes the word "detector". It
    also will keep a list of all detector surfaces in the class.

    The comment needs to have the form "detector <id>".
    Where `id` should bee an integer number.

    """
    self.is_detector: bool = False
    if self.comment:
        self.is_detector = "detector" in self.comment

    if self.is_detector:
        _, ch = self.comment.split()
        ch = int(ch)
        self.channel = ch
        if "all_detectors" not in self.hook_data:
            self.data["all_detectors"] = []
        self.data["all_detectors"].append(self)
