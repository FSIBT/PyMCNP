class Test:
    def __init__(self, potato):
        self._potato = potato

    @property
    def potato(self):
        return self._potato

    @potato.setter
    def potato(self, potato):
        if potato != 'a':
            raise ValueError
        self._potato = potato


t = Test('a')
t.potato = 'b'
