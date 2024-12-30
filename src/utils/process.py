from .state import State
from .functions import safe
from .gas import AIR
from ..tables.water import TABLE_SATURATED, TABLE_OVERHEATED
from ..tables.overheated import TableOverheated


class Process:
    """
    A generic thermodynamic process.

    Represents a transition between two states (A and B) in a thermodynamic cycle.
    Attributes:
        gas (str): The gas used in the process.
        A (Point): The starting point of the process.
        B (Point): The ending point of the process.
    """
    def __init__(self, gas: str, *, A: State, B: State):
        self.gas = gas.upper()
        self.A = A
        self.B = B

    def _compute_gas_state(self, s: State):
        """Compute the properties of a state using the ideal gas laws and the specific heat relationships"""
        # (p * v = R * T) and (h = c_p * T) and (u = c_v * T)
        s.T = s.T or safe(lambda: s.p * s.v / AIR.R) or safe(lambda: s.h / AIR.c_p) or safe(lambda: s.u / AIR.c_v)
        s.v = s.v or safe(lambda: AIR.R * s.T / s.p)
        s.p = s.p or safe(lambda: AIR.R * s.T / s.v)
        s.h = s.h or safe(lambda: AIR.c_p * s.T)
        s.u = s.u or safe(lambda: AIR.c_v * s.T)

    def _compute_overheated_state(self, s: State, table: TableOverheated):
        obj = table.get(p=s.get_pressure("bar"), T=s.get_temperature("C"))
        s.v = s.v or obj.v
        s.u = s.u or obj.u * 1e3
        s.h = s.h or obj.h * 1e3
        s.s = s.s or obj.s * 1e3

    def compute(self):
        """Compute the properties of the end point"""
        match self.gas:
            # If the gas is air, than we can use the ideal gas laws and the specific heat relationships
            case "AIR":
                self._compute_gas_state(self.A)
                self._compute_gas_state(self.B)
                return
            
            # If the gas is steam, than we can use the steam tables
            case "STEAM":
                if self.A.p and self.A.T:
                    self._compute_overheated_state(self.A, TABLE_OVERHEATED)
                    self._compute_overheated_state(self.B, TABLE_OVERHEATED)
        
        # TODO: If the gas is a refrigerant, than we can use the refrigerant tables
        if self.gas == "REFRIGERANT-12":
            pass

        # TODO: If the gas is ammonia, than we can use the ammonia tables
        if self.gas == "AMMONIA":
            pass

        pass

    def work(self) -> float | None:
        """
        Return the work related to the process \\
        If negative, the work is done by the system \\
        If positive, the work is done on the system
        """
        raise NotImplementedError

    def heat(self) -> float | None:
        """
        Return the heat added in the process \\
        If negative, the heat is removed from the system \\
        If positive, the heat is added to the system
        """
        raise NotImplementedError
    
    def plot(self, ax_pv, ax_ts):
        """
        Plot the process on a P-V diagram and a T-S diagram
        """
        raise NotImplementedError 
    
    def __repr__(self):
        return (f"Process('{self.gas}', A ---> B)\n"
                f"A: {self.A}\n"
                f"B: {self.B}")


if __name__ == "__main__":
    # Simple GAS
    s1 = State("1", p="1 bar", T=300)
    s2 = State("2", h=301350)
    p = Process("AIR", A=s1, B=s2)
    p.compute()

    assert round(s1.p, 2) == 100000 # To PA
    assert round(s1.v, 2) == 0.86   # To be checked
    assert round(s1.h, 2) == 301350 # Tutorial 5 - (1)
    assert round(s1.u, 2) == 215250 # To be checked

    assert round(s2.T, 2) == 300    # Reverse Tutorial 5 - (1)

    # Tables
    s1 = State("1", p="80 bar", T="480 C", x=1)
    s2 = State("2", T="440 C", x=1, p="8.10 bar")
    p = Process("STEAM", A=s1, B=s2)
    p.compute()
    print(p)
    assert round(s1.p, 2) == 8000000 # To PA
    assert round(s1.T, 2) == 753.15   # To K
    assert round(s1.h, 2) == 3348400 # Tutorial 2 - (b - 1)
    assert round(s1.s, 2) == 6658.6  # Tutorial 2 - (b - 1)

    # Tutorial 2 - b) 3
    assert round(s2.p, 2) == 810000, "Test failed"
    assert round(s2.h, 0) == 3351833, "Test failed"
    assert round(s2.s, 1) == 7695.2, "Test failed"
    