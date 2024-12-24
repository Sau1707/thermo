from .step import Step
from .point import Point
from src.tables.specific_heats import SPECIFIC_HEATS
import matplotlib.pyplot as plt


class Cycle:
    """
        Generic Thermodynamic Process

        A process have multiple Steps. The last step added close the cycle.

        Once all the steps are added, the process can be analyzed
        We do a while loop in two directions. Until all the points are computed

        R = 287 J/kgK
        gamma
        c_p or c_v
    """
    def __init__(self, gas="air"):
        # The cycle can either be air or steam
        """
        Steam /  
        """

        """
        Air: Mixture of gases (primarily nitrogen and oxygen) that behaves as a single-phase gas under most practical conditions
        does not have a saturation line like water
        """
        R, k = SPECIFIC_HEATS[gas]
    
        # TODO: R and gamma can be computed using the properties of the gas
        self.R = R
        self.k = k
        self.steps: list[Step] = []

    def add_step(self, step: Step):
        self.steps.append(step)

    def solve(self):
        """
        TODO: Try to solve the process, raise and error if it's impossible
        """
        # First we loop over all he points and compute the missing properties if possible
        # -> air: gas -> GAS LAWS CAN BE USED
        # -> steam: liquid -> TABLES MUST BE USED

        for step in self.steps:
            step.compute(self.R, self.gamma)
        
    def plot(self):
        """
        TODO: Plot the process in a T-s and p-v diagram
        """

        # Get all the points
        points: list[Point] = []
        for step in self.steps:
            points.append(step.start)
            points.append(step.end)

        # Plot the T-s diagram
        plt.figure()
        plt.title("T-s Diagram")
        plt.xlabel("Entropy")
        plt.ylabel("Temperature")

        for point in points:
            print(point.entropy, point.temperature)
            plt.plot(point.entropy, point.temperature, "o")
        plt.show()

        # TODO: Add the lines between the points, this changes depending on the process

    def table(self):
        """
        TODO: Print a table with the properties of each point
        """


if __name__ == "__main__":
    p1 = Point("Point 1", temperature=833, pressure=80, enthalpy=3545.30, entropy=6.9072)
    p2 = Point("Point 2", temperature=593, pressure=7, enthalpy=2854.99, entropy=6.9072)
    p3 = Point("Point 3", temperature=418, pressure=0.1, enthalpy=191.81, entropy=0.6492, volume=0.00101)
    p4 = Point("Point 4", temperature=323, pressure=80, enthalpy=201.58, entropy=0.6504, volume=0.00100)

    s1 = Step(p1, p2)
    s2 = Step(p2, p3)
    s3 = Step(p3, p4)
    s4 = Step(p4, p1)

    cycle = Cycle()
    cycle.add_step(s1)
    cycle.add_step(s2)
    cycle.add_step(s3)
    cycle.add_step(s4)

    cycle.plot()
