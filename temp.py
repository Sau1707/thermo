class Pressure(float):
    """Represents the force exerted by the gas per unit area.
    
    [Pa] (Pascal)
    """

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def from_bar(cls, value: float):
        return cls(value * 1e5)

    @classmethod
    def from_atm(cls, value: float):
        return cls(value * 101325)

    def to_bar(self):
        return self.value / 1e5

    def to_atm(self):
        return self.value / 101325


class SpecificVolume(float):
    """Represents the specific volume occupied by the gas in the system ().

    [m^3/kg] (cubic meter per kilogram)
    """

    def __init__(self, value: float):
        self.value = value  # Specific volume in m^3/kg

    @classmethod
    def from_liter_per_kg(cls, value: float):
        return cls(value * 1e-3)

    @classmethod
    def from_cm3_per_kg(cls, value: float):
        return cls(value * 1e-6)

    def to_liter_per_kg(self):
        return self.value * 1e3

    def to_cm3_per_kg(self):
        return self.value * 1e6


class Temperature(float):
    """
    Represents the absolute temperature of the gas, measured from absolute zero.

    [K] (Kelvin)
    """

    def __init__(self, value: float):
        self.value = value  # Temperature in Kelvin (K)

    @classmethod
    def from_celsius(cls, value: float):
        return cls(value + 273.15)

    @classmethod
    def from_fahrenheit(cls, value: float):
        return cls((value - 32) * 5 / 9 + 273.15)

    def to_celsius(self):
        return self.value - 273.15

    def to_fahrenheit(self):
        return (self.value - 273.15) * 9 / 5 + 32


class MassFlow(float):
    """Represents the mass flow rate of the gas in the system (kg/s).

    [kg/s] (kilogram per second)
    """

    def __init__(self, value: float):
        self.value = value  # Mass flow rate in kg/s

    @classmethod
    def from_kg_per_s(cls, value: float):
        return cls(value)

    @classmethod
    def from_g_per_s(cls, value: float):
        return cls(value / 1000)

    def to_kg_per_s(self):
        return self.value

    def to_g_per_s(self):
        return self.value * 1000


class SpecificGasConstant(float):
    """Represents the specific gas constant of the gas in the system (J/kg.K).

    [J/kg.K] (Joule per kilogram Kelvin)
    """

    def __init__(self, value: float):
        self.value = value


class AdiabaticIndex(float):
    """Represents the adiabatic index of the gas in the system.

        [] (dimensionless)
    """

    def __init__(self, value: float):
        self.value = value