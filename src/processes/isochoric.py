from ..step import Step
from ..point import Point
from ..utils import safe


class Isochoric(Step):
    """
    Volume remains constant throughout the process: 
    No work is done by the system or on the system, as work depends on volume change:
    """

    def __init__(self, start, end):
        super().__init__(start, end)
        A, B = self.start, self.end

        # The volume is constant (V_A = V_B)
        if A.v and B.v:
            assert A.v == B.v, "Volume is not constant, something is wrong with the data"

        # Assign the values
        A.v = A.v or B.v
        B.v = B.v or A.v

    def compute(self, R=287, gamma=1.4):
        A, B = self.start, self.end

        A.v = A.v or B.v
        B.v = B.v or A.v

        # Using the ideal gas law (p * v = R * T)
        A.v = A.v or safe(lambda: R * A.T / A.p)
        A.T = A.T or safe(lambda: A.p * A.v / R)
        A.p = A.p or safe(lambda: R * A.T / A.v)
        B.v = B.v or safe(lambda: R * B.T / B.p)
        B.T = B.T or safe(lambda: B.p * B.v / R)
        B.p = B.p or safe(lambda: R * B.T / B.v)

        # If we don't have the volume, we can compute it using the ideal gas law
        A.T = A.T or safe(lambda: B.T * (A.p / B.p))
        B.T = B.T or safe(lambda: A.T * (B.p / A.p))
        A.p = A.p or safe(lambda: B.p * (A.T / B.T))
        B.p = B.p or safe(lambda: A.p * (B.T / A.T))

    def work(self, R=287, gamma=1.4) -> float:
        """
        """
        return 0