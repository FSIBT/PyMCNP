import pymcnp


class Test_Surface:
    s1 = pymcnp.inp.Px(1, number=1)
    s2 = pymcnp.inp.Px(2, number=2)
    s3 = pymcnp.inp.Px(3, number=3)

    def test_operators(self):
        """
        Tests that operators build MCNP geometry (space is intersection, colon is union).
        """

        assert (self.s1 & ~self.s2 & self.s3).to_mcnp() == '1 -2 3'
        assert (self.s1 | self.s2).to_mcnp() == '1:2'
        assert ((self.s1 | self.s2) & self.s3).to_mcnp() == '(1:2) 3'
        assert (-self.s1 & +self.s2).to_mcnp() == '-1 +2'
        assert (~(self.s1 & self.s2)).to_mcnp() == '#(1 2)'
