import pytest
import hypothesis as hy
import hypothesis.strategies as st


@st.composite
def mcnp_integer(draw, thing=lambda _: True):
    return draw(st.integers().filter(thing))


@st.composite
def mcnp_real(draw, thing=lambda _: True):
    return draw(st.floats(allow_nan=False, allow_infinity=False).filter(thing))


@st.composite
def mcnp_designator(draw, valid: bool):
    if valid:
        return draw(
            st.sampled_from(
                [
                    "n",
                    "p",
                    "e",
                    "|",
                    "q",
                    "y",
                    "v",
                    "f",
                    "h",
                    "l",
                    "+",
                    "-",
                    "x",
                    "y",
                    "o",
                    "!",
                    "<",
                    ">",
                    "g",
                    "/",
                    "z",
                    "k",
                    "%",
                    "^",
                    "b",
                    "_",
                    "~",
                    "c",
                    "w",
                    "@",
                    "d",
                    "t",
                    "s",
                    "a",
                    "*",
                    "?",
                    "#",
                ]
            )
        )
    else:
        return None
