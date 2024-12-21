from abc import ABC, abstractmethod
from .point import Point


class Step(ABC):
    """
        A single step in a thermodynamic process

        it has a start and and end point
    """
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end

    @property
    def start(self):
        return self._start
    
    @property
    def end(self):
        return self._end

    def compute(self, R: float, gamma: float):
        """
            Compute the properties of the end point
            Tries first in one direction and then in the other one
        """

    def get_heat_flow(self, **kwargs):
        """
            Compute the heat flow in the process

            Q / m = h2 - h1
        """
        