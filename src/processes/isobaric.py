from ..step import Process
from ..point import Point
from ..utils import safe
import matplotlib.pyplot as plt


class Isobaric(Process):
    """
    Isobaric Process (p = constant)
    - Pressure remains constant throughout the process (p_A = p_B).
    - Work: W = p * ΔV
    - Heat: Q = ΔU + W
    - Represented on a P-V diagram as a horizontal line.
    """

    def __init__(self, A: Point, B: Point, R=287, gamma=1.4):
        super().__init__(A, B, R, gamma)

        # The pressure must remain constant (p_A = p_B)
        if A.p and B.p:
            assert A.p == B.p, "Pressure is not constant, something is wrong with the data."

        # Assign consistent pressure values if one is missing
        A.p = A.p or B.p
        B.p = B.p or A.p

    def compute(self):
        """
        Compute the missing thermodynamic properties based on the ideal gas law
        and relationships for an isobaric process.
        """
        A, B, R = self.A, self.B, self.R

        # Ensure pressure is constant
        A.p = A.p or B.p
        B.p = B.p or A.p

        # Update the points with current state
        A.update(R)
        B.update(R)

        # Compute missing properties using the ideal gas law
        A.T = A.T or safe(lambda: B.T * (A.v / B.v))
        B.T = B.T or safe(lambda: A.T * (B.v / A.v))
        A.v = A.v or safe(lambda: B.v * (A.T / B.T))
        B.v = B.v or safe(lambda: A.v * (B.T / A.T))

    def work(self) -> float:
        """
        Calculate the work done during the isobaric process.
        W = p * ΔV
        """
        return 0
    
    def heat(self) -> float:
        """
        Calculate the heat transferred during the isobaric process.
        Q = ΔU + W
        ΔU = n * C_v * ΔT (internal energy change)
        W = p * ΔV
        """
        return 0

    def plot(self, ax_pv: plt.Axes, ax_ts: plt.Axes):
        """"""
        A, B = self.A, self.B

        # Plot the process on the P-V diagram
        ax_pv.plot([A.v, B.v], [A.p, B.p], label="Isobaric", color="red")

        # Plot the process on the T-S diagram
        ax_ts.plot([A.s, B.s], [A.T, B.T], label="Isobaric", color="red")
        

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

    # Try to plot
    import matplotlib.pyplot as plt
    fig, (ax_pv, ax_ts) = plt.subplots(1, 2)
    ax_pv.set_title("P-V Diagram")
    ax_ts.set_title("T-S Diagram")
    isobaric.plot(ax_pv, ax_ts)
    plt.show()