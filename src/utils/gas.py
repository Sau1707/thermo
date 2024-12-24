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
        self.c_p = k * R / (k - 1)
        self.c_v = R / (k - 1)