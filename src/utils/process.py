from abc import ABC, abstractmethod
from .point import Point


class Process(ABC):
    """
    A generic thermodynamic process.

    Represents a transition between two points (A and B) in a thermodynamic cycle.
    Attributes:
        A (Point): The starting point of the process.
        B (Point): The ending point of the process.
        R (float): The gas constant.
        gamma (float): The specific heat ratio.
    """
    def __init__(self, A: Point, B: Point):
        self.A = A
        self.B = B

    @abstractmethod
    def compute(self):
        """Compute the properties of the end point"""
        pass

    @abstractmethod
    def work(self) -> float | None:
        """
        Return the work related to the process \\
        If negative, the work is done by the system \\
        If positive, the work is done on the system
        """
        pass

    @abstractmethod
    def heat(self) -> float | None:
        """
        Return the heat added in the process \\
        If negative, the heat is removed from the system \\
        If positive, the heat is added to the system
        """
        pass
    
    @abstractmethod
    def plot(self, ax_pv, ax_ts):
        """
        Plot the process on a P-V diagram and a T-S diagram
        """
        