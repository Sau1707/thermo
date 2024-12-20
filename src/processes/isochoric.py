from ..step import Step
from ..point import Point


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

    def compute(self, R=287):
        A, B = self.start, self.end

        A.v = A.v or B.v
        B.v = B.v or A.v