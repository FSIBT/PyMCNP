from dataclasses import dataclass


@dataclass
class InputLine:
    text: str
    comment: str = ""
