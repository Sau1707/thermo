

class State:
    """
        Represent a point in a thermodynamic system.
    """

    name: str = None # Name of the point

    p: float = None # Pressure [Pa]
    T: float = None # Temperature [K]
    v: float = None # Specific volume [m^3/kg]
    u: float = None # Specific internal energy [J/kg]
    h: float = None # Specific enthalpy [J/kg]
    s: float = None # Specific entropy [J/kgK]

    # Steam / Tables only only
    x: float = None # Ratio of steam to water [0-1]
    u_f: float = None # Specific internal energy of saturated liquid [J/kg]
    u_g: float = None # Specific internal energy of saturated vapor [J/kg]
    h_f: float = None # Specific enthalpy of saturated liquid [J/kg]
    h_g: float = None # Specific enthalpy of saturated vapor [J/kg]
    s_f: float = None # Specific entropy of saturated liquid [J/kgK]
    s_g: float = None # Specific entropy of saturated vapor [J/kgK]

    def __init__(self, name: str, *, p: float | str = None, T: float | str = None, v: float = None, u: float = None, h: float = None, s: float = None, x: float = None, u_f: float = None, u_g: float = None, h_f: float = None, h_g: float = None, s_f: float = None, s_g: float = None):
        # Try to load the temperature and the pressure
        if isinstance(p, str):
            p = p.replace(" ", "")
            if "bar" in p:
                p = float(p.replace("bar", "")) * 1e5
            elif "kPa" in p:
                p = float(p.replace("kPa", "")) * 1e3
            elif "MPa" in p:
                p = float(p.replace("MPa", "")) * 1e6
            elif "Pa" in p:
                p = float(p.replace("Pa", ""))

        if isinstance(T, str):
            T = T.replace(" ", "")
            if "C" in T:
                T = float(T.replace("C", "")) + 273.15
            elif "K" in T:
                T = float(T.replace("K", ""))
        
        self.name = name
        self.p = p
        self.T = T
        self.v = v
        self.u = u
        self.h = h
        self.s = s
        self.x = x
        self.u_f = u_f
        self.u_g = u_g
        self.h_f = h_f
        self.h_g = h_g
        self.s_f = s_f
        self.s_g = s_g

    def __repr__(self):
        fn = lambda value: f"{value:.2f}" if isinstance(value, (int, float)) else "None"

        return (f"Point('{self.name}', "
                f"p={fn(self.p)}, " 
                f"T={fn(self.T)}, " 
                f"v={fn(self.v)}, " 
                f"u={fn(self.u)}, " 
                f"h={fn(self.h)}, " 
                f"s={fn(self.s)}, " 
                f"x={fn(self.x)}, " 
                f"u_f={fn(self.u_f)}, " 
                f"u_g={fn(self.u_g)}, " 
                f"h_f={fn(self.h_f)}, " 
                f"h_g={fn(self.h_g)}, " 
                f"s_f={fn(self.s_f)}, " 
                f"s_g={fn(self.s_g)})")

    def get_temperature(self, unit="K") -> float:
        match unit:
            case "K":
                return self.T
            case "C":
                return self.T - 273.15
        raise ValueError(f"Invalid unit '{unit}'")
       
    def get_pressure(self, unit="Pa") -> float:
        match unit:
            case "Pa":
                return self.p
            case "kPa":
                return self.p / 1000
            case "bar":
                return self.p / 1e5
        raise ValueError(f"Invalid unit '{unit}'")


if __name__ == "__main__":
    s = State("Test")
    print(s)