from ..step import Step
from ..point import Point


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
        if A.T:
            A.v = A.v or R * A.T / A.p

        if A.v:
            A.T = A.T or A.p * A.v / R

        if B.T:
            B.v = B.v or R * B.T / B.p
        
        if B.v:
            B.T = B.T or B.p * B.v / R

        # If we don't have the pressure, we can compute it using the ideal gas law
        if not A.T and all(A.v, B.v, B.T):
            A.T = B.T * (A.v / B.v)

        if not B.T and all(A.v, B.v, A.T):
            B.T = A.T * (B.v / A.v)

        if not A.v and all(A.T, B.T, B.v):
            A.v = B.v * (A.T / B.T)

        if not B.v and all(A.T, B.T, A.v):
            B.v = A.v * (B.T / A.T)

        



if __name__ == "__main__":
    # Exercise 3
    p1 = Point("P1", T=298, p=1)
    p2 = Point("P2", p=50)
    p3 = Point("P3", T=1600)
    p4 = Point("P4")

    print(p1)
    print(p2)
    print(p3)
    print(p4)

    isentropic = Isentropic(p1, p2)
    isentropic.compute()

    isobaric = Isobaric(p2, p3)
    isobaric.compute()

    isentropic = Isentropic(p3, p4)
    isentropic.compute()

    isochoric = Isochoric(p4, p1)
    isochoric.compute()

    print("Second Loop")

    isentropic = Isentropic(p1, p2)
    isentropic.compute()

    isobaric = Isobaric(p2, p3)
    isobaric.compute()

    isentropic = Isentropic(p3, p4)
    isentropic.compute()

    isochoric = Isochoric(p4, p1)
    isochoric.compute()

    print("Third Loop")

    isentropic = Isentropic(p1, p2)
    isentropic.compute()

    isobaric = Isobaric(p2, p3)
    isobaric.compute()

    isentropic = Isentropic(p3, p4)
    isentropic.compute()

    isochoric = Isochoric(p4, p1)
    isochoric.compute()

    print(p1)
    print(p2)
    print(p3)
    print(p4)