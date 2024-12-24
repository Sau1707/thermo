from collections import defaultdict
from .utils import safe

class Point:
    def __init__(self, name: str, *, 
                temperature: float = None,
                pressure: float = None,
                enthalpy: float = None,
                entropy: float = None,
                internal_energy: float = None,  
                volume: float = None):
        """
            Create a new point with the given properties. 
            The point only contains the data, does not compute anything.

            Args:
                name (str): The name of the point
                temperature (float): The temperature of the point
                pressure (float): The pressure of the point
                enthalpy (float): The enthalpy of the point
                entropy (float): The entropy of the point
                volume (float): The volume of the point
        """
        self.name = name

        self._default = defaultdict(lambda: None)
        self._computed = defaultdict(lambda: None)

        self._default["volume"] = volume # v
        self._default["pressure"] = pressure # p
        self._default["temperature"] = temperature # T

        self._default["entropy"] = entropy # s
        self._default["enthalpy"] = enthalpy # h
        self._default["internal_energy"] = internal_energy # u

    def __repr__(self):
        fn = lambda value: f"{value:.2f}" if isinstance(value, (int, float)) else "None"

        return (f"Point('{self.name}', "
                f"T={fn(self.temperature)}, "
                f"p={fn(self.pressure)}, "
                f"h={fn(self.enthalpy)}, "
                f"s={fn(self.entropy)}, "
                f"v={fn(self.volume)})")

    def update(self, R=287):
        """Update the point using the gas laws (p * v = R * T)"""

        self.v = self.v or safe(lambda: R * self.T / self.p)
        self.T = self.T or safe(lambda: self.p * self.v / R)
        self.p = self.p or safe(lambda: R * self.T / self.v)

    ############################################
    # Properties
    ############################################
    @property
    def temperature(self):
        return self._computed["temperature"] or self._default["temperature"]
    
    @temperature.setter
    def temperature(self, value):
        self._computed["temperature"] = value

    @property
    def pressure(self):
        return self._computed["pressure"] or self._default["pressure"]
    
    @pressure.setter
    def pressure(self, value):
        self._computed["pressure"] = value

    @property
    def enthalpy(self):
        return self._computed["enthalpy"] or self._default["enthalpy"]

    @enthalpy.setter
    def enthalpy(self, value):
        self._computed["enthalpy"] = value

    @property
    def entropy(self):
        return self._computed["entropy"] or self._default["entropy"]

    @entropy.setter
    def entropy(self, value):
        self._computed["entropy"] = value

    @property
    def volume(self):
        return self._computed["volume"] or self._default["volume"]

    @volume.setter
    def volume(self, value):
        self._computed["volume"] = value

    # Define aliases for the properties
    T = temperature
    p = pressure
    h = enthalpy
    s = entropy
    v = volume
    

if __name__ == "__main__":
    point = Point("Point 1", temperature=300, pressure=100)
    print(point)
    print("Temperature:", point.temperature)
    point.temperature = 400
    print("Temperature:", point.T)

    print("Pressure:", point.pressure)
    point.pressure = 200
    print("Pressure:", point.p)

    print("Enthalpy:", point.enthalpy)
    point.enthalpy = 200
    print("Enthalpy:", point.h)

    print("Entropy:", point.entropy)
    point.entropy = 200
    print("Entropy:", point.s)

    print("Volume:", point.volume)
    point.volume = 200
    print("Volume:", point.v)