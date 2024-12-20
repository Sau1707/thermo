from ..step import Step
from ..point import Point
from ..utils import safe


class Isobaric(Step):
    """
    p = constant
    """
    def __init__(self, start, end):
        super().__init__(start, end)
        A, B = self.start, self.end

        # The pressure is constant (P_A = P_B)
        if A.p and B.p:
            assert A.p == B.p, "Pressure is not constant, something is wrong with the data"

        # Assign the values
        A.p = A.p or B.p
        B.p = B.p or A.p

    def compute(self, R=287):
        A, B = self.start, self.end

        # The pressure is constant
        A.p = A.p or B.p
        B.p = B.p or A.p

        # Using the ideal gas law (p * v = R * T)
        A.v = A.v or safe(lambda: R * A.T / A.p)
        A.T = A.T or safe(lambda: A.p * A.v / R)
        A.p = A.p or safe(lambda: R * A.T / A.v)
        B.v = B.v or safe(lambda: R * B.T / B.p)
        B.T = B.T or safe(lambda: B.p * B.v / R)
        B.p = B.p or safe(lambda: R * B.T / B.v)

        # If we don't have the pressure, we can compute it using the ideal gas law
        A.T = A.T or safe(lambda: B.T * (A.v / B.v))
        B.T = B.T or safe(lambda: A.T * (B.v / A.v))
        A.v = A.v or safe(lambda: B.v * (A.T / B.T))
        B.v = B.v or safe(lambda: A.v * (B.T / A.T))
        

if __name__ == "__main__":
    # Exercise 3
    # Point('P1', T=911.25, p=50.00, v=5230.56)
    # Point('P2', T=1600.00, p=50.00, v=9184.00)
    # TODO: Flipped p1 and p2

    p1 = Point("P1", T=911.25, p=50)
    p2 = Point("P2", T=1600)
    isobaric = Isobaric(p1, p2)
    isobaric.compute()
    print(p1)
    print(p2)

    p1 = Point("P1", T=911.25)
    p2 = Point("P2", T=1600, p=50)
    isobaric = Isobaric(p1, p2)
    isobaric.compute()
    print(p1)
    print(p2)

    p1 = Point("P1", p=50, v=5230.57)
    p2 = Point("P2", v=9184.00)
    isobaric = Isobaric(p1, p2)
    isobaric.compute()
    print(p1)
    print(p2)

    p1 = Point("P1", v=5230.56)
    p2 = Point("P2", p=50, v=9184.00)
    isobaric = Isobaric(p1, p2)
    isobaric.compute()
    print(p1)
    print(p2)

    p1 = Point("P1", v=5230.57)
    p2 = Point("P2", p=50, T=1600.00)
    isobaric = Isobaric(p1, p2)
    isobaric.compute()
    print(p1)
    print(p2)

    p1 = Point("P1", T=911.25, p=50.00)
    p2 = Point("P2", v=9184.00)
    isobaric = Isobaric(p1, p2)
    isobaric.compute()
    print(p1)
    print(p2)