

class State:
    name: str = None # Name of the point

    p: float = None # Pressure [Pa]
    T: float = None # Temperature [K]
    v: float = None # Specific volume [m^3/kg]
    u: float = None # Specific internal energy [J/kg]
    h: float = None # Specific enthalpy [J/kg]
    s: float = None # Specific entropy [J/kgK]

    # Steam only
    x: float = None # Ratio of steam to water [0-1]

    def __repr__(self):
        fn = lambda value: f"{value:.2f}" if isinstance(value, (int, float)) else "None"

        return (f"Point('{self.name}', "
                f"T={fn(self.T)}, "
                f"p={fn(self.p)}, "
                f"v={fn(self.v)}, "
                f"u={fn(self.u)}, "
                f"h={fn(self.h)}, "
                f"s={fn(self.s)}),"
                f"x={fn(self.x)}")

    def get_temperature(self, unit="K") -> float:
        match unit:
            case "K":
                return self.T
            case "°C":
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
