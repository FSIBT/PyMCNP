import pymcnp
from ..... import classes


class Test_M(classes.Test_Nonterminal):
    element = pymcnp.inp.card.data.M
    EXAMPLES_VALID = [
        'm100 013027 -0.1701 020040 -0.131742819 020042 -0.000879273 020044 &\n      -0.002834874 026054 -0.00086506 026056 -0.013579592 026057 -0.000313612 &\n      008016 -0.45489192 019039 -0.0001865162 019041 -0.0000134604 012024 &\n      -0.00402849 012025 -0.00051 012026 -0.00056151 011023 -0.0045 014028 &\n      -0.190532718 014029 -0.00967921 014030 -0.006388072 090232 -0.006 022046 &\n      -0.000066 022047 -0.00005952 022048 -0.00058976 022049 -0.00004328 022050 &\n      -0.00004144',
    ]

    def test_form_formula(self) -> None:
        pymcnp.inp.card.data.M.from_formula(suffix='1', formulas={'H2O': 1}, is_weight=True)
        pymcnp.inp.card.data.M.from_formula(suffix='1', formulas={'H2O': 1}, is_weight=False)
