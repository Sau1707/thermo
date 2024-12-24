from ..step import Process
from ..point import Point
from ..utils import safe

# This process can have an efficiency - 4s or 4
class Isentropic(Process):
    """
    https://www.grc.nasa.gov/www/k-12/airplane/compexp.html

    c_p = specific heat at constant pressure
    c_v = specific heat at constant volume
    R = gas constant
    T = temperature
    p = pressure
    s = entropy
    v = specific volume

    c_p - c_v = R
    c_p / c_v = gamma

    Equation of State:
    p * v = R * T
    
    Entropy of a Gas:
    s2 - s1 = c_p * ln(T2 / T1) - R * ln(p2 / p1)

    Compression and expansion are reversible (s2 = s1):
    c_p * ln(T2 / T1) = R * ln(p2 / p1) 

    => Effect of Pressure on Temperature:
    T2 / T1 = (p2 / p1) ^ (1 - 1 / gamma)

    => Effect of Volume on Temperature:
    T2 / T1 = (v1 / v2) ^ (gamma)

    Definition: Entropy (s) remains constant (s1 = s2)
    T-s Diagram: The process appears as a vertical line downward
    - Idealized expansion with no heat transfer or irreversibilities
    - Work output is maximized in a turbine.
    """
    def __init__(self, start, end):
        super().__init__(start, end)
        A, B = self.start, self.end

        # The entropy is constant -> s2 = s1
        if A.s and B.s:
            assert A.s == B.s, "Entropy is not constant, something is wrong with the data"

        # Assign the values
        A.s = A.s or B.s
        B.s = B.s or A.s

    def compression_ratio(self, gamma=1.4) -> float | None:
        """
        The compression ratio (epsilon) is the ratio of the volume of the gas before compression to the volume after compression.

        e = V_A / V_B
        e = (p_B / p_A) ^ (1 / gamma)
        e = (T_B / T_A) ^ (1 / (gamma - 1))
        """
        A, B = self.start, self.end

        e = safe(lambda: A.v / B.v)
        e = e or safe(lambda: (B.p / A.p) ** (1 / gamma))
        e = e or safe(lambda: (B.T / A.T) ** (1 / (gamma - 1)))
        return e

    def compute(self, R=287, gamma=1.4):
        """"""
        A, B = self.start, self.end

        # First try to compute the compression ratio e, using the data that is available
        e = self.compression_ratio(gamma)

        # Update the points
        A.update(R)
        B.update(R)

        # Using the compression ratio
        A.p = A.p or safe(lambda: B.p / e ** gamma)
        B.p = B.p or safe(lambda: A.p * e ** gamma)
        A.T = A.T or safe(lambda: B.T / e ** (gamma - 1))
        B.T = B.T or safe(lambda: A.T * e ** (gamma - 1))
        A.v = A.v or safe(lambda: B.v * e)
        B.v = B.v or safe(lambda: A.v / e)

    def work(self, R=287, gamma=1.4) -> float:
        """
        First law for a Closed system:
        
        Δu = q - w

        Δu: Change in internal energy.
        q: Heat transfer.
        w: Work done by the system

        For an isentropic process: q = 0 (No heat transfer)
        => Δu = -w or w = - Δu = - c_v ΔT

        Work done by the system: positive
        Work done on the system: negative
        """
        c_v = R / (gamma - 1)

        A, B = self.start, self.end
        return -c_v * (B.T - A.T)
        
if __name__ == "__main__":
    # Point('P1', T=298.00, p=1.00, v=85526.00)
    # Point('P2', T=911.25, p=50.00, v=5230.56)

    # Test 1 - T and p
    p1 = Point('P1', T=298.00, p=1.00)
    p2 = Point('P2', p=50.00)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

    p1 = Point('P1', p=1.00)
    p2 = Point('P2', T=911.25, p=50.00)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

    p1 = Point('P1', v=85526.00)
    p2 = Point('P2', T=911.25, v=5230.56)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

    p1 = Point('P1', T=298.00, v=85526.00)
    p2 = Point('P2', v=5230.56)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

    p1 = Point('P1', p=1.00, v=85526.00)
    p2 = Point('P2', v=5230.56)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)

    p1 = Point('P1', v=85526.00)
    p2 = Point('P2', p=50, v=5230.56)
    isentropic = Isentropic(p1, p2)
    isentropic.compute()
    print(p1)
    print(p2)