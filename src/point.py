############### 
class Point:
    """
        A single point in a thermodynamic process

        Each Step in the process have:
        T (Temperature)
        P (Pressure)
        h (Enthalpy)
        s (Entropy)
        V (Volume)
    """

    def __init__(self, name: str):
        self.name = name

        self.T = None
        self.P = None
        self.h = None
        self.s = None
        self.V = None

    
