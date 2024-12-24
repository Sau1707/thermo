from ..step import Process
from ..point import Point
from ..utils import safe


class Isothermal(Process):
    """
    - Constant Temperature Process (ΔT = 0)
    - Work Done (W = n * R * T * ln(V2/V1))
    - Heat Added Equals Work Done (Q = W, ΔU = 0)
    - Pressure-Volume Relationship (P1 * V1 = P2 * V2)
    - Represented on the P-V diagram as a hyperbolic curve.
    """

    def __init__(self, A: Point, B: Point, R=287, gamma=1.4):
        super().__init__(A, B, R, gamma)

        # The temperature must be constant
        if self.A.T and self.B.T:
            assert A.T == B.T, "Temperature is not constant, something is wrong with the data"

    def compute(self):
        A, B, R = self.A, self.B, self.R

        # Ensure temperature is constant
        A.T = A.T or B.T
        B.T = B.T or A.T

        # Update the points
        A.update(R)
        B.update(R)

        # If we don't have a property, calculate it using the ideal gas law and isothermal relationships
        A.p = A.p or safe(lambda: B.p * (B.v / A.v))
        B.p = B.p or safe(lambda: A.p * (A.v / B.v))
        A.v = A.v or safe(lambda: B.p * B.v / A.p)
        B.v = B.v or safe(lambda: A.p * A.v / B.p)

    def work(self) -> float:
        """
        Calculate the work done during the isothermal process.
        W = n * R * T * ln(V2/V1)
        """
        return 0
    
    def heat(self) -> float:
        """
        Calculate the heat transfer during the isothermal process.
        For isothermal processes, Q = W (ΔU = 0).
        """
        return 0
