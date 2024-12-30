from dataclasses import dataclass

@dataclass
class Gas:
    R: float # Gas constant [J/(kg K)]
    k: float # Specific heat ratio (gamma) 
    c_p: float # Specific heat at constant pressure [J/(kg K)]
    c_v: float # Specific heat at constant volume [J/(kg K)]

    def __init__(self, R: float, k: float):
        self.R = R
        self.k = k

    @property
    def c_p(self):
        """"""
        return self.R / (1 - 1 / self.k)

    @property
    def c_v(self):
        """"""
        return self.R / (self.k - 1)
    

AIR = Gas(287, 1.4)

if __name__ == "__main__":
    assert AIR.R == 287
    assert AIR.k == 1.4
    assert round(AIR.c_p, 2) == 1004.50
    assert round(AIR.c_v, 2) == 717.50