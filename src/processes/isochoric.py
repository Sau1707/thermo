from ..step import Process
from ..point import Point
from ..utils import safe


class Isochoric(Process):
    """
    - Constant Volume Process (ΔV = 0) 
    - No Work Done (W = 0)
    - Change in Internal Energy (ΔU = Q)
    - Pressure-Temperature Relationship (P1/T1 = P2/T2)
    - Heat Capacity (Q = n * c_v * ΔT)
    - Represented on the P-V diagram as a vertical line.    
    """

    def __init__(self, A: Point, B: Point, R=287, gamma=1.4):
        super().__init__(A, B, R, gamma)

        # The volume must be constant
        if self.A.v and B.v:
            assert A.v == B.v, "Volume is not constant, something is wrong with the data"

    def compute(self):
        A, B, R = self.A, self.B, self.R

        # The volume must be constant
        A.v = A.v or B.v
        B.v = B.v or A.v

        # Update the points
        A.update(R)
        B.update(R)

        # If we don't have the volume, we can compute it using the ideal gas law
        A.T = A.T or safe(lambda: B.T * (A.p / B.p))
        B.T = B.T or safe(lambda: A.T * (B.p / A.p))
        A.p = A.p or safe(lambda: B.p * (A.T / B.T))
        B.p = B.p or safe(lambda: A.p * (B.T / A.T))

    def work(self) -> float:
        """TODO"""
        return 0
    
    def heat(self) -> float:
        """TODO"""
        return 0