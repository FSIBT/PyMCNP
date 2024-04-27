from dataclasses import dataclass


@dataclass
class InputLine:
    """A single input line from an MCNP input file.

    These are used during the parsing of an input file.
    They represent a single line, such as 'sdef' for a source.
    We already unify some formatting before creating an InputLine instance:
    - multi lines are collapses into a single line (which can have arbitrary length)
    - whitespaces around equal signes are removed
    - split between text and comments
    """

    text: str
    comment: str = ""
