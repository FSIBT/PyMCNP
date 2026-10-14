import pandas


class Dataframe:
    """
    Mixin generating `pandas.DataFrame` from OUTP tally blocks with `subtallies`.
    """

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from the tally.

        Returns:
            `pandas.DataFrame`.
        """

        df = pandas.concat((subtally.to_dataframe() for subtally in self.subtallies), ignore_index=True)
        df['number'] = self.number.value.strip()
        df['type'] = self.tally_type.value.strip()
        df['particles'] = self.particles.value.strip()
        df['nps'] = self.nps.value.strip()

        return df
