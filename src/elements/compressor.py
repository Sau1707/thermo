from src.utils import State
from src.processes import Isentropic


class Compressor:
    """
    - Compressors are designed to work with gases or vapors (x = 1)
    - Gases are compressible, so compressors increase the gas's pressure by reducing its volume
    - Adds energy to the gas, causing a rise in both pressure and temperature due to compression

    Ideal compressor (s1 = s2)

    Real compressor (s1 < s2)
    - The actual compression process is irreversible -> has an efficiency (μ)

    """

    def __init__(self, μ: float = 1, *, A: State, B: State):
        assert 0 < μ <= 1, "The efficiency must be between 0 and 1"
        self.μ = μ
        self.A = A
        self.B = B
        self.S = State()

        self.ideal = Isentropic(A=self.A, B=self.S)
        
        # -> Solve the ideal process
        """
        μ = (h_2s - h_1) / (h_2 - h_1) = (T_2s - T_1) / (T_2 - T_1)
        """
        # Using Mu, solve the real process
